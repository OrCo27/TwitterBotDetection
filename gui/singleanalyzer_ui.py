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
        SingleAnalyzer.setEnabled(True)
        SingleAnalyzer.resize(613, 562)
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
"#lbl_model {\n"
"font: 75 11pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: black;\n"
"padding-left: 1px\n"
"}\n"
"\n"
"QComboBox {\n"
"font: 75 10.5pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: #1F1F21;\n"
" border: 1px solid gray;\n"
" border-radius: 10px;\n"
" min-width: 6em;\n"
"padding-left: 8px;\n"
"qproperty-alignment: AlignCenter;\n"
"}\n"
"QComboBox::hover {\n"
" border: 1px solid blue;\n"
"background: #f0f5f9;\n"
"}\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}\n"
"QComboBox:on {\n"
"    borde-radius: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 10px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    border-radius: 10px;\n"
"    background: white;\n"
"    border: 1px solid gray;\n"
"    box-shadow: transparent;\n"
"    selection-background-color:lightblue;\n"
"    color: #1F1F21;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"image: url(:/images/arrow_down.png);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"padding-right: 1px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"border: 1px solid; \n"
"border-radius:10px;\n"
"background-color: palette(base);\n"
"font: 75 14pt \"Georgia, serif\";\n"
"font-weight: bold;\n"
"color: #3f72af;\n"
" min-width: 6em;\n"
"}\n"
"\n"
"QTextEdit::disabled {\n"
"background-color: #D3D3D3;\n"
"}\n"
"\n"
"#progressbar_batch::disabled {\n"
"background-color: #D3D3D3;\n"
"}\n"
"#lbl_result {\n"
"font: 75 18pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"qproperty-alignment: AlignCenter;\n"
"color: #3f72af;\n"
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
"QPushButton {\n"
"font: 75 13pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"border: 1px solid; \n"
"border-radius:10px;\n"
"background-color: #f0f5f9;\n"
"}\n"
"QPushButton::disabled {\n"
"background-color: #D3D3D3;\n"
"}\n"
"QPushButton::hover {\n"
"background: #c9d6df;\n"
"}\n"
"QPushButton:pressed {\n"
"background: #3f72af;\n"
"}\n"
"QProgressBar:horizontal {\n"
"border: 1px solid gray;\n"
"border-radius: 3px;\n"
"background: white;\n"
"padding: 0px;\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #a8ff78, stop: 1 #78ffd6);\n"
"}\n"
"\n"
"QProgressBar:vertical {\n"
"border: 1px solid gray;\n"
"border-radius: 3px;\n"
"background: white;\n"
"padding: 0px;\n"
"}\n"
"QProgressBar::chunk:vertical {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #a8ff78, stop: 1 #78ffd6);\n"
"}\n"
"\n"
"QProgressBar::chunk:vertical::disabled {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #ED213A, stop: 1 #93291E);\n"
"}\n"
"\n"
"QGroupBox {\n"
"font: 75 13pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: #3f72af;\n"
"}\n"
"\n"
"#lbl_human_result, #lbl_bot_result {\n"
"font: 75 13pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: green;\n"
"}\n"
"\n"
"#lbl_human_result, #lbl_bot_result::disabled {\n"
"color: red;\n"
"}\n"
"\n"
"#pic_human {\n"
"image: url(:/images/human.png);\n"
"}\n"
"\n"
"#pic_bot {\n"
"image: url(:/images/bot.png);\n"
"}\n"
"\n"
"\n"
"")
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
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(60, 19, 60, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.combobox_model = QtWidgets.QComboBox(SingleAnalyzer)
        self.combobox_model.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_model.sizePolicy().hasHeightForWidth())
        self.combobox_model.setSizePolicy(sizePolicy)
        self.combobox_model.setMinimumSize(QtCore.QSize(124, 0))
        self.combobox_model.setMaximumSize(QtCore.QSize(270, 16777215))
        self.combobox_model.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.combobox_model.setMinimumContentsLength(150)
        self.combobox_model.setObjectName("combobox_model")
        self.combobox_model.addItem("")
        self.horizontalLayout.addWidget(self.combobox_model)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 8, -1, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(SingleAnalyzer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(25, 25))
        self.label_2.setMaximumSize(QtCore.QSize(25, 25))
        self.label_2.setStyleSheet("image: url(:/images/open_quotes.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.textbox_tweet = QtWidgets.QTextEdit(SingleAnalyzer)
        self.textbox_tweet.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbox_tweet.sizePolicy().hasHeightForWidth())
        self.textbox_tweet.setSizePolicy(sizePolicy)
        self.textbox_tweet.setMinimumSize(QtCore.QSize(140, 150))
        self.textbox_tweet.setMaximumSize(QtCore.QSize(500, 150))
        self.textbox_tweet.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textbox_tweet.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textbox_tweet.setAcceptRichText(False)
        self.textbox_tweet.setObjectName("textbox_tweet")
        self.horizontalLayout_6.addWidget(self.textbox_tweet)
        self.label_3 = QtWidgets.QLabel(SingleAnalyzer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(25, 25))
        self.label_3.setMaximumSize(QtCore.QSize(25, 25))
        self.label_3.setStyleSheet("image: url(:/images/close_quotes.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.progressbar_batch = QtWidgets.QProgressBar(SingleAnalyzer)
        self.progressbar_batch.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressbar_batch.sizePolicy().hasHeightForWidth())
        self.progressbar_batch.setSizePolicy(sizePolicy)
        self.progressbar_batch.setMinimumSize(QtCore.QSize(200, 17))
        self.progressbar_batch.setMaximumSize(QtCore.QSize(500, 17))
        self.progressbar_batch.setProperty("value", 0)
        self.progressbar_batch.setAlignment(QtCore.Qt.AlignCenter)
        self.progressbar_batch.setObjectName("progressbar_batch")
        self.horizontalLayout_4.addWidget(self.progressbar_batch)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_start = QtWidgets.QPushButton(SingleAnalyzer)
        self.btn_start.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QtCore.QSize(122, 40))
        self.btn_start.setMaximumSize(QtCore.QSize(16777215, 40))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/predict.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_start.setIcon(icon3)
        self.btn_start.setIconSize(QtCore.QSize(35, 35))
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_3.addWidget(self.btn_start)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_8)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalFrame_2 = QtWidgets.QFrame(SingleAnalyzer)
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.groupbox_human = QtWidgets.QGroupBox(self.horizontalFrame_2)
        self.groupbox_human.setEnabled(False)
        self.groupbox_human.setAlignment(QtCore.Qt.AlignCenter)
        self.groupbox_human.setObjectName("groupbox_human")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupbox_human)
        self.verticalLayout_2.setContentsMargins(25, 10, 25, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(40, 0, 40, -1)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pic_human = QtWidgets.QLabel(self.groupbox_human)
        self.pic_human.setMinimumSize(QtCore.QSize(100, 100))
        self.pic_human.setMaximumSize(QtCore.QSize(100, 100))
        self.pic_human.setStyleSheet("")
        self.pic_human.setText("")
        self.pic_human.setAlignment(QtCore.Qt.AlignCenter)
        self.pic_human.setObjectName("pic_human")
        self.verticalLayout_4.addWidget(self.pic_human)
        self.lbl_human_result = QtWidgets.QLabel(self.groupbox_human)
        self.lbl_human_result.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_human_result.setObjectName("lbl_human_result")
        self.verticalLayout_4.addWidget(self.lbl_human_result)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.progressbar_human = QtWidgets.QProgressBar(self.groupbox_human)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressbar_human.sizePolicy().hasHeightForWidth())
        self.progressbar_human.setSizePolicy(sizePolicy)
        self.progressbar_human.setMinimumSize(QtCore.QSize(13, 100))
        self.progressbar_human.setMaximumSize(QtCore.QSize(13, 100))
        self.progressbar_human.setMaximum(100)
        self.progressbar_human.setProperty("value", 0)
        self.progressbar_human.setAlignment(QtCore.Qt.AlignCenter)
        self.progressbar_human.setTextVisible(False)
        self.progressbar_human.setOrientation(QtCore.Qt.Vertical)
        self.progressbar_human.setFormat("")
        self.progressbar_human.setObjectName("progressbar_human")
        self.verticalLayout_5.addWidget(self.progressbar_human)
        self.label = QtWidgets.QLabel(self.groupbox_human)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addWidget(self.groupbox_human)
        self.groupbox_bot = QtWidgets.QGroupBox(self.horizontalFrame_2)
        self.groupbox_bot.setEnabled(False)
        self.groupbox_bot.setAlignment(QtCore.Qt.AlignCenter)
        self.groupbox_bot.setObjectName("groupbox_bot")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupbox_bot)
        self.verticalLayout_3.setContentsMargins(25, 10, 25, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(40, 0, 40, -1)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pic_bot = QtWidgets.QLabel(self.groupbox_bot)
        self.pic_bot.setMinimumSize(QtCore.QSize(100, 100))
        self.pic_bot.setMaximumSize(QtCore.QSize(100, 100))
        self.pic_bot.setStyleSheet("")
        self.pic_bot.setText("")
        self.pic_bot.setObjectName("pic_bot")
        self.verticalLayout_6.addWidget(self.pic_bot, 0, QtCore.Qt.AlignHCenter)
        self.lbl_bot_result = QtWidgets.QLabel(self.groupbox_bot)
        self.lbl_bot_result.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_bot_result.setObjectName("lbl_bot_result")
        self.verticalLayout_6.addWidget(self.lbl_bot_result)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.progressbar_bot = QtWidgets.QProgressBar(self.groupbox_bot)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressbar_bot.sizePolicy().hasHeightForWidth())
        self.progressbar_bot.setSizePolicy(sizePolicy)
        self.progressbar_bot.setMinimumSize(QtCore.QSize(13, 100))
        self.progressbar_bot.setMaximumSize(QtCore.QSize(13, 100))
        self.progressbar_bot.setProperty("value", 0)
        self.progressbar_bot.setAlignment(QtCore.Qt.AlignCenter)
        self.progressbar_bot.setTextVisible(False)
        self.progressbar_bot.setOrientation(QtCore.Qt.Vertical)
        self.progressbar_bot.setFormat("")
        self.progressbar_bot.setObjectName("progressbar_bot")
        self.verticalLayout_7.addWidget(self.progressbar_bot)
        self.label_5 = QtWidgets.QLabel(self.groupbox_bot)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2.addWidget(self.groupbox_bot)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.horizontalFrame_2)

        self.retranslateUi(SingleAnalyzer)
        QtCore.QMetaObject.connectSlotsByName(SingleAnalyzer)

    def retranslateUi(self, SingleAnalyzer):
        _translate = QtCore.QCoreApplication.translate
        SingleAnalyzer.setWindowTitle(_translate("SingleAnalyzer", "Single Tweet Analyzer"))
        self.btn_homepage.setToolTip(_translate("SingleAnalyzer", "Back To HomePage"))
        self.btn_help.setToolTip(_translate("SingleAnalyzer", "Open Help Documentation"))
        self.lbl_title.setText(_translate("SingleAnalyzer", "Single Tweet Analyzer"))
        self.combobox_model.setCurrentText(_translate("SingleAnalyzer", "Select Model"))
        self.combobox_model.setItemText(0, _translate("SingleAnalyzer", "Select Model"))
        self.textbox_tweet.setPlaceholderText(_translate("SingleAnalyzer", "Enter a Tweet Content..."))
        self.btn_start.setText(_translate("SingleAnalyzer", "Predict"))
        self.groupbox_human.setTitle(_translate("SingleAnalyzer", "Human"))
        self.lbl_human_result.setText(_translate("SingleAnalyzer", "0%"))
        self.groupbox_bot.setTitle(_translate("SingleAnalyzer", "Bot"))
        self.lbl_bot_result.setText(_translate("SingleAnalyzer", "0%"))

import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SingleAnalyzer = QtWidgets.QWidget()
    ui = Ui_SingleAnalyzer()
    ui.setupUi(SingleAnalyzer)
    SingleAnalyzer.show()
    sys.exit(app.exec_())

