# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModelConfig.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModelConfig(object):
    def setupUi(self, ModelConfig):
        ModelConfig.setObjectName("ModelConfig")
        ModelConfig.resize(1186, 683)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ModelConfig.setWindowIcon(icon)
        ModelConfig.setStyleSheet("QLabel#lbl_title {\n"
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
"#btn_embed,#btn_bot, #btn_human {\n"
"font: 75 11pt \"MS Shell Dialog 2\";\n"
"border-radius: 0px;\n"
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
"QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: #fff;\n"
"border: 1px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #eee, stop:1 #ccc);\n"
"border: 1px solid #777;\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #fff, stop:1 #ddd);\n"
"border: 1px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
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
"font: 75 9pt \"MS Shell Dlg 2\";\n"
"color: #1F1F21;\n"
" border: 1px solid gray;\n"
" border-radius: 8px;\n"
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
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(ModelConfig)
        self.verticalLayout_13.setContentsMargins(-1, 5, -1, 8)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.btn_homepage = QtWidgets.QToolButton(ModelConfig)
        self.btn_homepage.setAutoFillBackground(False)
        self.btn_homepage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/homepage.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_homepage.setIcon(icon1)
        self.btn_homepage.setIconSize(QtCore.QSize(35, 35))
        self.btn_homepage.setObjectName("btn_homepage")
        self.horizontalLayout_11.addWidget(self.btn_homepage)
        self.btn_help = QtWidgets.QToolButton(ModelConfig)
        self.btn_help.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_help.setIcon(icon2)
        self.btn_help.setIconSize(QtCore.QSize(35, 35))
        self.btn_help.setObjectName("btn_help")
        self.horizontalLayout_11.addWidget(self.btn_help)
        self.lbl_title = QtWidgets.QLabel(ModelConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title.sizePolicy().hasHeightForWidth())
        self.lbl_title.setSizePolicy(sizePolicy)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.horizontalLayout_11.addWidget(self.lbl_title)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.verticalLayout_13.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalFrame = QtWidgets.QFrame(ModelConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMinimumSize(QtCore.QSize(430, 470))
        self.verticalFrame.setMaximumSize(QtCore.QSize(450, 16777215))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupbox_inputs = QtWidgets.QGroupBox(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupbox_inputs.sizePolicy().hasHeightForWidth())
        self.groupbox_inputs.setSizePolicy(sizePolicy)
        self.groupbox_inputs.setObjectName("groupbox_inputs")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupbox_inputs)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(14, 7, 14, 11)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupbox_inputs)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupbox_inputs)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupbox_inputs)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textbox_embed = QtWidgets.QLineEdit(self.groupbox_inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbox_embed.sizePolicy().hasHeightForWidth())
        self.textbox_embed.setSizePolicy(sizePolicy)
        self.textbox_embed.setMinimumSize(QtCore.QSize(0, 0))
        self.textbox_embed.setMaximumSize(QtCore.QSize(500, 16777215))
        self.textbox_embed.setText("")
        self.textbox_embed.setObjectName("textbox_embed")
        self.verticalLayout_4.addWidget(self.textbox_embed)
        self.textbox_bot = QtWidgets.QLineEdit(self.groupbox_inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbox_bot.sizePolicy().hasHeightForWidth())
        self.textbox_bot.setSizePolicy(sizePolicy)
        self.textbox_bot.setMinimumSize(QtCore.QSize(0, 0))
        self.textbox_bot.setMaximumSize(QtCore.QSize(500, 16777215))
        self.textbox_bot.setObjectName("textbox_bot")
        self.verticalLayout_4.addWidget(self.textbox_bot)
        self.textbox_human = QtWidgets.QLineEdit(self.groupbox_inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbox_human.sizePolicy().hasHeightForWidth())
        self.textbox_human.setSizePolicy(sizePolicy)
        self.textbox_human.setMinimumSize(QtCore.QSize(0, 0))
        self.textbox_human.setMaximumSize(QtCore.QSize(500, 16777215))
        self.textbox_human.setObjectName("textbox_human")
        self.verticalLayout_4.addWidget(self.textbox_human)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn_embed = QtWidgets.QPushButton(self.groupbox_inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_embed.sizePolicy().hasHeightForWidth())
        self.btn_embed.setSizePolicy(sizePolicy)
        self.btn_embed.setMinimumSize(QtCore.QSize(35, 0))
        self.btn_embed.setMaximumSize(QtCore.QSize(35, 16777215))
        self.btn_embed.setObjectName("btn_embed")
        self.verticalLayout_5.addWidget(self.btn_embed)
        self.btn_bot = QtWidgets.QPushButton(self.groupbox_inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_bot.sizePolicy().hasHeightForWidth())
        self.btn_bot.setSizePolicy(sizePolicy)
        self.btn_bot.setMinimumSize(QtCore.QSize(35, 0))
        self.btn_bot.setMaximumSize(QtCore.QSize(35, 16777215))
        self.btn_bot.setObjectName("btn_bot")
        self.verticalLayout_5.addWidget(self.btn_bot)
        self.btn_human = QtWidgets.QPushButton(self.groupbox_inputs)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_human.sizePolicy().hasHeightForWidth())
        self.btn_human.setSizePolicy(sizePolicy)
        self.btn_human.setMinimumSize(QtCore.QSize(35, 0))
        self.btn_human.setMaximumSize(QtCore.QSize(35, 16777215))
        self.btn_human.setObjectName("btn_human")
        self.verticalLayout_5.addWidget(self.btn_human)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout.addWidget(self.groupbox_inputs)
        self.groupbox_dataset = QtWidgets.QGroupBox(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupbox_dataset.sizePolicy().hasHeightForWidth())
        self.groupbox_dataset.setSizePolicy(sizePolicy)
        self.groupbox_dataset.setObjectName("groupbox_dataset")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupbox_dataset)
        self.horizontalLayout_2.setContentsMargins(14, 7, 14, 11)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupbox_dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupbox_dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupbox_dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.slider_train = QtWidgets.QSlider(self.groupbox_dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_train.sizePolicy().hasHeightForWidth())
        self.slider_train.setSizePolicy(sizePolicy)
        self.slider_train.setMinimumSize(QtCore.QSize(255, 0))
        self.slider_train.setMaximumSize(QtCore.QSize(255, 16777215))
        self.slider_train.setMinimum(5)
        self.slider_train.setMaximum(100)
        self.slider_train.setProperty("value", 80)
        self.slider_train.setOrientation(QtCore.Qt.Horizontal)
        self.slider_train.setInvertedAppearance(False)
        self.slider_train.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_train.setObjectName("slider_train")
        self.verticalLayout_6.addWidget(self.slider_train)
        self.slider_val = QtWidgets.QSlider(self.groupbox_dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_val.sizePolicy().hasHeightForWidth())
        self.slider_val.setSizePolicy(sizePolicy)
        self.slider_val.setMinimumSize(QtCore.QSize(255, 0))
        self.slider_val.setMaximumSize(QtCore.QSize(255, 16777215))
        self.slider_val.setMinimum(5)
        self.slider_val.setMaximum(100)
        self.slider_val.setProperty("value", 25)
        self.slider_val.setOrientation(QtCore.Qt.Horizontal)
        self.slider_val.setObjectName("slider_val")
        self.verticalLayout_6.addWidget(self.slider_val)
        self.combobox_gen_method = QtWidgets.QComboBox(self.groupbox_dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_gen_method.sizePolicy().hasHeightForWidth())
        self.combobox_gen_method.setSizePolicy(sizePolicy)
        self.combobox_gen_method.setMinimumSize(QtCore.QSize(94, 22))
        self.combobox_gen_method.setMaximumSize(QtCore.QSize(200, 22))
        self.combobox_gen_method.setObjectName("combobox_gen_method")
        self.combobox_gen_method.addItem("")
        self.combobox_gen_method.addItem("")
        self.verticalLayout_6.addWidget(self.combobox_gen_method)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.lbl_train = QtWidgets.QLabel(self.groupbox_dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_train.sizePolicy().hasHeightForWidth())
        self.lbl_train.setSizePolicy(sizePolicy)
        self.lbl_train.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_train.setObjectName("lbl_train")
        self.verticalLayout_9.addWidget(self.lbl_train)
        self.lbl_val = QtWidgets.QLabel(self.groupbox_dataset)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_val.sizePolicy().hasHeightForWidth())
        self.lbl_val.setSizePolicy(sizePolicy)
        self.lbl_val.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_val.setObjectName("lbl_val")
        self.verticalLayout_9.addWidget(self.lbl_val)
        spacerItem1 = QtWidgets.QSpacerItem(16, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_9.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.groupbox_dataset)
        self.groupbox_trainparams = QtWidgets.QGroupBox(self.verticalFrame)
        self.groupbox_trainparams.setObjectName("groupbox_trainparams")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupbox_trainparams)
        self.horizontalLayout_3.setContentsMargins(14, 7, 14, 11)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.groupbox_trainparams)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.label_7 = QtWidgets.QLabel(self.groupbox_trainparams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.groupbox_trainparams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.groupbox_trainparams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.spinbox_earlystop = QtWidgets.QSpinBox(self.groupbox_trainparams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_earlystop.sizePolicy().hasHeightForWidth())
        self.spinbox_earlystop.setSizePolicy(sizePolicy)
        self.spinbox_earlystop.setMinimumSize(QtCore.QSize(60, 20))
        self.spinbox_earlystop.setMaximumSize(QtCore.QSize(60, 20))
        self.spinbox_earlystop.setMinimum(1)
        self.spinbox_earlystop.setMaximum(100)
        self.spinbox_earlystop.setProperty("value", 5)
        self.spinbox_earlystop.setObjectName("spinbox_earlystop")
        self.horizontalLayout_12.addWidget(self.spinbox_earlystop)
        self.label_11 = QtWidgets.QLabel(self.groupbox_trainparams)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.spinbox_batch = QtWidgets.QSpinBox(self.groupbox_trainparams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_batch.sizePolicy().hasHeightForWidth())
        self.spinbox_batch.setSizePolicy(sizePolicy)
        self.spinbox_batch.setMinimumSize(QtCore.QSize(0, 20))
        self.spinbox_batch.setMaximumSize(QtCore.QSize(60, 20))
        self.spinbox_batch.setMinimum(50)
        self.spinbox_batch.setMaximum(1024)
        self.spinbox_batch.setProperty("value", 50)
        self.spinbox_batch.setObjectName("spinbox_batch")
        self.verticalLayout_8.addWidget(self.spinbox_batch)
        self.spinbox_epoches = QtWidgets.QSpinBox(self.groupbox_trainparams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinbox_epoches.sizePolicy().hasHeightForWidth())
        self.spinbox_epoches.setSizePolicy(sizePolicy)
        self.spinbox_epoches.setMinimumSize(QtCore.QSize(0, 20))
        self.spinbox_epoches.setMaximumSize(QtCore.QSize(60, 20))
        self.spinbox_epoches.setMinimum(1)
        self.spinbox_epoches.setMaximum(100)
        self.spinbox_epoches.setProperty("value", 15)
        self.spinbox_epoches.setObjectName("spinbox_epoches")
        self.verticalLayout_8.addWidget(self.spinbox_epoches)
        self.checkbox_additional_feats = QtWidgets.QCheckBox(self.groupbox_trainparams)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_additional_feats.sizePolicy().hasHeightForWidth())
        self.checkbox_additional_feats.setSizePolicy(sizePolicy)
        self.checkbox_additional_feats.setMinimumSize(QtCore.QSize(0, 20))
        self.checkbox_additional_feats.setMaximumSize(QtCore.QSize(100, 20))
        self.checkbox_additional_feats.setChecked(True)
        self.checkbox_additional_feats.setObjectName("checkbox_additional_feats")
        self.verticalLayout_8.addWidget(self.checkbox_additional_feats)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.groupbox_trainparams)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(14, 0, 14, 0)
        self.horizontalLayout_4.setSpacing(31)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_start = QtWidgets.QPushButton(self.verticalFrame)
        self.btn_start.setEnabled(True)
        self.btn_start.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_start.setMaximumSize(QtCore.QSize(16777215, 35))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/run.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_start.setIcon(icon3)
        self.btn_start.setIconSize(QtCore.QSize(30, 30))
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_4.addWidget(self.btn_start)
        self.btn_stop = QtWidgets.QPushButton(self.verticalFrame)
        self.btn_stop.setEnabled(False)
        self.btn_stop.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_stop.setMaximumSize(QtCore.QSize(16777215, 35))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stop.setIcon(icon4)
        self.btn_stop.setIconSize(QtCore.QSize(25, 25))
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout_4.addWidget(self.btn_stop)
        self.btn_save = QtWidgets.QPushButton(self.verticalFrame)
        self.btn_save.setEnabled(False)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 35))
        self.btn_save.setMaximumSize(QtCore.QSize(16777215, 35))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon5)
        self.btn_save.setIconSize(QtCore.QSize(25, 25))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_4.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(14, 8, 14, 0)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.label_12 = QtWidgets.QLabel(self.verticalFrame)
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
        self.progressbar_epoches = QtWidgets.QProgressBar(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressbar_epoches.sizePolicy().hasHeightForWidth())
        self.progressbar_epoches.setSizePolicy(sizePolicy)
        self.progressbar_epoches.setMinimumSize(QtCore.QSize(0, 17))
        self.progressbar_epoches.setMaximumSize(QtCore.QSize(16777215, 17))
        self.progressbar_epoches.setMinimum(0)
        self.progressbar_epoches.setMaximum(100)
        self.progressbar_epoches.setProperty("value", 0)
        self.progressbar_epoches.setAlignment(QtCore.Qt.AlignCenter)
        self.progressbar_epoches.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressbar_epoches.setObjectName("progressbar_epoches")
        self.verticalLayout_11.addWidget(self.progressbar_epoches)
        self.progressbar_batch = QtWidgets.QProgressBar(self.verticalFrame)
        self.progressbar_batch.setMinimumSize(QtCore.QSize(0, 17))
        self.progressbar_batch.setMaximumSize(QtCore.QSize(16777215, 17))
        self.progressbar_batch.setProperty("value", 0)
        self.progressbar_batch.setAlignment(QtCore.Qt.AlignCenter)
        self.progressbar_batch.setObjectName("progressbar_batch")
        self.verticalLayout_11.addWidget(self.progressbar_batch)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addWidget(self.verticalFrame)
        self.verticalFrame_11 = QtWidgets.QFrame(ModelConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame_11.sizePolicy().hasHeightForWidth())
        self.verticalFrame_11.setSizePolicy(sizePolicy)
        self.verticalFrame_11.setMinimumSize(QtCore.QSize(600, 0))
        self.verticalFrame_11.setObjectName("verticalFrame_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalFrame_11)
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalFrame_4 = QtWidgets.QFrame(self.verticalFrame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_4.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_4.setSizePolicy(sizePolicy)
        self.horizontalFrame_4.setObjectName("horizontalFrame_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalFrame_4)
        self.horizontalLayout_8.setContentsMargins(-1, 6, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.graph_acc_epoch = PlotWidget(self.horizontalFrame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_acc_epoch.sizePolicy().hasHeightForWidth())
        self.graph_acc_epoch.setSizePolicy(sizePolicy)
        self.graph_acc_epoch.setMinimumSize(QtCore.QSize(200, 200))
        self.graph_acc_epoch.setMaximumSize(QtCore.QSize(9999999, 9999999))
        self.graph_acc_epoch.setObjectName("graph_acc_epoch")
        self.horizontalLayout_8.addWidget(self.graph_acc_epoch)
        self.graph_loss_epoch = PlotWidget(self.horizontalFrame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_loss_epoch.sizePolicy().hasHeightForWidth())
        self.graph_loss_epoch.setSizePolicy(sizePolicy)
        self.graph_loss_epoch.setMinimumSize(QtCore.QSize(200, 200))
        self.graph_loss_epoch.setMaximumSize(QtCore.QSize(9999999, 9999999))
        self.graph_loss_epoch.setObjectName("graph_loss_epoch")
        self.horizontalLayout_8.addWidget(self.graph_loss_epoch)
        self.verticalLayout_12.addWidget(self.horizontalFrame_4)
        self.horizontalFrame_41 = QtWidgets.QFrame(self.verticalFrame_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_41.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_41.setSizePolicy(sizePolicy)
        self.horizontalFrame_41.setObjectName("horizontalFrame_41")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalFrame_41)
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.graph_acc_batch = PlotWidget(self.horizontalFrame_41)
        self.graph_acc_batch.setMinimumSize(QtCore.QSize(200, 200))
        self.graph_acc_batch.setObjectName("graph_acc_batch")
        self.horizontalLayout_9.addWidget(self.graph_acc_batch)
        self.graph_loss_batch = PlotWidget(self.horizontalFrame_41)
        self.graph_loss_batch.setMinimumSize(QtCore.QSize(200, 200))
        self.graph_loss_batch.setObjectName("graph_loss_batch")
        self.horizontalLayout_9.addWidget(self.graph_loss_batch)
        self.verticalLayout_12.addWidget(self.horizontalFrame_41)
        self.horizontalLayout_6.addWidget(self.verticalFrame_11)
        self.verticalLayout_13.addLayout(self.horizontalLayout_6)
        self.horizontalGroupBox_4 = QtWidgets.QGroupBox(ModelConfig)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalGroupBox_4.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox_4.setSizePolicy(sizePolicy)
        self.horizontalGroupBox_4.setObjectName("horizontalGroupBox_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_4)
        self.horizontalLayout_10.setContentsMargins(10, 11, 10, 11)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.textbox_log = QtWidgets.QTextEdit(self.horizontalGroupBox_4)
        self.textbox_log.setDocumentTitle("")
        self.textbox_log.setReadOnly(True)
        self.textbox_log.setPlaceholderText("")
        self.textbox_log.setObjectName("textbox_log")
        self.horizontalLayout_10.addWidget(self.textbox_log)
        self.verticalLayout_13.addWidget(self.horizontalGroupBox_4)

        self.retranslateUi(ModelConfig)
        QtCore.QMetaObject.connectSlotsByName(ModelConfig)

    def retranslateUi(self, ModelConfig):
        _translate = QtCore.QCoreApplication.translate
        ModelConfig.setWindowTitle(_translate("ModelConfig", "Model Configuration"))
        self.btn_homepage.setToolTip(_translate("ModelConfig", "Back To HomePage"))
        self.btn_help.setToolTip(_translate("ModelConfig", "Open Help Documentation"))
        self.lbl_title.setText(_translate("ModelConfig", "Model Configuration"))
        self.groupbox_inputs.setTitle(_translate("ModelConfig", "Input Files"))
        self.label.setText(_translate("ModelConfig", "Embedding File:"))
        self.label_2.setText(_translate("ModelConfig", "Bot File:"))
        self.label_3.setText(_translate("ModelConfig", "Human File:"))
        self.btn_embed.setText(_translate("ModelConfig", "..."))
        self.btn_bot.setText(_translate("ModelConfig", "..."))
        self.btn_human.setText(_translate("ModelConfig", "..."))
        self.groupbox_dataset.setTitle(_translate("ModelConfig", "Dataset Config"))
        self.label_4.setText(_translate("ModelConfig", "Training Split:"))
        self.label_5.setText(_translate("ModelConfig", "Validation Split:"))
        self.label_6.setText(_translate("ModelConfig", "Generation Method:"))
        self.combobox_gen_method.setItemText(0, _translate("ModelConfig", "User Grouping"))
        self.combobox_gen_method.setItemText(1, _translate("ModelConfig", "Random Pairing"))
        self.lbl_train.setText(_translate("ModelConfig", "80%"))
        self.lbl_val.setText(_translate("ModelConfig", "20%"))
        self.groupbox_trainparams.setTitle(_translate("ModelConfig", "Training Parameters"))
        self.label_10.setText(_translate("ModelConfig", "Early Stopping After:"))
        self.label_7.setText(_translate("ModelConfig", "Batch Size:"))
        self.label_8.setText(_translate("ModelConfig", "Epochs:"))
        self.label_9.setText(_translate("ModelConfig", "Additional Features:"))
        self.label_11.setText(_translate("ModelConfig", "Epochs"))
        self.checkbox_additional_feats.setText(_translate("ModelConfig", "Enabled"))
        self.btn_start.setText(_translate("ModelConfig", "Start"))
        self.btn_stop.setText(_translate("ModelConfig", "Stop"))
        self.btn_save.setText(_translate("ModelConfig", "Save"))
        self.label_13.setText(_translate("ModelConfig", "Epoches"))
        self.label_12.setText(_translate("ModelConfig", "Batch"))
        self.horizontalGroupBox_4.setTitle(_translate("ModelConfig", "Log"))
from pyqtgraph import PlotWidget
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModelConfig = QtWidgets.QWidget()
    ui = Ui_ModelConfig()
    ui.setupUi(ModelConfig)
    ModelConfig.show()
    sys.exit(app.exec_())
