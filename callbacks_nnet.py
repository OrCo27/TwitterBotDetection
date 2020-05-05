from tensorflow.keras.callbacks import Callback


class CallBackNNet(Callback):
    def __init__(self, logger, conf_controller):
        super(CallBackNNet, self).__init__()
        self.logger = logger
        self.conf_controller = conf_controller
        self.batch_sum = 0
        self.epoch_cnt = 0

    #TODO: add exit breakpoints every epoch/batch

    def on_epoch_begin(self, epoch, logs=None):
        """ Called at the start of an epoch """
        self.batch_sum = 0

    def on_epoch_end(self, batch, logs={}):
        """ Called at the end of an epoch """
        loss = logs['loss']
        acc = logs['accuracy']
        val_loss = logs['val_loss']
        val_acc = logs['val_accuracy']
        epoches = self.params['epochs']
        self.epoch_cnt += 1
        epoch_progress = (self.epoch_cnt / epoches) * 100

        # update progressbar and logs
        self.conf_controller.ui.progressbar_epoches.setValue(epoch_progress)
        self.conf_controller.log.write_log(f'Epoch {self.epoch_cnt}/{epoches} | loss: {loss} - accuracy: {acc} - '
                                           f'val_loss: {val_loss} - val_accuracy: {val_acc}')

    def on_batch_end(self, batch, logs=None):
        """ Called at the end of a training batch in fit methods """
        samples = self.params['samples']
        self.batch_sum += logs['size']
        batch_progress = (self.batch_sum / samples) * 100

        # update progressbar
        self.conf_controller.ui.progressbar_batch.setValue(batch_progress)

    def on_batch_begin(self, batch, logs=None):
        pass

    def on_predict_begin(logs=None):
        """ Called at the beginning of prediction """
        pass

    def on_predict_batch_end(self, batch, logs=None):
        """ Called at the end of a batch in predict methods """
        pass
