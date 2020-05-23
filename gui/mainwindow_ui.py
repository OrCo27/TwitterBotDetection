# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(570, 666)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainMenu.sizePolicy().hasHeightForWidth())
        MainMenu.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainMenu.setWindowIcon(icon)
        MainMenu.setWindowOpacity(1.0)
        MainMenu.setStyleSheet("QWidget {\n"
"background: white\n"
"}\n"
"\n"
"QLabel#lbl_title {\n"
"font: 75 30pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"qproperty-alignment: AlignCenter;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #004a7c, stop:1 #005691);\n"
"}\n"
"\n"
"QLabel#lbl_created {\n"
"font: 75 10pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #004a7c, stop:1 #005691);\n"
"}\n"
"\n"
"QPushButton {\n"
"font: 75 13pt \"Microsoft YaHei UI\";\n"
"font-weight: bold;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #004a7c, stop:1 #005691);\n"
"border-style: solid;\n"
"border-radius:21px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(cx: 0.3, cy: -0.4,\n"
"fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #2F4F4F, stop: 1 #2F4F4F);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qradialgradient(cx: 0.4, cy: -0.1,\n"
"fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #a9a9a9, stop: 1 #a9a9a9);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(MainMenu)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(18)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_created = QtWidgets.QLabel(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_created.sizePolicy().hasHeightForWidth())
        self.lbl_created.setSizePolicy(sizePolicy)
        self.lbl_created.setMinimumSize(QtCore.QSize(361, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_created.setFont(font)
        self.lbl_created.setObjectName("lbl_created")
        self.gridLayout.addWidget(self.lbl_created, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setContentsMargins(0, 13, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_multi = QtWidgets.QPushButton(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_multi.sizePolicy().hasHeightForWidth())
        self.btn_multi.setSizePolicy(sizePolicy)
        self.btn_multi.setMinimumSize(QtCore.QSize(360, 50))
        self.btn_multi.setMaximumSize(QtCore.QSize(390, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_multi.setFont(font)
        self.btn_multi.setObjectName("btn_multi")
        self.gridLayout_2.addWidget(self.btn_multi, 3, 0, 1, 1)
        self.btn_config = QtWidgets.QPushButton(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_config.sizePolicy().hasHeightForWidth())
        self.btn_config.setSizePolicy(sizePolicy)
        self.btn_config.setMinimumSize(QtCore.QSize(360, 50))
        self.btn_config.setMaximumSize(QtCore.QSize(390, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_config.setFont(font)
        self.btn_config.setObjectName("btn_config")
        self.gridLayout_2.addWidget(self.btn_config, 0, 0, 1, 1)
        self.btn_help = QtWidgets.QPushButton(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_help.sizePolicy().hasHeightForWidth())
        self.btn_help.setSizePolicy(sizePolicy)
        self.btn_help.setMinimumSize(QtCore.QSize(360, 50))
        self.btn_help.setMaximumSize(QtCore.QSize(390, 50))
        self.btn_help.setIconSize(QtCore.QSize(30, 30))
        self.btn_help.setObjectName("btn_help")
        self.gridLayout_2.addWidget(self.btn_help, 4, 0, 1, 1)
        self.btn_single = QtWidgets.QPushButton(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_single.sizePolicy().hasHeightForWidth())
        self.btn_single.setSizePolicy(sizePolicy)
        self.btn_single.setMinimumSize(QtCore.QSize(360, 50))
        self.btn_single.setMaximumSize(QtCore.QSize(390, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_single.setFont(font)
        self.btn_single.setObjectName("btn_single")
        self.gridLayout_2.addWidget(self.btn_single, 2, 0, 1, 1)
        self.btn_test = QtWidgets.QPushButton(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_test.sizePolicy().hasHeightForWidth())
        self.btn_test.setSizePolicy(sizePolicy)
        self.btn_test.setMinimumSize(QtCore.QSize(360, 50))
        self.btn_test.setMaximumSize(QtCore.QSize(390, 16777215))
        self.btn_test.setObjectName("btn_test")
        self.gridLayout_2.addWidget(self.btn_test, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.frame = QtWidgets.QFrame(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 188))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 188))
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(500, 188))
        self.label.setMaximumSize(QtCore.QSize(16777215, 188))
        self.label.setStyleSheet("image: url(:/images/logo.png);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Main Menu"))
        self.lbl_created.setText(_translate("MainMenu", "<html><head/><body><p align=\"center\">Created By Or Cohen &amp; Eliran Menashe<br/>Supervisor: Dr. Renata Avros<br/>Date: 01/05/2020</p></body></html>"))
        self.btn_multi.setText(_translate("MainMenu", "Analyze Multiple Tweets"))
        self.btn_config.setText(_translate("MainMenu", "Configuration"))
        self.btn_help.setText(_translate("MainMenu", "Help"))
        self.btn_single.setText(_translate("MainMenu", "Analyze Single Tweet"))
        self.btn_test.setText(_translate("MainMenu", "Model Testing"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QWidget()
    ui = Ui_MainMenu()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec_())
