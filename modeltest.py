from run_nnet import ModelTestPredictor, ModelPredictorThread, ExportExcelThread
from callbacks_nnet import CallBackMultiPredictNNet
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFile, QTextStream, pyqtSignal, Qt, QMargins
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice, QLegend
from PyQt5.QtChart import QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.QtGui import QPainter, QPen, QFont, QColor
from utils_nnet import ModelCommon as Utils
import os
import sys
sys.path.append('gui/')
from gui.modeltest_ui import Ui_ModelTest


class ModelTestController(QMainWindow):
    # qt signals
    update_tweet_progress = pyqtSignal(int)
    update_batch_progress = pyqtSignal(int)

    def __init__(self, parent=None):
        super(ModelTestController, self).__init__(parent)
        self.parent = parent
        self.main = QFrame()
        self.ui = Ui_ModelTest()
        self.ui.setupUi(self.main)
        self._load_stylesheet()
        self._center_on_screen()
        self.load_models_names()

        # initialize form
        self.reset_form()

        self.model_callback = None
        self.predictor = None
        self.pred_thread = None
        self.export_thread = None

        # connect listeners
        self.ui.btn_homepage.clicked.connect(self.back_homepage)
        self.ui.btn_bot_file.clicked.connect(lambda: self.open_file(self.ui.textbox_bot_file.setText))
        self.ui.btn_human_file.clicked.connect(lambda: self.open_file(self.ui.textbox_human_file.setText))
        self.ui.btn_start.clicked.connect(self.start_predict)
        self.ui.btn_stop.clicked.connect(self.stop_predict)
        self.ui.btn_save.clicked.connect(self.save_results)
        self.ui.btn_classify.clicked.connect(self.classify_tweets)
        self.ui.textbox_bot_file.textChanged.connect(self.check_validation)
        self.ui.textbox_human_file.textChanged.connect(self.check_validation)
        self.ui.combobox_model.currentIndexChanged.connect(self.check_validation)
        self.ui.btn_help.clicked.connect(Utils.open_help_file)

        # connect signals
        self.update_tweet_progress.connect(self.ui.progressbar_tweets.setValue)
        self.update_batch_progress.connect(self.ui.progressbar_batch.setValue)

    def _load_stylesheet(self):
        file = QFile('./css/ModelTest.qss')
        file.open(QFile.ReadOnly)
        stream = QTextStream(file)
        text = stream.readAll()
        self.main.setStyleSheet(text)

    def _center_on_screen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.main.move((resolution.width() / 2) - (self.main.frameSize().width() / 2), 5)

    def save_results(self):
        threshold = self.ui.spinbox_threshold.value()
        filter = "Excel file (*.xlsx)"
        excel_file, _ = QFileDialog.getSaveFileName(self, 'Save Excel File', "./output/predict_results.xlsx", filter)
        if excel_file:
            self.export_thread = ExportExcelThread(self.predictor, threshold, excel_file)
            self.export_thread.finished.connect(self.export_finished)
            self.export_thread.start()

    def export_finished(self):
        if self.export_thread.is_success():
            Utils.show_msg(text="Exporting Complete!", title="Successful", msg_type=QMessageBox.Information)
            os.startfile(self.export_thread.excel_path)
        else:
            Utils.show_msg(text=self.export_thread.error, title="Error", msg_type=QMessageBox.Critical)

    def check_validation(self):
        model_index = self.ui.combobox_model.currentIndex()
        bot_file = self.ui.textbox_bot_file.text()
        human_file = self.ui.textbox_human_file.text()

        if (len(bot_file) > 0) and (len(human_file) > 0) and model_index > 0:
            self.ui.btn_start.setDisabled(False)
        else:
            self.ui.btn_start.setDisabled(True)

    def _create_series_barchart(self, correct_bot, correct_human, incorrect_bot, incorrect_human):
        correct_set = QBarSet('Correct Prediction')
        correct_set.append([correct_human, correct_bot])
        correct_set.setColor(QColor("#29ec1e"))

        incorrect_set = QBarSet('Incorrect Prediction')
        incorrect_set.append([incorrect_human, incorrect_bot])
        incorrect_set.setColor(QColor("#ED213A"))

        series = QBarSeries()
        series.append(correct_set)
        series.append(incorrect_set)
        return series

    def create_initialize_barchart(self):
        series = self._create_series_barchart(0, 0, 0, 0)
        max_val = 100
        return series, max_val

    def create_predict_barchart(self):
        correct_bot_score, correct_human_score = self.predictor.get_accuracy_bot_human()

        correct_bot_percentage = int(round(correct_bot_score * 100))
        correct_human_percentage = int(round(correct_human_score * 100))

        incorrect_bot_percentage = 100 - correct_bot_percentage
        incorrect_human_percentage = 100 - correct_human_percentage

        scores_arr = [correct_bot_percentage, correct_human_percentage,
                      incorrect_bot_percentage, incorrect_human_percentage]

        series = self._create_series_barchart(*scores_arr)
        max_val = max(scores_arr)

        return series, max_val

    def create_barchart(self, series, max_val, animation=True):
        if animation:
            animation_type = QChart.AllAnimations
        else:
            animation_type = QChart.NoAnimation

        chart = QChart()
        chart.addSeries(series)
        chart.setBackgroundVisible(False)
        chart.setMargins(QMargins())
        chart.setAnimationOptions(animation_type)

        labels = ('Human', 'Bot')

        axisX = QBarCategoryAxis()
        axisX.append(labels)

        axisY = QValueAxis()
        axisY.setTitleText("Percentage (%)")
        axisY.setRange(0, max_val)

        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)

        font = QFont()
        font.setPointSize(9)

        chart.legend().setVisible(True)
        chart.legend().setFont(font)
        chart.legend().setAlignment(Qt.AlignBottom)

        self.ui.barchart.setChart(chart)
        self.ui.barchart.setRenderHint(QPainter.Antialiasing)

    def open_file(self, update_textbox_method):
        try:
            filter = "Text files (*.txt)"
            file_path, _ = QFileDialog.getOpenFileName(self, "Please select a file", "./data/", filter)
            if file_path:
                update_textbox_method(file_path)

        except IOError as e:
            pass

    def show(self):
        self.main.show()

    def back_homepage(self):
        self.parent.show()
        self.main.close()

    def load_models_names(self):
        model_names = ModelTestPredictor.get_models_names()
        self.ui.combobox_model.addItems(model_names)

    def classify_tweets(self):
        threshold = self.ui.spinbox_threshold.value()
        self.predictor.classify_by_threshold(threshold=threshold)

        # update barchart chart prediction
        bar_series, max_val = self.create_predict_barchart()
        self.create_barchart(bar_series, max_val, animation=True)

        # write final accuracy of model
        correct_model_score = self.predictor.get_accuracy_model()
        correct_model_percentage = int(round(correct_model_score * 100))
        self.ui.lbl_acc.setText(f'Model Accuracy: {correct_model_percentage}%')

    def disable_widgets(self, state):
        self.ui.btn_start.setDisabled(state)
        self.ui.btn_save.setDisabled(state)
        self.ui.btn_stop.setDisabled(not state)
        self.ui.combobox_model.setDisabled(state)
        self.ui.groupbox_threshold.setDisabled(state)
        self.ui.btn_classify.setDisabled(state)
        self.ui.groupbox_config.setDisabled(state)

    def reset_form(self):
        self.need_stop = False

        # reset barchart
        bar_series, max_val = self.create_initialize_barchart()
        self.create_barchart(bar_series, max_val, animation=False)

        # reset progressbars
        self.ui.progressbar_batch.setValue(0)
        self.ui.progressbar_tweets.setValue(0)

        # reset model accuracy
        self.ui.lbl_acc.setText(f'Model Accuracy: 0%')

    def stop_predict(self):
        if self.pred_thread is not None:
            if self.pred_thread.isRunning():
                self.need_stop = True
                if not self.model_callback.predict_start:
                    self.pred_thread.terminate()
                else:
                    self.predictor.need_stop()

    def start_predict(self):
        # get predicting parameters
        model_name = str(self.ui.combobox_model.currentText())
        bot_file = self.ui.textbox_bot_file.text()
        human_file = self.ui.textbox_human_file.text()
        bot_tweets = self.ui.spinbox_bot_tweets.value()
        human_tweets = self.ui.spinbox_human_tweets.value()
        total_tweets = bot_tweets + human_tweets

        # check for file validity
        try:
            Utils.file_validation(bot_file, 'Tweet')
            Utils.file_validation(human_file, 'Tweet')
        except Exception as ex:
            Utils.show_msg(text=ex.args[0], title="Input Error")
            return

        # reset values of widgets
        self.reset_form()

        # disable all widgets
        self.disable_widgets(True)

        self.model_callback = CallBackMultiPredictNNet(self.update_batch_progress, self.update_tweet_progress,
                                                       total_tweets)

        self.predictor = ModelTestPredictor(model_name, self.model_callback, bot_file, human_file,
                                            bot_tweets, human_tweets)

        # create a thread for predictor
        self.pred_thread = ModelPredictorThread(self.predictor)
        self.pred_thread.finished.connect(self.on_predict_finished)
        self.pred_thread.start()

    def on_predict_finished(self):
        self.disable_widgets(False)

        if not self.need_stop:
            if self.pred_thread.is_success():
                self.classify_tweets()
            else:
                Utils.show_msg(text=self.pred_thread.error, title="Error")
                self.ui.btn_save.setDisabled(True)
                self.ui.groupbox_threshold.setDisabled(True)
        else:
            self.reset_form()
            self.ui.btn_save.setDisabled(True)
            self.ui.groupbox_threshold.setDisabled(True)



