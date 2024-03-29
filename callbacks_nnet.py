from tensorflow.keras.callbacks import Callback
import time


class CallBackTrainNNet(Callback):
    def __init__(self, log, draw_graphs, clear_batch_graphs, update_progressbars, need_stop, max_batch, update_range):
        super(CallBackTrainNNet, self).__init__()
        self.log = log
        self.draw_graphs = draw_graphs
        self.clear_batch_graphs = clear_batch_graphs
        self.update_progressbars = update_progressbars
        self.update_range = update_range
        self.need_stop = need_stop
        self.max_batch = max_batch
        self.train_started = False

        # initialize arrays for epoch graphs
        self.arr_epoch_index = [0]
        self.arr_epoch_acc = {'train': [0], 'val': [0]}
        self.arr_epoch_loss = {'train': [1], 'val': [1]}
        self.epoch_cnt = 0

        # initialize arrays for batch graphs
        self.arr_batch_index = [0]
        self.arr_batch_acc = [0]
        self.arr_batch_loss = [1]
        self.batch_sum = 0
        self.batch_cnt = 0

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
        self.draw_graphs['EPOCH'].emit(self.arr_epoch_index, self.arr_epoch_acc['train'], self.arr_epoch_acc['val'],
                                       self.arr_epoch_loss['train'], self.arr_epoch_loss['val'])

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

        # limit loss
        avg_loss = 1 if avg_loss > 1 else avg_loss

        # append values for graphs
        self.arr_batch_acc.append(avg_acc)
        self.arr_batch_loss.append(avg_loss)

        # start window sliding only when reached to maximum
        if self.batch_cnt >= self.max_batch:
            window_batch_index = self.arr_batch_index[-self.max_batch:]
            window_batch_loss = self.arr_batch_loss[-self.max_batch:]
            window_batch_acc = self.arr_batch_acc[-self.max_batch:]
            self.update_range.emit()
        else:
            window_batch_index = self.arr_batch_index
            window_batch_loss = self.arr_batch_loss
            window_batch_acc = self.arr_batch_acc

        # update graphs
        self.draw_graphs['BATCH'].emit(window_batch_index, window_batch_acc, window_batch_loss)


class CallBackSinglePredictNNet(Callback):
    def __init__(self, update_batch_progress):
        super(CallBackSinglePredictNNet, self).__init__()
        self.update_batch_progress = update_batch_progress
        self.batch_sum = 0
        self.predict_start = False

    def on_predict_begin(self, logs=None):
        self.batch_sum = 0
        self.predict_start = True

    def on_predict_batch_end(self, batch, logs=None):
        # calculate batch percentage for progressbar
        samples = self.params['samples']
        self.batch_sum += logs['size']
        batch_progress = (self.batch_sum / samples) * 100

        # update progressbar
        self.update_batch_progress.emit(batch_progress)


class CallBackMultiPredictNNet(CallBackSinglePredictNNet):
    def __init__(self, update_batch_progress, update_tweets_progress, total_tweets):
        super(CallBackMultiPredictNNet, self).__init__(update_batch_progress)
        self.update_tweets_progress = update_tweets_progress
        self.total_tweets = total_tweets
        self.tweets_num = 0

    def on_predict_end(self, logs=None):
        self.tweets_num += 1
        tweets_progress = (self.tweets_num / self.total_tweets) * 100

        # update progressbar
        self.update_tweets_progress.emit(tweets_progress)

        self.predict_start = False
