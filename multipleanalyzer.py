from run_nnet import ModelMultiplePredictorThread, MultiPredictor
from callbacks_nnet import CallBackMultiPredictNNet
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFile, QTextStream
from utils_nnet import ModelCommon as Utils
import os
import sys
import glob
sys.path.append('gui/')
from gui.multipleanalyzer_ui import Ui_MultipleAnalayzer


class MultipleAnalyzerController(QMainWindow):
    def __init__(self, parent=None):
        super(MultipleAnalyzerController, self).__init__(parent)
        self.parent = parent
        self.main = QFrame()
        self.ui = Ui_MultipleAnalayzer()
        self.ui.setupUi(self.main)
        self._load_stylesheet()
        self.load_models_names()
        self.predictor = None

        # connect listeners
        self.ui.btn_homepage.clicked.connect(self.back_homepage)
        self.ui.btn_tweets_file.clicked.connect(self.open_file)
        self.ui.btn_start.clicked.connect(self.start_predict)
        self.ui.btn_classify.clicked.connect(self.classify_tweets)
        #TODO: add save button for export to excel

    def _load_stylesheet(self):
        file = QFile('./css/MultipleAnalyzer.qss')
        file.open(QFile.ReadOnly)
        stream = QTextStream(file)
        text = stream.readAll()
        self.main.setStyleSheet(text)

    def open_file(self):
        try:
            filter = "CSV files (*.csv);;Text files (.txt)"
            file_path, _ = QFileDialog.getOpenFileName(self, "Please select a file", "./data/", filter)
            if file_path:
                self.ui.textbox_tweets_file.setText(file_path)

        except IOError as e:
            pass

    def show(self):
        self.main.show()

    def back_homepage(self):
        self.parent.show()
        self.main.close()

    def load_models_names(self):
        model_files = glob.glob('output/*.h5')
        fix_files = list(map(lambda x: os.path.basename(x).split('.')[0], model_files))
        self.ui.combobox_model.addItems(fix_files)

    def classify_tweets(self):
        threshold = self.ui.spinbox_threshold.value()
        self.predictor.classify_by_threshold(threshold=threshold)
        bots_part = self.predictor.get_bots_distribution()
        rounded_bots_part = int(round(bots_part * 100))

        #TODO: show to pie chart
        print(rounded_bots_part)

    def start_predict(self):
        # get predicting parameters
        model_name = str(self.ui.combobox_model.currentText())
        tweets_file = self.ui.textbox_tweets_file.text()
        header_included = self.ui.checkbox_header.isChecked()
        random_tweets = self.ui.spinbox_rand_tweets.value()

        # check for file validity
        try:
            Utils.file_validation(tweets_file, 'Tweet')
        except Exception as ex:
            Utils.show_error(text=ex.args[0], title="Input Error")
            return

        # reset progressbars
        self.ui.progressbar_batch.setValue(0)
        self.ui.progressbar_tweets.setValue(0)

        self.ui.btn_start.setDisabled(True)
        self.ui.btn_classify.setDisabled(True)
        self.ui.btn_save.setDisabled(True)

        model_callback = CallBackMultiPredictNNet(self, random_tweets)
        self.predictor = MultiPredictor(model_name, model_callback)

        # create a thread for predictor
        pred_thread = ModelMultiplePredictorThread(self.predictor, tweets_file, header_included, random_tweets, self)
        pred_thread.start()