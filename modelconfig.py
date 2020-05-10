from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from utils_nnet import ModelCommon as Utils
import sys
import pyqtgraph as pg
sys.path.append('gui/')
from gui.modelconfig_ui import Ui_ModelConfig
from build_nnet import ModelTrainer, ModelTrainerThread
from dataset_parser import DatasetConfig
from logger import Log


class ModelConfigController(QMainWindow):
    def __init__(self, parent=None):
        super(ModelConfigController, self).__init__(parent)
        self.parent = parent
        self.main = QFrame()
        self.ui = Ui_ModelConfig()
        self.ui.setupUi(self.main)
        self._load_stylesheet()
        self._center_on_screen()

        # initialize graphs
        self._all_graphs_init()

        # create two lines for train and val for each epoch graphs
        # key-> train/val, value-> line
        self.acc_epoch_lines = self.create_train_val_lines(self.ui.graph_acc_epoch, legend_offset=(53, 30))
        self.loss_epoch_lines = self.create_train_val_lines(self.ui.graph_loss_epoch, legend_offset=(-3, 30))

        # create single line for each batch graphs
        self.acc_batch_line = self.create_line(self.ui.graph_acc_batch)
        self.loss_batch_line = self.create_line(self.ui.graph_loss_batch)

        self.stop_requested = False
        self.model = None
        self.model_thread = None
        self.log = None

        # initialize default paths
        self.ui.textbox_embed.setText('C:/Users/אור כהן/PycharmProjects/TwitterBotDetection/data/glove.twitter.27B.200d.txt')
        self.ui.textbox_bot.setText('C:/Users/אור כהן/PycharmProjects/TwitterBotDetection/data/bots_tweets.txt')
        self.ui.textbox_human.setText('C:/Users/אור כהן/PycharmProjects/TwitterBotDetection/data/human_tweets.txt')

        # connect listeners
        self.ui.btn_homepage.clicked.connect(self.back_homepage)
        self.ui.slider_train.valueChanged.connect(lambda: self.slider_changed(self.ui.slider_train, self.ui.lbl_train))
        self.ui.slider_val.valueChanged.connect(lambda: self.slider_changed(self.ui.slider_val, self.ui.lbl_val))
        self.ui.btn_embed.clicked.connect(lambda: self.open_file(self.ui.textbox_embed))
        self.ui.btn_bot.clicked.connect(lambda: self.open_file(self.ui.textbox_bot))
        self.ui.btn_human.clicked.connect(lambda: self.open_file(self.ui.textbox_human))
        self.ui.btn_start.clicked.connect(self.start_train)
        self.ui.btn_stop.clicked.connect(self.stop_train)
        self.ui.btn_save.clicked.connect(self.save_model)
        # TODO: add help

    def _load_stylesheet(self):
        file = QFile('./css/ModelConfig.qss')
        file.open(QFile.ReadOnly)
        stream = QTextStream(file)
        text = stream.readAll()
        self.main.setStyleSheet(text)

    def _center_on_screen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.main.move((resolution.width() / 2) - (self.main.frameSize().width() / 2), 0)

    def show(self):
        self.main.showMaximized()

    def back_homepage(self):
        self.parent.show()
        self.main.close()

    def is_stopped(self):
        return self.stop_requested

    def stop_train(self):
        self.log.write_log("Send request for stopping...")
        self.stop_requested = True;
        self.log.disable_log()

    def create_train_val_lines(self, graph, legend_offset):
        line_train = pg.PlotCurveItem(clear=True, pen=pg.mkPen('r', width=2))
        line_val = pg.PlotCurveItem(clear=True, pen=pg.mkPen('g', width=2))

        # initialize legends
        legend_acc = pg.LegendItem((70, 40), offset=legend_offset)
        legend_acc.setParentItem(graph.graphicsItem())

        legend_acc.addItem(line_train, "<b>train</b>")
        legend_acc.addItem(line_val, "<b>val</b>")

        graph.addItem(line_train)
        graph.addItem(line_val)

        dict_lines = { 'train': line_train, 'val': line_val }
        return dict_lines

    def create_line(self, graph):
        line = pg.PlotCurveItem(clear=True, pen=pg.mkPen((255,171,0), width=2))
        graph.addItem(line)
        return line

    def change_widgets_disabled(self, state):
        self.ui.btn_stop.setDisabled(not state)
        self.ui.btn_start.setDisabled(state)
        self.ui.groupbox_inputs.setDisabled(state)
        self.ui.groupbox_dataset.setDisabled(state)
        self.ui.groupbox_trainparams.setDisabled(state)

    def write_log(self, text):
        self.ui.textbox_log.append(text)
        self.ui.textbox_log.moveCursor(QTextCursor.End)

    def reset_graphs(self):
        self.plot_batch_acc([0], [0])
        self.plot_batch_loss([0], [0])
        self.plot_epoch_acc([0], [0], [0], [0])
        self.plot_epoch_loss([0], [0], [0], [0])

    def start_train(self):
        # get training parameters
        embedding_file = self.ui.textbox_embed.text()
        bot_file = self.ui.textbox_bot.text()
        human_file = self.ui.textbox_human.text()
        train_split = self.ui.slider_train.value() / 100.0
        test_split = 1 - train_split
        val_split = self.ui.slider_val.value() / 100.0
        epoches = self.ui.spinbox_epoches.value()
        batch_size = self.ui.spinbox_batch.value()
        addit_feat_enabled = self.ui.checkbox_additional_feats.isChecked()
        early_stop = self.ui.spinbox_earlystop.value()

        # get dataset config from combobox
        gen_method = str(self.ui.combobox_gen_method.currentText())
        if gen_method == "User Grouping":
            dataset_config = DatasetConfig.USER_STATE
        elif gen_method == "Random Pairing":
            dataset_config = DatasetConfig.RANDOM_STATE

        # Check for early stop validity
        if early_stop > epoches:
            Utils.show_error(text="Can not Insert Early Stop Epochs\nThat Bigger Than Training Epochs Number!",
                             title="Input Error")
            return

        # check for files validity
        try:
            Utils.file_validation(embedding_file, 'Embedding')
            Utils.file_validation(bot_file, 'Bot')
            Utils.file_validation(human_file, 'Human')
        except Exception as ex:
            Utils.show_error(text=ex.args[0], title="Input Error")
            return

        self.stop_requested = False;

        # set log method for writing to log textbox
        self.log = Log(self.write_log)

        # reset progressbars
        self.ui.progressbar_epoches.setValue(0)
        self.ui.progressbar_batch.setValue(0)

        # reset graphs
        self.reset_graphs()

        # disable unnecessery widgets when starting training
        self.change_widgets_disabled(True)
        self.ui.btn_save.setDisabled(True)

        self.log.write_log("Start pre-training phase...")

        # create model instance with all parameters
        self.model = ModelTrainer(logger=self.log, embedding_file=embedding_file, bots_file=bot_file,
                                  human_file=human_file, validation_split=val_split, test_split=test_split,
                                  batch_size=batch_size, epochs=epoches, additional_feats_enabled=addit_feat_enabled,
                                  early_stopping=early_stop, dataset_config=dataset_config, config_controller=self)

        # create a thread for training phase
        self.model_thread = ModelTrainerThread(self.model)
        self.model_thread.start() # run the thread to start training

    def save_model(self):
        model_name, _ = QFileDialog.getSaveFileName(self, 'Save Model File', "./output/model_name")
        if model_name:
            self.model.save_model(model_name)

    def slider_changed(self, slider_obj, lbl_obj):
        val = slider_obj.value()
        lbl_obj.setText(f'{val}%')

    def open_file(self, text_box):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "Please select a file", "./data/", "*.*")
            if file_path:
                text_box.setText(file_path)

        except IOError as e:
            pass

    def _all_graphs_init(self):
        pg.setConfigOption("antialias", True)
        self._graph_init(self.ui.graph_acc_epoch, '<b>Accuracy Epoch</b>', 'Epoch Number<', 'Accuracy')
        self._graph_init(self.ui.graph_acc_batch, '<b>Accuracy Batch</b>', 'Batch Number', 'Accuracy')
        self._graph_init(self.ui.graph_loss_epoch, '<b>Loss Epoch</b>', 'Epoch Number', 'Loss Value')
        self._graph_init( self.ui.graph_loss_batch, '<b>Loss Batch</b>', 'Batch Number', 'Loss Value')

    def _graph_init(self, graph, title, bottom_label, left_label):
        graph.setTitle(title)
        graph.setLabel('bottom', bottom_label, units='times')
        graph.setLabel('left', left_label, units='%')
        graph.showGrid(x=True, y=True)
        graph.getAxis('bottom').enableAutoSIPrefix(False)
        graph.getAxis('left').enableAutoSIPrefix(False)

    def plot_epoch_acc(self, x_train, y_train, x_val, y_val):
        self.acc_epoch_lines['train'].setData(x_train, y_train)
        self.acc_epoch_lines['val'].setData(x_val, y_val)
        QApplication.processEvents()

    def plot_epoch_loss(self, x_train, y_train, x_val, y_val):
        self.loss_epoch_lines['train'].setData(x_train, y_train)
        self.loss_epoch_lines['val'].setData(x_val, y_val)
        QApplication.processEvents()

    def plot_batch_acc(self, x, y):
        self.acc_batch_line.setData(x, y)
        QApplication.processEvents()

    def plot_batch_loss(self, x, y):
        self.loss_batch_line.setData(x, y)
        QApplication.processEvents()
