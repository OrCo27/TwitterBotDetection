from tensorflow.keras.callbacks import Callback
import time


class CallBackTrainNNet(Callback):
    def __init__(self, log, draw_graphs, clear_batch_graphs, update_progressbars, need_stop):
        super(CallBackTrainNNet, self).__init__()
        self.log = log
        self.draw_graphs = draw_graphs
        self.clear_batch_graphs = clear_batch_graphs
        self.update_progressbars = update_progressbars
        self.need_stop = need_stop
        self.batch_sum = 0
        self.batch_cnt = 0
        self.epoch_cnt = 0
        self.arr_epoch_index = [0]
        self.arr_batch_index = [0]
        self.arr_epoch_acc = {'train': [0], 'val': [0]}
        self.arr_epoch_loss = {'train': [1], 'val': [1]}
        self.arr_batch_acc = [0]
        self.arr_batch_loss = [1]
        self.train_started = False
        self.need_stop = need_stop

    def stop_train(self):
        self.model.stop_training = True

    def on_train_begin(self, logs=None):
        self.train_started = True

    def on_epoch_begin(self, epoch, logs=None):
        """ Called at the start of an epoch """
        if self.need_stop():
            return

        self.batch_cnt = 0
        self.batch_sum = 0
        self.arr_batch_index = [0]
        self.arr_batch_acc = [self.arr_batch_acc[-1]]
        self.arr_batch_loss = [self.arr_batch_loss[-1]]
        self.clear_batch_graphs.emit()

    def on_epoch_end(self, batch, logs={}):
        # extract parameters about current epoch
        if self.need_stop():
            return

        loss = logs['loss']
        acc = logs['accuracy']
        val_loss = logs['val_loss']
        val_acc = logs['val_accuracy']
        epochs = self.params['epochs']

        # calculate values for updating progressbar
        self.epoch_cnt += 1
        epoch_progress = (self.epoch_cnt / epochs) * 100

        # append values for graphs
        self.arr_epoch_index.append(self.epoch_cnt)
        self.arr_epoch_acc['train'].append(acc)
        self.arr_epoch_acc['val'].append(val_acc)
        self.arr_epoch_loss['train'].append(loss)
        self.arr_epoch_loss['val'].append(val_loss)

        # update progressbar and logs
        self.update_progressbars['EPOCH'].emit(epoch_progress)
        self.log.write_log(f'Epoch {self.epoch_cnt}/{epochs} | loss: {loss:.4f} - accuracy: '
                           f'{acc:.4f} - val_loss: {val_loss:.4f} - val_accuracy: {val_acc:.4f}')

        # update epoch graphs
        self.draw_graphs['EPOCH_ACC'].emit(self.arr_epoch_index, self.arr_epoch_acc['train'],
                                           self.arr_epoch_index, self.arr_epoch_acc['val'])

        self.draw_graphs['EPOCH_LOSS'].emit(self.arr_epoch_index, self.arr_epoch_loss['train'],
                                            self.arr_epoch_index, self.arr_epoch_loss['val'])

    def on_batch_end(self, batch, logs=None):
        # extract parameters about current epoch
        if self.need_stop():
            return

        loss = logs['loss']
        acc = logs['accuracy']
        batch_size = logs['size']
        samples = self.params['samples']

        # calculate batch percentage for progressbar
        self.batch_sum += batch_size
        batch_progress = (self.batch_sum / samples) * 100
        self.batch_cnt += 1

        # update progressbar
        self.update_progressbars['BATCH'].emit(batch_progress)

        self.arr_batch_index.append(self.batch_cnt)

        # calculate new accumulative average
        avg_acc = ((self.batch_cnt - 1) * self.arr_batch_acc[-1] + acc) / self.batch_cnt
        avg_loss = ((self.batch_cnt - 1) * self.arr_batch_loss[-1] + loss) / self.batch_cnt

        # append values for graphs
        self.arr_batch_acc.append(avg_acc)
        self.arr_batch_loss.append(avg_loss)

        # update graphs
        self.draw_graphs['BATCH_ACC'].emit(self.arr_batch_index, self.arr_batch_acc)
        self.draw_graphs['BATCH_LOSS'].emit(self.arr_batch_index, self.arr_batch_loss)

    def on_batch_begin(self, batch, logs=None):
        pass
        #self.stop_train()

class CallBackSinglePredictNNet(Callback):
    def __init__(self, single_controller):
        super(CallBackSinglePredictNNet, self).__init__()
        self.single_controller = single_controller
        self.batch_sum = 0

    def on_predict_begin(self, logs=None):
        self.batch_sum = 0

    def on_predict_batch_end(self, batch, logs=None):
        # calculate batch percentage for progressbar
        samples = self.params['samples']
        self.batch_sum += logs['size']
        batch_progress = (self.batch_sum / samples) * 100

        # update progressbar
        self.single_controller.ui.progressbar_batch.setValue(batch_progress)


class CallBackMultiPredictNNet(Callback):
    def __init__(self, multi_controller, rand_tweets):
        super(CallBackMultiPredictNNet, self).__init__()
        self.multi_controller = multi_controller
        self.rand_tweets = rand_tweets
        self.batch_sum = 0
        self.tweets_num = 0

    def on_predict_begin(self, logs=None):
        self.batch_sum = 0

    def on_predict_batch_end(self, batch, logs=None):
        # calculate batch percentage for progressbar
        samples = self.params['samples']
        self.batch_sum += logs['size']
        batch_progress = (self.batch_sum / samples) * 100

        # update progressbar
        self.multi_controller.ui.progressbar_batch.setValue(batch_progress)

    def on_predict_end(self, logs=None):
        self.tweets_num += 1
        tweets_progress = (self.tweets_num / self.rand_tweets) * 100

        # update progressbar
        self.multi_controller.ui.progressbar_tweets.setValue(tweets_progress)
