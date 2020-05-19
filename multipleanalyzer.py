from run_nnet import MultiPredictor, ModelPredictorThread, ExportExcelThread
from callbacks_nnet import CallBackMultiPredictNNet
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFile, QTextStream, pyqtSignal, Qt, QMargins
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice, QLegend
from PyQt5.QtGui import QPainter, QPen, QFont, QColor
from utils_nnet import ModelCommon as Utils
import os
import sys
sys.path.append('gui/')
from gui.multipleanalyzer_ui import Ui_MultipleAnalayzer


class MultipleAnalyzerController(QMainWindow):
    # qt signals
    update_tweet_progress = pyqtSignal(int)
    update_batch_progress = pyqtSignal(int)

    def __init__(self, parent=None):
        super(MultipleAnalyzerController, self).__init__(parent)
        self.parent = parent
        self.main = QFrame()
        self.ui = Ui_MultipleAnalayzer()
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
        self.ui.btn_tweets_file.clicked.connect(self.open_file)
        self.ui.btn_start.clicked.connect(self.start_predict)
        self.ui.btn_stop.clicked.connect(self.stop_predict)
        self.ui.btn_save.clicked.connect(self.save_results)
        self.ui.btn_classify.clicked.connect(self.classify_tweets)
        self.ui.textbox_tweets_file.textChanged.connect(self.check_validation)
        self.ui.combobox_model.currentIndexChanged.connect(self.check_validation)

        # connect signals
        self.update_tweet_progress.connect(self.ui.progressbar_tweets.setValue)
        self.update_batch_progress.connect(self.ui.progressbar_batch.setValue)

    def _load_stylesheet(self):
        file = QFile('./css/MultipleAnalyzer.qss')
        file.open(QFile.ReadOnly)
        stream = QTextStream(file)
        text = stream.readAll()
        self.main.setStyleSheet(text)

    def _center_on_screen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.main.move((resolution.width() / 2) - (self.main.frameSize().width() / 2), 10)

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
            Utils.show_msg(text="Exporting Complete!", title="Input Error", msg_type=QMessageBox.Information)
        else:
            Utils.show_msg(text=self.export_thread.error, title="Error", msg_type=QMessageBox.Critical)

    def check_validation(self):
        model_index = self.ui.combobox_model.currentIndex()
        tweet_file = self.ui.textbox_tweets_file.text()

        if (len(tweet_file) > 0) and model_index > 0:
            self.ui.btn_start.setDisabled(False)
        else:
            self.ui.btn_start.setDisabled(True)

    def create_initialize_pieseries(self):
        color = QColor("#757a79")
        # define the series slices of the pie
        series = QPieSeries()
        none_slice = QPieSlice("Undefined", 1.0)
        none_slice.setColor(color)
        none_slice.setBorderColor(color)

        series.append(none_slice)
        series.setLabelsVisible(False)
        series.setLabelsPosition(QPieSlice.LabelOutside)
        series.setPieSize(1.0)

        return series

    def create_predict_pieseries(self, bots_part):
        human_part = 1 - bots_part
        percentage_bots_part = int(round(bots_part * 100))
        percentage_human_part = 100 - percentage_bots_part

        # define the series slices of the pie
        series = QPieSeries()
        bot_slice = QPieSlice(f"Bot ({percentage_bots_part}%)", bots_part)
        human_slice = QPieSlice(f"Human ({percentage_human_part}%)", human_part)

        font = QFont()
        font.setBold(True)

        bot_slice.setColor(QColor("#3498db"))
        bot_slice.setLabelFont(font)
        human_slice.setColor(QColor("#a8e6cf"))
        human_slice.setLabelFont(font)

        series.append(bot_slice)
        series.append(human_slice)
        series.setLabelsVisible(False)
        series.setLabelsPosition(QPieSlice.LabelInsideHorizontal)
        series.setPieSize(1.0)

        return series

    def create_piechart(self, series, animation=True):
        if animation:
            animation_type = QChart.AllAnimations
        else:
            animation_type = QChart.NoAnimation

        # define the chart properties
        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(animation_type)
        chart.setBackgroundVisible(False)
        chart.setMargins(QMargins())

        font = QFont()
        font.setBold(True)

        # define legend properties
        chart.legend().show()
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.legend().setFont(font)
        self.ui.piechart.setChart(chart)
        self.ui.piechart.setRenderHint(QPainter.Antialiasing)
        QApplication.processEvents()

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
        model_names = MultiPredictor.get_models_names()
        self.ui.combobox_model.addItems(model_names)

    def classify_tweets(self):
        threshold = self.ui.spinbox_threshold.value()
        self.predictor.classify_by_threshold(threshold=threshold)
        bots_part = self.predictor.get_bots_distribution()

        series = self.create_predict_pieseries(bots_part)
        self.create_piechart(series, animation=True)

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

        # reset piechart
        series = self.create_initialize_pieseries()
        self.create_piechart(series, animation=False)

        # reset progressbars
        self.ui.progressbar_batch.setValue(0)
        self.ui.progressbar_tweets.setValue(0)

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
        tweets_file = self.ui.textbox_tweets_file.text()
        header_included = self.ui.checkbox_header.isChecked()
        random_tweets = self.ui.spinbox_rand_tweets.value()

        # check for file validity
        try:
            Utils.file_validation(tweets_file, 'Tweet')
        except Exception as ex:
            Utils.show_msg(text=ex.args[0], title="Input Error")
            return

        # reset values of widgets
        self.reset_form()

        # disable all widgets
        self.disable_widgets(True)

        self.model_callback = CallBackMultiPredictNNet(self.update_batch_progress, self.update_tweet_progress,
                                                       random_tweets)

        self.predictor = MultiPredictor(model_name, self.model_callback, tweets_file, header_included, random_tweets)

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





