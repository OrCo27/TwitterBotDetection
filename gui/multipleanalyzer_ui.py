# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultipleAnalyzer.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MultipleAnalayzer(object):
    def setupUi(self, MultipleAnalayzer):
        MultipleAnalayzer.setObjectName("MultipleAnalayzer")
        MultipleAnalayzer.resize(964, 670)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MultipleAnalayzer.sizePolicy().hasHeightForWidth())
        MultipleAnalayzer.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MultipleAnalayzer.setWindowIcon(icon)
        MultipleAnalayzer.setStyleSheet("#lbl_title {\n"
"font: 75 20pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"qproperty-alignment: AlignCenter;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3643f7, stop:1 #3643f7);\n"
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
"#btn_tweets_file {\n"
"font: 75 11pt \"MS Shell Dialog 2\";\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"#btn_classify,#btn_save {\n"
"font: 75 11pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"}\n"
"#lbl_threshold {\n"
"font: 75 9pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"}\n"
"#spinbox_threshold {\n"
"font: 75 10pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"}\n"
"QPushButton {\n"
"font: 75 13pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"border-radius: 9px;\n"
"border: 1px solid black;\n"
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
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MultipleAnalayzer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn_homepage = QtWidgets.QToolButton(MultipleAnalayzer)
        self.btn_homepage.setAutoFillBackground(False)
        self.btn_homepage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/homepage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_homepage.setIcon(icon1)
        self.btn_homepage.setIconSize(QtCore.QSize(35, 35))
        self.btn_homepage.setObjectName("btn_homepage")
        self.horizontalLayout_11.addWidget(self.btn_homepage)
        self.btn_help = QtWidgets.QToolButton(MultipleAnalayzer)
        self.btn_help.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_help.setIcon(icon2)
        self.btn_help.setIconSize(QtCore.QSize(35, 35))
        self.btn_help.setObjectName("btn_help")
        self.horizontalLayout_11.addWidget(self.btn_help)
        self.lbl_title = QtWidgets.QLabel(MultipleAnalayzer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title.sizePolicy().hasHeightForWidth())
        self.lbl_title.setSizePolicy(sizePolicy)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.horizontalLayout_11.addWidget(self.lbl_title)
        spacerItem = QtWidgets.QSpacerItem(45, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.frame = QtWidgets.QFrame(MultipleAnalayzer)
        self.frame.setMinimumSize(QtCore.QSize(700, 0))
        self.frame.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frame.setObjectName("frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_8.setContentsMargins(1, 16, 1, 14)
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.combobox_model = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_model.sizePolicy().hasHeightForWidth())
        self.combobox_model.setSizePolicy(sizePolicy)
        self.combobox_model.setMinimumSize(QtCore.QSize(124, 0))
        self.combobox_model.setMaximumSize(QtCore.QSize(270, 16777215))
        self.combobox_model.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.combobox_model.setObjectName("combobox_model")
        self.combobox_model.addItem("")
        self.horizontalLayout_3.addWidget(self.combobox_model)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.groupbox_config = QtWidgets.QGroupBox(MultipleAnalayzer)
        self.groupbox_config.setMinimumSize(QtCore.QSize(700, 0))
        self.groupbox_config.setMaximumSize(QtCore.QSize(700, 16777215))
        self.groupbox_config.setObjectName("groupbox_config")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupbox_config)
        self.horizontalLayout_2.setContentsMargins(6, 10, 6, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupbox_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.groupbox_config)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_7 = QtWidgets.QLabel(self.groupbox_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 4, -1, 2)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textbox_tweets_file = QtWidgets.QLineEdit(self.groupbox_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbox_tweets_file.sizePolicy().hasHeightForWidth())
        self.textbox_tweets_file.setSizePolicy(sizePolicy)
        self.textbox_tweets_file.setMinimumSize(QtCore.QSize(370, 0))
        self.textbox_tweets_file.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textbox_tweets_file.setObjectName("textbox_tweets_file")
        self.horizontalLayout.addWidget(self.textbox_tweets_file)
        self.btn_tweets_file = QtWidgets.QPushButton(self.groupbox_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tweets_file.sizePolicy().hasHeightForWidth())
        self.btn_tweets_file.setSizePolicy(sizePolicy)
        self.btn_tweets_file.setMinimumSize(QtCore.QSize(32, 18))
        self.btn_tweets_file.setMaximumSize(QtCore.QSize(32, 16777215))
        self.btn_tweets_file.setObjectName("btn_tweets_file")
        self.horizontalLayout.addWidget(self.btn_tweets_file)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.checkbox_header = QtWidgets.QCheckBox(self.groupbox_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_header.sizePolicy().hasHeightForWidth())
        self.checkbox_header.setSizePolicy(sizePolicy)
        self.checkbox_header.setChecked(True)
        self.checkbox_header.setObjectName("checkbox_header")
        self.verticalLayout_7.addWidget(self.checkbox_header)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.spinbox_rand_tweets = QtWidgets.QSpinBox(self.groupbox_config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_rand_tweets.sizePolicy().hasHeightForWidth())
        self.spinbox_rand_tweets.setSizePolicy(sizePolicy)
        self.spinbox_rand_tweets.setMinimumSize(QtCore.QSize(0, 20))
        self.spinbox_rand_tweets.setMaximumSize(QtCore.QSize(60, 20))
        self.spinbox_rand_tweets.setMinimum(3)
        self.spinbox_rand_tweets.setMaximum(5000)
        self.spinbox_rand_tweets.setProperty("value", 50)
        self.spinbox_rand_tweets.setObjectName("spinbox_rand_tweets")
        self.horizontalLayout_8.addWidget(self.spinbox_rand_tweets)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addWidget(self.groupbox_config, 0, QtCore.Qt.AlignHCenter)
        self.frame1 = QtWidgets.QFrame(MultipleAnalayzer)
        self.frame1.setMinimumSize(QtCore.QSize(700, 0))
        self.frame1.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frame1.setObjectName("frame1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout_4.setContentsMargins(35, 7, 35, 7)
        self.horizontalLayout_4.setSpacing(34)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.btn_start = QtWidgets.QPushButton(self.frame1)
        self.btn_start.setEnabled(False)
        self.btn_start.setMinimumSize(QtCore.QSize(122, 40))
        self.btn_start.setMaximumSize(QtCore.QSize(16777214, 40))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/predict.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_start.setIcon(icon3)
        self.btn_start.setIconSize(QtCore.QSize(33, 33))
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_4.addWidget(self.btn_start)
        self.btn_stop = QtWidgets.QPushButton(self.frame1)
        self.btn_stop.setEnabled(False)
        self.btn_stop.setMinimumSize(QtCore.QSize(122, 40))
        self.btn_stop.setMaximumSize(QtCore.QSize(16777215, 40))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon4)
        self.btn_stop.setIconSize(QtCore.QSize(30, 30))
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_4.addWidget(self.btn_stop)
        self.btn_save = QtWidgets.QPushButton(self.frame1)
        self.btn_save.setEnabled(False)
        self.btn_save.setMinimumSize(QtCore.QSize(122, 40))
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 40))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/export_excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon5)
        self.btn_save.setIconSize(QtCore.QSize(27, 27))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_4.addWidget(self.btn_save)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_2.addWidget(self.frame1, 0, QtCore.Qt.AlignHCenter)
        self.horizontalGroupBox_3 = QtWidgets.QGroupBox(MultipleAnalayzer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalGroupBox_3.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox_3.setSizePolicy(sizePolicy)
        self.horizontalGroupBox_3.setMaximumSize(QtCore.QSize(16777215, 300))
        self.horizontalGroupBox_3.setTitle("")
        self.horizontalGroupBox_3.setObjectName("horizontalGroupBox_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_3)
        self.horizontalLayout_9.setContentsMargins(10, 5, 0, 5)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.histogram = QChartView(self.horizontalGroupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogram.sizePolicy().hasHeightForWidth())
        self.histogram.setSizePolicy(sizePolicy)
        self.histogram.setMinimumSize(QtCore.QSize(380, 0))
        self.histogram.setObjectName("histogram")
        self.horizontalLayout_9.addWidget(self.histogram)
        self.piechart = QChartView(self.horizontalGroupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.piechart.sizePolicy().hasHeightForWidth())
        self.piechart.setSizePolicy(sizePolicy)
        self.piechart.setMinimumSize(QtCore.QSize(270, 270))
        self.piechart.setMaximumSize(QtCore.QSize(350, 16777215))
        self.piechart.setObjectName("piechart")
        self.horizontalLayout_9.addWidget(self.piechart)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalFrame_3 = QtWidgets.QFrame(self.horizontalGroupBox_3)
        self.verticalFrame_3.setObjectName("verticalFrame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_3.setContentsMargins(1, 0, 0, -1)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupbox_threshold = QtWidgets.QGroupBox(self.verticalFrame_3)
        self.groupbox_threshold.setEnabled(False)
        self.groupbox_threshold.setMinimumSize(QtCore.QSize(100, 0))
        self.groupbox_threshold.setMaximumSize(QtCore.QSize(90, 16777215))
        self.groupbox_threshold.setObjectName("groupbox_threshold")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupbox_threshold)
        self.verticalLayout_6.setContentsMargins(0, 5, 0, 10)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lbl_threshold = QtWidgets.QLabel(self.groupbox_threshold)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_threshold.sizePolicy().hasHeightForWidth())
        self.lbl_threshold.setSizePolicy(sizePolicy)
        self.lbl_threshold.setObjectName("lbl_threshold")
        self.horizontalLayout_10.addWidget(self.lbl_threshold)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.spinbox_threshold = QtWidgets.QDoubleSpinBox(self.groupbox_threshold)
        self.spinbox_threshold.setMinimumSize(QtCore.QSize(50, 22))
        self.spinbox_threshold.setMaximumSize(QtCore.QSize(50, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.spinbox_threshold.setFont(font)
        self.spinbox_threshold.setSpecialValueText("")
        self.spinbox_threshold.setDecimals(1)
        self.spinbox_threshold.setMinimum(0.1)
        self.spinbox_threshold.setMaximum(1.0)
        self.spinbox_threshold.setSingleStep(0.1)
        self.spinbox_threshold.setProperty("value", 0.5)
        self.spinbox_threshold.setObjectName("spinbox_threshold")
        self.verticalLayout_6.addWidget(self.spinbox_threshold, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.btn_classify = QtWidgets.QPushButton(self.groupbox_threshold)
        self.btn_classify.setEnabled(False)
        self.btn_classify.setMinimumSize(QtCore.QSize(80, 28))
        self.btn_classify.setMaximumSize(QtCore.QSize(80, 28))
        self.btn_classify.setIconSize(QtCore.QSize(25, 25))
        self.btn_classify.setObjectName("btn_classify")
        self.verticalLayout_13.addWidget(self.btn_classify, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalLayout_3.addWidget(self.groupbox_threshold)
        self.verticalLayout_5.addWidget(self.verticalFrame_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.horizontalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_2.addWidget(self.horizontalGroupBox_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(14, 8, 14, 0)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_13 = QtWidgets.QLabel(MultipleAnalayzer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.label_12 = QtWidgets.QLabel(MultipleAnalayzer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_10.addWidget(self.label_12)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.progressbar_tweets = QtWidgets.QProgressBar(MultipleAnalayzer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressbar_tweets.sizePolicy().hasHeightForWidth())
        self.progressbar_tweets.setSizePolicy(sizePolicy)
        self.progressbar_tweets.setMinimumSize(QtCore.QSize(0, 17))
        self.progressbar_tweets.setMaximumSize(QtCore.QSize(16777215, 17))
        self.progressbar_tweets.setMinimum(0)
        self.progressbar_tweets.setMaximum(100)
        self.progressbar_tweets.setProperty("value", 0)
        self.progressbar_tweets.setAlignment(QtCore.Qt.AlignCenter)
        self.progressbar_tweets.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressbar_tweets.setObjectName("progressbar_tweets")
        self.verticalLayout_11.addWidget(self.progressbar_tweets)
        self.progressbar_batch = QtWidgets.QProgressBar(MultipleAnalayzer)
        self.progressbar_batch.setMinimumSize(QtCore.QSize(0, 17))
        self.progressbar_batch.setMaximumSize(QtCore.QSize(16777215, 17))
        self.progressbar_batch.setProperty("value", 0)
        self.progressbar_batch.setAlignment(QtCore.Qt.AlignCenter)
        self.progressbar_batch.setObjectName("progressbar_batch")
        self.verticalLayout_11.addWidget(self.progressbar_batch)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(MultipleAnalayzer)
        QtCore.QMetaObject.connectSlotsByName(MultipleAnalayzer)

    def retranslateUi(self, MultipleAnalayzer):
        _translate = QtCore.QCoreApplication.translate
        MultipleAnalayzer.setWindowTitle(_translate("MultipleAnalayzer", "Multiple Tweets Analyzer"))
        self.btn_homepage.setToolTip(_translate("MultipleAnalayzer", "Back To HomePage"))
        self.btn_help.setToolTip(_translate("MultipleAnalayzer", "Open Help Documentation"))
        self.lbl_title.setText(_translate("MultipleAnalayzer", "Multiple Tweets Analyzer"))
        self.combobox_model.setItemText(0, _translate("MultipleAnalayzer", "Select Model"))
        self.groupbox_config.setTitle(_translate("MultipleAnalayzer", "Input Configuration"))
        self.label_2.setText(_translate("MultipleAnalayzer", "Tweets File:"))
        self.label_7.setText(_translate("MultipleAnalayzer", "Random Tweets:"))
        self.btn_tweets_file.setText(_translate("MultipleAnalayzer", "..."))
        self.checkbox_header.setText(_translate("MultipleAnalayzer", "Include Header"))
        self.btn_start.setText(_translate("MultipleAnalayzer", "Predict"))
        self.btn_stop.setText(_translate("MultipleAnalayzer", "Stop"))
        self.btn_save.setText(_translate("MultipleAnalayzer", "Export"))
        self.lbl_threshold.setText(_translate("MultipleAnalayzer", "Threshold:"))
        self.btn_classify.setText(_translate("MultipleAnalayzer", "Update"))
        self.label_13.setText(_translate("MultipleAnalayzer", "Tweets"))
        self.label_12.setText(_translate("MultipleAnalayzer", "Batch"))
from PyQt5.QtChart import QChartView
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MultipleAnalayzer = QtWidgets.QWidget()
    ui = Ui_MultipleAnalayzer()
    ui.setupUi(MultipleAnalayzer)
    MultipleAnalayzer.show()
    sys.exit(app.exec_())
