# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 100, 301, 201))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 171, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonHist = QtWidgets.QRadioButton(
            self.verticalLayoutWidget)
        self.radioButtonHist.setChecked(True)
        self.radioButtonHist.setObjectName("radioButtonHist")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButtonHist)
        self.verticalLayout.addWidget(self.radioButtonHist)
        self.radioButtonContrast = QtWidgets.QRadioButton(
            self.verticalLayoutWidget)
        self.radioButtonContrast.setObjectName("radioButtonContrast")
        self.buttonGroup.addButton(self.radioButtonContrast)
        self.verticalLayout.addWidget(self.radioButtonContrast)
        self.radioButtonLog = QtWidgets.QRadioButton(
            self.verticalLayoutWidget)
        self.radioButtonLog.setObjectName("radioButtonLog")
        self.buttonGroup.addButton(self.radioButtonLog)
        self.verticalLayout.addWidget(self.radioButtonLog)
        self.radioButtonReverse = QtWidgets.QRadioButton(
            self.verticalLayoutWidget)
        self.radioButtonReverse.setObjectName("radioButtonReverse")
        self.buttonGroup.addButton(self.radioButtonReverse)
        self.verticalLayout.addWidget(self.radioButtonReverse)
        self.radioButtonMedian = QtWidgets.QRadioButton(
            self.verticalLayoutWidget)
        self.radioButtonMedian.setObjectName("radioButtonMedian")
        self.buttonGroup.addButton(self.radioButtonMedian)
        self.verticalLayout.addWidget(self.radioButtonMedian)
        self.pushButtonApply = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonApply.setGeometry(QtCore.QRect(200, 170, 91, 23))
        self.pushButtonApply.setObjectName("pushButtonApply")
        self.toolButtonLoad = QtWidgets.QToolButton(self.centralwidget)
        self.toolButtonLoad.setGeometry(QtCore.QRect(470, 60, 25, 19))
        self.toolButtonLoad.setObjectName("toolButtonLoad")
        self.lineEditLoad = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLoad.setGeometry(QtCore.QRect(130, 60, 331, 20))
        self.lineEditLoad.setObjectName("lineEditLoad")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 100, 241, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.commandLinkButtonViewer = QtWidgets.QCommandLinkButton(
            self.groupBox_2)
        self.commandLinkButtonViewer.setGeometry(
            QtCore.QRect(20, 20, 185, 41))
        self.commandLinkButtonViewer.setObjectName("commandLinkButtonViewer")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(330, 190, 251, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 131, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButtonJPEG = QtWidgets.QRadioButton(
            self.verticalLayoutWidget_3)
        self.radioButtonJPEG.setObjectName("radioButtonJPEG")
        self.verticalLayout_3.addWidget(self.radioButtonJPEG)
        self.radioButtonPNG = QtWidgets.QRadioButton(
            self.verticalLayoutWidget_3)
        self.radioButtonPNG.setObjectName("radioButtonPNG")
        self.verticalLayout_3.addWidget(self.radioButtonPNG)
        self.radioButtonTIFF = QtWidgets.QRadioButton(
            self.verticalLayoutWidget_3)
        self.radioButtonTIFF.setObjectName("radioButtonTIFF")
        self.verticalLayout_3.addWidget(self.radioButtonTIFF)
        self.pushButtonDonwload = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonDonwload.setGeometry(QtCore.QRect(160, 80, 75, 23))
        self.pushButtonDonwload.setObjectName("pushButtonDonwload")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 71, 20))
        self.label.setObjectName("label")
        self.lineEditEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEmail.setGeometry(QtCore.QRect(130, 20, 331, 20))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 71, 20))
        self.label_2.setObjectName("label_2")
        self.pushButtonEmail = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEmail.setGeometry(QtCore.QRect(470, 20, 75, 23))
        self.pushButtonEmail.setObjectName("pushButtonEmail")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Image Corrections"))
        self.radioButtonHist.setText(
            _translate("MainWindow", "Histogram Equalization"))
        self.radioButtonContrast.setText(
            _translate("MainWindow", "Contrast Stretching"))
        self.radioButtonLog.setText(
            _translate("MainWindow", "Log Compression"))
        self.radioButtonReverse.setText(
            _translate("MainWindow", "Reverse Video"))
        self.radioButtonMedian.setText(
            _translate("MainWindow", "Gamma Correction"))
        self.pushButtonApply.setText(
            _translate("MainWindow", "Apply Processing"))
        self.toolButtonLoad.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Show Images"))
        self.commandLinkButtonViewer.setText(
            _translate("MainWindow", "Launch Image Viewer"))
        self.groupBox_3.setTitle(
            _translate("MainWindow", "Download Processed Image"))
        self.radioButtonJPEG.setText(_translate("MainWindow", "JPEG"))
        self.radioButtonPNG.setText(_translate("MainWindow", "PNG"))
        self.radioButtonTIFF.setText(_translate("MainWindow", "TIFF"))
        self.pushButtonDonwload.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "Input images"))
        self.label_2.setText(_translate("MainWindow", "Email address"))
        self.pushButtonEmail.setText(
            _translate("MainWindow", "Validate Email"))
