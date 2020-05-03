from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from pyqtgraph import PlotWidget, plot
import sys
import pyqtgraph as pg
sys.path.append('gui/')
from gui.modelconfig_ui import Ui_ModelConfig
import random

class ModelConfigController(QMainWindow):
    def __init__(self, parent=None):
        super(ModelConfigController, self).__init__(parent)
        self.parent = parent
        self.main = QFrame()
        self.ui = Ui_ModelConfig()
        self.ui.setupUi(self.main)
        self._load_stylesheet()
        self._center_on_screen()
        self.graphs = {
            "ACC_EPOCH": self.ui.graph_acc_epoch,
            "LOSS_EPOCH": self.ui.graph_loss_epoch,
            "ACC_BATCH": self.ui.graph_acc_batch,
            "LOSS_BATCH": self.ui.graph_loss_batch
        }

        # initialize default paths
        self.ui.textbox_embed.setText('data/glove.twitter.27B.200d.txt')
        self.ui.textbox_bot.setText('data/bots_tweets.txt')
        self.ui.textbox_human.setText('data/human_tweets.txt')

        # initialize legends
        self.legend_acc = pg.LegendItem((70, 40), offset=(62, 30))
        self.legend_acc.setParentItem(self.graphs["ACC_EPOCH"].graphicsItem())
        self.legend_loss = pg.LegendItem((70, 40), offset=(-30, 30))
        self.legend_loss.setParentItem(self.graphs["LOSS_EPOCH"].graphicsItem())

        # initialize graphs
        self._all_graphs_init()

        self.plot_two_lines(self.graphs["ACC_EPOCH"], self.legend_acc,
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [50,55,60,65,70,75,80,83,85,89],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [45,52,57,60,65,70,78,80,82,95])

        self.plot_two_lines(self.graphs["LOSS_EPOCH"], self.legend_loss,
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [70,60,55,44,40,38,36,32,30,25],
                            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [72,63,58,48,43,40,39,30,27,22])

        self.plot_one_line(self.graphs["ACC_BATCH"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], random.sample(range(20, 100), 10))
        self.plot_one_line(self.graphs["LOSS_BATCH"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], random.sample(range(20, 100), 10))

        # connect listeners
        self.ui.btn_homepage.clicked.connect(self.back_homepage)
        self.ui.slider_train.valueChanged.connect(lambda: self.slider_changed(self.ui.slider_train, self.ui.lbl_train))
        self.ui.slider_val.valueChanged.connect(lambda: self.slider_changed(self.ui.slider_val, self.ui.lbl_val))
        self.ui.btn_embed.clicked.connect(lambda: self.open_file(self.ui.textbox_embed))
        self.ui.btn_bot.clicked.connect(lambda: self.open_file(self.ui.textbox_bot))
        self.ui.btn_human.clicked.connect(lambda: self.open_file(self.ui.textbox_human))

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

    def slider_changed(self, slider_obj, lbl_obj):
        val = slider_obj.value()
        lbl_obj.setText(f'{val}%')

    def open_file(self, text_box):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "Please select a file", "", "*.*")
            if file_path:
                text_box.setText(file_path)

        except IOError as e:
            pass

    def _all_graphs_init(self):
        self._graph_init(self.graphs["ACC_EPOCH"], '<b>Accuracy Epoch</b>', 'Epoch Number<', 'Accuracy')
        self._graph_init(self.graphs["ACC_BATCH"], '<b>Accuracy Batch</b>', 'Batch Number', 'Accuracy')
        self._graph_init(self.graphs["LOSS_EPOCH"], '<b>Loss Epoch</b>', 'Epoch Number', 'Loss Value')
        self._graph_init(self.graphs["LOSS_BATCH"], '<b>Loss Batch</b>', 'Batch Number', 'Loss Value')

    def _graph_init(self, graph, title, bottom_label, left_label):
        graph.setTitle(title)
        graph.setLabel('bottom', bottom_label, units='times')
        graph.setLabel('left', left_label, units='%')
        graph.showGrid(x=True, y=True)
        graph.getAxis('bottom').enableAutoSIPrefix(False)
        graph.getAxis('left').enableAutoSIPrefix(False)

    def plot_two_lines(self, graph, legend, x_train, y_train, x_val, y_val):
        graph.clear()

        legend_train = "<b>train</b>"
        legend_val = "<b>val</b>"
        c1 = self._plot(graph, x_train, y_train, color='r', legend=legend_train)
        c2 = self._plot(graph, x_val, y_val, color='g', legend=legend_val)

        legend.addItem(c1, legend_train)
        legend.addItem(c2, legend_val)

    def plot_one_line(self, graph, x, y):
        graph.clear()
        self._plot(graph, x, y, color=(255,171,0))

    def _plot(self, graph, x, y, color, legend=None):
        return graph.plot(x, y, pen=pg.mkPen(color, width=2), name=legend)