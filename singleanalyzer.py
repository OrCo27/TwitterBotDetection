from run_nnet import SinglePredictor, ModelPredictorThread
from utils_nnet import ModelCommon as Utils
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFile, QTextStream, pyqtSignal
from callbacks_nnet import CallBackSinglePredictNNet
import os
import sys
import numpy as np
sys.path.append('gui/')
from gui.singleanalyzer_ui import Ui_SingleAnalyzer


class SingleAnalyzerController(QMainWindow):

    # qt signals
    update_progress = pyqtSignal(int)

    def __init__(self, parent=None):
        super(SingleAnalyzerController, self).__init__(parent)
        self.parent = parent
        self.main = QFrame()
        self.ui = Ui_SingleAnalyzer()
        self.ui.setupUi(self.main)
        self._load_stylesheet()
        self.load_models_names()

        self.pred_thread = None
        self.predictor = None

        # connect listeners
        self.ui.btn_homepage.clicked.connect(self.back_homepage)
        self.ui.textbox_tweet.textChanged.connect(self.check_validation)
        self.ui.combobox_model.currentIndexChanged.connect(self.check_validation)
        self.ui.btn_start.clicked.connect(self.start_predict)

        # connect signals
        self.update_progress.connect(self.ui.progressbar_batch.setValue)

    def _load_stylesheet(self):
        file = QFile('./css/SingleAnalyzer.qss')
        file.open(QFile.ReadOnly)
        stream = QTextStream(file)
        text = stream.readAll()
        self.main.setStyleSheet(text)

    def check_validation(self):
        model_index = self.ui.combobox_model.currentIndex()
        tweet_text = self.ui.textbox_tweet.toPlainText()

        if (len(tweet_text) > 0) and model_index > 0:
            self.ui.btn_start.setDisabled(False)
        else:
            self.ui.btn_start.setDisabled(True)

    def show(self):
        self.main.show()

    def back_homepage(self):
        self.parent.show()
        self.main.close()

    def load_models_names(self):
        model_names = SinglePredictor.get_models_names()
        self.ui.combobox_model.addItems(model_names)

    def update_ui_scores(self, bot_percentage, human_percentage):
        self.ui.lbl_bot_result.setText(f'{bot_percentage}%')
        self.ui.lbl_human_result.setText(f'{human_percentage}%')

        self.ui.groupbox_human.setDisabled(False)
        self.ui.groupbox_bot.setDisabled(False)
        self.ui.progressbar_human.setValue(human_percentage)
        self.ui.progressbar_bot.setValue(bot_percentage)
        QApplication.processEvents()

    def reset_form(self):
        self.ui.progressbar_batch.setValue(0)
        self.update_ui_scores(0, 0)
        self.ui.groupbox_bot.setDisabled(True)
        self.ui.groupbox_human.setDisabled(True)

    def start_predict(self):
        # extract inputs from gui
        model_index = self.ui.combobox_model.currentIndex()
        model_name = str(self.ui.combobox_model.currentText())
        tweet_text = self.ui.textbox_tweet.toPlainText()

        # reset fields
        self.reset_form()
        self.ui.btn_start.setDisabled(True)
        self.ui.textbox_tweet.setReadOnly(True)
        self.ui.combobox_model.setDisabled(True)

        model_callback = CallBackSinglePredictNNet(self.update_progress)
        self.predictor = SinglePredictor(model_name, model_callback)
        self.predictor.set_single_tweet(tweet_text)

        # create a thread for predictor
        self.pred_thread = ModelPredictorThread(self.predictor)
        self.pred_thread.finished.connect(self.on_predict_finished)
        self.pred_thread.start()

    def on_predict_finished(self):
        if self.pred_thread.is_success():
            bot_sim_score = self.predictor.get_similarity_score()
            bot_percentage = int(round(bot_sim_score * 100))
            human_percentage = 100 - bot_percentage

            # calculate the max value for ui
            scores_arr = [bot_percentage, human_percentage]
            group_boxes_arr = [self.ui.groupbox_bot, self.ui.groupbox_human]
            max_element = np.argmax(scores_arr)
            min_element = 1-max_element

            self.update_ui_scores(bot_percentage, human_percentage)

            group_boxes_arr[max_element].setDisabled(False)
            group_boxes_arr[min_element].setDisabled(True)
        else:
            Utils.show_error(text=self.pred_thread.error, title="Error")

        self.ui.btn_start.setDisabled(False)
        self.ui.textbox_tweet.setReadOnly(False)
        self.ui.combobox_model.setDisabled(False)
