from tensorflow.keras.callbacks import Callback


class CallBackNNet(Callback):
    def __init__(self, logger, conf_controller):
        super(CallBackNNet, self).__init__()
        self.logger = logger
        self.conf_controller = conf_controller

    def on_epoch_begin(self, epoch, logs=None):
        """ Called at the start of an epoch """
        pass

    def on_epoch_end(self, batch, logs={}):
        """ Called at the end of an epoch """
        pass

    def on_batch_end(self, batch, logs=None):
        """ Called at the end of a training batch in fit methods """
        pass

    def on_predict_begin(logs=None):
        """ Called at the beginning of prediction """
        pass

    def on_predict_batch_end(self, batch, logs=None):
        """ Called at the end of a batch in predict methods """
        pass
