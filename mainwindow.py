from modelconfig import ModelConfigController
from singleanalyzer import SingleAnalyzerController
from multipleanalyzer import MultipleAnalyzerController
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFile, QTextStream
import ctypes
import sys
sys.path.append('gui/')
from gui.mainwindow_ui import Ui_MainMenu


class MainWindowController(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindowController, self).__init__(parent)
        self.main = QFrame()
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self.main)
        self._load_stylesheet()

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('FinalProject.TweetBotDetector')

        # connect listeners
        self.ui.btn_config.clicked.connect(self.open_model_config_gui)
        self.ui.btn_single.clicked.connect(self.open_single_analyzer_gui)
        self.ui.btn_multi.clicked.connect(self.open_multiple_analyzer_gui)
        #TODO: update the final date on label

    def _load_stylesheet(self):
        file = QFile('./css/MainWindow.qss')
        file.open(QFile.ReadOnly)
        stream = QTextStream(file)
        text = stream.readAll()
        self.main.setStyleSheet(text)

    def show(self):
        self.main.show()

    def open_model_config_gui(self):
        model_config = ModelConfigController(self)
        model_config.show()
        self.main.close()

    def open_single_analyzer_gui(self):
        single_analyzer = SingleAnalyzerController(self)
        single_analyzer.show()
        self.main.close()

    def open_multiple_analyzer_gui(self):
        multi_analyzer = MultipleAnalyzerController(self)
        multi_analyzer.show()
        self.main.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindowController()
    main.show()
    sys.exit(app.exec_())