from run_nnet import ModelSinglePredictorThread, SinglePredictor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFile, QTextStream
from callbacks_nnet import CallBackSinglePredictNNet
import os
import sys
import glob
sys.path.append('gui/')
from gui.singleanalyzer_ui import Ui_SingleAnalyzer


class SingleAnalyzerController(QMainWindow):
    def __init__(self, parent=None):
        super(SingleAnalyzerController, self).__init__(parent)
        self.parent = parent
        self.main = QFrame()
        self.ui = Ui_SingleAnalyzer()
        self.ui.setupUi(self.main)
        self._load_stylesheet()
        self.load_models_names()

        #TODO: fix alignment on tweet textbox - with wrapping

        # connect listeners
        self.ui.btn_homepage.clicked.connect(self.back_homepage)
        self.ui.textbox_tweet.textChanged.connect(self.tweet_text_changed)
        self.ui.btn_start.clicked.connect(self.start_predict)

    def _load_stylesheet(self):
        file = QFile('./css/SingleAnalyzer.qss')
        file.open(QFile.ReadOnly)
        stream = QTextStream(file)
        text = stream.readAll()
        self.main.setStyleSheet(text)

    def tweet_text_changed(self):
        tweet_text = self.ui.textbox_tweet.toPlainText()
        if len(tweet_text) > 0:
            self.ui.btn_start.setDisabled(False)
        else:
            self.ui.btn_start.setDisabled(True)

    def show(self):
        self.main.show()

    def back_homepage(self):
        self.parent.show()
        self.main.close()

    def load_models_names(self):
        model_files = glob.glob('output/*.h5')
        fix_files = list(map(lambda x: os.path.basename(x).split('.')[0], model_files))
        self.ui.combobox_model.addItems(fix_files)

    def start_predict(self):
        model_name = str(self.ui.combobox_model.currentText())
        tweet_text = self.ui.textbox_tweet.toPlainText()

        # reset fields
        self.ui.progressbar_batch.setValue(0)
        self.ui.lbl_result.setText('The Tweet is a Bot With Probability of 0%')

        model_callback = CallBackPredictNNet(self)
        predictor = SinglePredictor(model_name, model_callback)

        self.ui.btn_start.setDisabled(True)

        # create a thread for predictor
        pred_thread = ModelSinglePredictorThread(predictor, tweet_text, self)
        pred_thread.start()