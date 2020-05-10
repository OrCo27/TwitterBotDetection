# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SingleAnalyzer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SingleAnalyzer(object):
    def setupUi(self, SingleAnalyzer):
        SingleAnalyzer.setObjectName("SingleAnalyzer")
        SingleAnalyzer.resize(568, 563)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SingleAnalyzer.setWindowIcon(icon)
        SingleAnalyzer.setStyleSheet("#lbl_title {\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"qproperty-alignment: AlignCenter;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3643f7, stop:1 #3643f7);\n"
"}\n"
"\n"
"#lbl_result {\n"
"font: 75 15pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"qproperty-alignment: AlignCenter;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #48CFAD, stop:1 #37BC9B);\n"
"}\n"
"\n"
"#btn_homepage {\n"
"background: transparent;\n"
"border-radius: 19px;\n"
"}\n"
"\n"
"#btn_homepage::hover {\n"
"background: #3f72af;\n"
"}\n"
"\n"
"#btn_help {\n"
"background: transparent;\n"
"border-radius: 19px;\n"
"}\n"
"\n"
"#btn_help::hover {\n"
"background: #3f72af;\n"
"}\n"
"\n"
"#btn_start {\n"
"font: 75 13pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar:horizontal {\n"
"border: 1px solid gray;\n"
"border-radius: 3px;\n"
"background: white;\n"
"padding: 0px;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #a8ff78, stop: 1 #78ffd6);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(SingleAnalyzer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn_homepage = QtWidgets.QToolButton(SingleAnalyzer)
        self.btn_homepage.setAutoFillBackground(False)
        self.btn_homepage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/homepage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_homepage.setIcon(icon1)
        self.btn_homepage.setIconSize(QtCore.QSize(35, 35))
        self.btn_homepage.setObjectName("btn_homepage")
        self.horizontalLayout_11.addWidget(self.btn_homepage)
        self.btn_help = QtWidgets.QToolButton(SingleAnalyzer)
        self.btn_help.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_help.setIcon(icon2)
        self.btn_help.setIconSize(QtCore.QSize(35, 35))
        self.btn_help.setObjectName("btn_help")
        self.horizontalLayout_11.addWidget(self.btn_help)
        self.lbl_title = QtWidgets.QLabel(SingleAnalyzer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title.sizePolicy().hasHeightForWidth())
        self.lbl_title.setSizePolicy(sizePolicy)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.horizontalLayout_11.addWidget(self.lbl_title)
        spacerItem = QtWidgets.QSpacerItem(86, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalFrame = QtWidgets.QFrame(SingleAnalyzer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMinimumSize(QtCore.QSize(500, 0))
        self.verticalFrame.setMaximumSize(QtCore.QSize(800, 16777215))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.combobox_model = QtWidgets.QComboBox(self.verticalFrame)
        self.combobox_model.setObjectName("combobox_model")
        self.verticalLayout_2.addWidget(self.combobox_model)
        self.horizontalLayout.addWidget(self.verticalFrame)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalFrame1 = QtWidgets.QFrame(SingleAnalyzer)
        self.verticalFrame1.setMinimumSize(QtCore.QSize(500, 0))
        self.verticalFrame1.setMaximumSize(QtCore.QSize(800, 16777215))
        self.verticalFrame1.setObjectName("verticalFrame1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_3.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textbox_tweet = QtWidgets.QTextEdit(self.verticalFrame1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbox_tweet.sizePolicy().hasHeightForWidth())
        self.textbox_tweet.setSizePolicy(sizePolicy)
        self.textbox_tweet.setMaximumSize(QtCore.QSize(16777215, 300))
        self.textbox_tweet.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textbox_tweet.setObjectName("textbox_tweet")
        self.verticalLayout_3.addWidget(self.textbox_tweet)
        self.horizontalLayout_2.addWidget(self.verticalFrame1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_start = QtWidgets.QPushButton(SingleAnalyzer)
        self.btn_start.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QtCore.QSize(122, 35))
        self.btn_start.setMaximumSize(QtCore.QSize(16777215, 35))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/run.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_start.setIcon(icon3)
        self.btn_start.setIconSize(QtCore.QSize(30, 30))
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_3.addWidget(self.btn_start)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(120, 4, 120, 4)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.progressbar_batch = QtWidgets.QProgressBar(SingleAnalyzer)
        self.progressbar_batch.setMinimumSize(QtCore.QSize(0, 17))
        self.progressbar_batch.setMaximumSize(QtCore.QSize(16777215, 17))
        self.progressbar_batch.setProperty("value", 0)
        self.progressbar_batch.setAlignment(QtCore.Qt.AlignCenter)
        self.progressbar_batch.setObjectName("progressbar_batch")
        self.horizontalLayout_5.addWidget(self.progressbar_batch)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalGroupBox_5 = QtWidgets.QGroupBox(SingleAnalyzer)
        self.horizontalGroupBox_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalGroupBox_5.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox_5.setSizePolicy(sizePolicy)
        self.horizontalGroupBox_5.setMinimumSize(QtCore.QSize(550, 0))
        self.horizontalGroupBox_5.setMaximumSize(QtCore.QSize(550, 16777215))
        self.horizontalGroupBox_5.setObjectName("horizontalGroupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_5)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.horizontalGroupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(200, 0))
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setStyleSheet("image: url(:/images/icon.png);")
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lbl_result = QtWidgets.QLabel(self.horizontalGroupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_result.sizePolicy().hasHeightForWidth())
        self.lbl_result.setSizePolicy(sizePolicy)
        self.lbl_result.setWordWrap(True)
        self.lbl_result.setObjectName("lbl_result")
        self.horizontalLayout_4.addWidget(self.lbl_result)
        spacerItem6 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.horizontalGroupBox_5)

        self.retranslateUi(SingleAnalyzer)
        QtCore.QMetaObject.connectSlotsByName(SingleAnalyzer)

    def retranslateUi(self, SingleAnalyzer):
        _translate = QtCore.QCoreApplication.translate
        SingleAnalyzer.setWindowTitle(_translate("SingleAnalyzer", "Single Tweet Analyzer"))
        self.btn_homepage.setToolTip(_translate("SingleAnalyzer", "Back To HomePage"))
        self.btn_help.setToolTip(_translate("SingleAnalyzer", "Open Help Documentation"))
        self.lbl_title.setText(_translate("SingleAnalyzer", "Single Tweet Analyzer"))
        self.label.setText(_translate("SingleAnalyzer", "Select Model:"))
        self.textbox_tweet.setPlaceholderText(_translate("SingleAnalyzer", "Enter a Tweet Content"))
        self.btn_start.setText(_translate("SingleAnalyzer", "Predict"))
        self.horizontalGroupBox_5.setTitle(_translate("SingleAnalyzer", "Result"))
        self.lbl_result.setText(_translate("SingleAnalyzer", "The Tweet is a Bot With Probability of 0%"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SingleAnalyzer = QtWidgets.QWidget()
    ui = Ui_SingleAnalyzer()
    ui.setupUi(SingleAnalyzer)
    SingleAnalyzer.show()
    sys.exit(app.exec_())

