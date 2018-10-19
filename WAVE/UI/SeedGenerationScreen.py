# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SeedGenerationScreen.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import random
import audit
import UI
import UI.UIUtils

class Ui_Seed_Generation(object):

    seed = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 364)
        UI.UIUtils.SetPallete(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(700, 400))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, -1, 20, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.seedValueTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.seedValueTextEdit.setMinimumSize(QtCore.QSize(800, 50))
        self.seedValueTextEdit.setMaximumSize(QtCore.QSize(1000, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.seedValueTextEdit.setFont(font)
        self.seedValueTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.seedValueTextEdit.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.seedValueTextEdit.setMaxLength(20)
        #self.seedValueTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        #self.seedValueTextEdit.setLineWidth(2)
        #self.seedValueTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.seedValueTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        #self.seedValueTextEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        # self.seedValueTextEdit.setOverwriteMode(True)
        self.seedValueTextEdit.setObjectName("seedValueTextEdit")
        self.horizontalLayout_2.addWidget(self.seedValueTextEdit)
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setMinimumSize(QtCore.QSize(100, 35))
        self.confirmButton.setMaximumSize(QtCore.QSize(100, 35))
        self.confirmButton.setObjectName("confirmButton")
        self.horizontalLayout_2.addWidget(self.confirmButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setMinimumSize(QtCore.QSize(100, 35))
        self.backButton.setMaximumSize(QtCore.QSize(100, 35))
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_3.addWidget(self.backButton)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setMinimumSize(QtCore.QSize(100, 35))
        self.exitButton.setMaximumSize(QtCore.QSize(100, 35))
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout_3.addWidget(self.exitButton)
        self.saveConfigurationButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveConfigurationButton.setMinimumSize(QtCore.QSize(100, 35))
        self.saveConfigurationButton.setMaximumSize(QtCore.QSize(100, 35))
        self.saveConfigurationButton.setObjectName("saveConfigurationButton")
        self.horizontalLayout_3.addWidget(self.saveConfigurationButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.confirmButton.clicked.connect(self.confirm_seed)
        self.backButton.clicked.connect(self.back)
        self.exitButton.clicked.connect(self.exit)
        self.saveConfigurationButton.clicked.connect(self.save_configuration)
        # self.onlyInt = QtGui.QIntValidator()
        # self.seedValueTextEdit.setValidator(self.onlyInt)
        self.seedValueTextEdit.setInputMask("999999999999999999999999999999")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RI WAVE - Seed Generation"))
        self.seedValueTextEdit.setPlaceholderText(_translate("MainWindow", "Enter Seed Here"))
        self.confirmButton.setText(_translate("MainWindow", "Confirm"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.saveConfigurationButton.setText(_translate("MainWindow", "Save"))

    def __init__(self):
        self._election = None
        self._current_ballot = None
        self._audit = None
        self._audits = audit.get_audits()

    def init(self, election, audit):
        self._election = election
        self._audit = audit

    def confirm_seed(self):
        print(self.get_seed_text())
        self.seed = int(self.get_seed_text())
        if (self.seed is not None):
            random.seed(self.seed)
            print(random.random())


    def get_seed_text(self):
        return self.seedValueTextEdit.text()

    # TODO: Implement if needed
    def back(self):
        print("back")

    #TODO: Implement
    def exit(self):
        print("exit")


    def open_main_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI.Ui_MainWindow()
        self.ui.init(self._election, self._audit, int(self.seed))
        self.ui.setupUi(self.window)
        self.window.show()

    #TODO: Call main window for audit
    def save_configuration(self):
        print("Next")
        if (self.seed is not None):
            random.seed(self.seed)
            print(random.random())
            self.open_main_window()



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Seed_Generation()
    ui.setupUi(MainWindow)
    MainWindow.show()

    app.exec_()

