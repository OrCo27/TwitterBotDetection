from tensorflow.keras.callbacks import Callback


class CallBackNNet(Callback):
    def __init__(self, logger, conf_controller, check_exit_breakpoint):
        super(CallBackNNet, self).__init__()
        self.logger = logger
        self.conf_controller = conf_controller
        self.check_exit_breakpoint = check_exit_breakpoint
        self.batch_sum = 0
        self.batch_cnt = 0
        self.epoch_cnt = 0
        self.arr_epoch_index = [0]
        self.arr_batch_index = [0]
        self.arr_epoch_acc = {'train': [0], 'val': [0]}
        self.arr_epoch_loss = {'train': [1], 'val': [1]}
        self.arr_batch_acc = [0]
        self.arr_batch_loss = [1]

    def stop_train(self):
        self.model.stop_training = True

    def on_epoch_begin(self, epoch, logs=None):
        """ Called at the start of an epoch """
        self.batch_cnt = 0
        self.batch_sum = 0
        self.arr_batch_index = [0]
        self.arr_batch_acc = [self.arr_batch_acc[-1]]
        self.arr_batch_loss = [self.arr_batch_loss[-1]]

    def on_epoch_end(self, batch, logs={}):
        if self.conf_controller.is_stopped():
            return

        # extract parameters about current epoch
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
        self.conf_controller.ui.progressbar_epoches.setValue(epoch_progress)
        self.conf_controller.log.write_log(f'Epoch {self.epoch_cnt}/{epochs} | loss: {loss:.4f} - accuracy: '
                                           f'{acc:.4f} - val_loss: {val_loss:.4f} - val_accuracy: {val_acc:.4f}')

        # update epoch graphs
        self.conf_controller.plot_epoch_acc(self.arr_epoch_index, self.arr_epoch_acc['train'],
                                            self.arr_epoch_index, self.arr_epoch_acc['val'])

        self.conf_controller.plot_epoch_loss(self.arr_epoch_index, self.arr_epoch_loss['train'],
                                             self.arr_epoch_index, self.arr_epoch_loss['val'])

    def on_train_batch_end(self, batch, logs=None):
        if self.conf_controller.is_stopped():
            return

        # extract parameters about current epoch
        loss = logs['loss']
        acc = logs['accuracy']
        samples = self.params['samples']

        # calculate batch percentage for progressbar
        self.batch_sum += logs['size']
        batch_progress = (self.batch_sum / samples) * 100
        self.batch_cnt += 1

        self.arr_batch_index.append(self.batch_cnt)

        # calculate new accumulative average
        avg_acc = ((self.batch_cnt - 1) * self.arr_batch_acc[-1] + acc) / self.batch_cnt
        avg_loss = ((self.batch_cnt - 1) * self.arr_batch_loss[-1] + loss) / self.batch_cnt

        # append values for graphs
        self.arr_batch_acc.append(avg_acc)
        self.arr_batch_loss.append(avg_loss)

        # update progressbar
        self.conf_controller.ui.progressbar_batch.setValue(batch_progress)

        # update graphs
        self.conf_controller.plot_batch_acc(self.arr_batch_index, self.arr_batch_acc)
        self.conf_controller.plot_batch_loss(self.arr_batch_index, self.arr_batch_loss)

    def on_train_batch_begin(self, batch, logs=None):
        # stopping break - if there is a request - exit
        self.check_exit_breakpoint(exit_process=self.stop_train)

    def on_predict_begin(self, logs=None):
        """ Called at the beginning of prediction """
        pass

    def on_predict_batch_end(self, batch, logs=None):
        """ Called at the end of a batch in predict methods """
        pass
