from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import pyqtgraph as pg
sys.path.append('gui/')
from gui.modelconfig_ui import Ui_ModelConfig

## Switch to using white background and black foreground
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')


class ModelConfigController(QMainWindow):
    def __init__(self, parent=None):
        super(ModelConfigController, self).__init__(parent)
        self.parent = parent
        self.main = QFrame()
        self.ui = Ui_ModelConfig()
        self.ui.setupUi(self.main)
        self._load_stylesheet()
        self._center_on_screen()

        # connect listeners
        self.ui.btn_homepage.clicked.connect(self.back_homepage)

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
        self.main.show()

    def back_homepage(self):
        self.parent.show()
        self.main.close()