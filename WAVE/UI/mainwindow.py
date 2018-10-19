# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import  QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
import enum
import audit
import election
import random
import csv
import UI
import UI.UIUtils

from PyQt5.QtCore import pyqtSignal
class Ui_MainWindow(object):
    closed = pyqtSignal()
    audited_ballot_nums = []
    audited_ballots = []
    current_audit_ballot = 0
    total_rows = 0
    filename = 'Election_Params.csv'
    seed = 0
    #audit_type = "bcrla"

    class TableNum(enum.IntEnum):
        AUDIT_NUM = 0
        BALLOT_NUM = 1
        REPORTED_VALUE = 2
        ACTUAL_VALUE = 3

    def __init__(self):
        self._election = None
        self._current_ballot = None
        self._audit = None

        self._audits = audit.get_audits()

    def init(self, election, audit,seed):
        self._election = election
        self._audit = audit
        self.seed = int(seed)

        print("SEED " + str(self.seed))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 800)
        UI.UIUtils.SetPallete(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 7, 16, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 2, 16, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 0, 0, 2, 1)
        self.auditTable = QtWidgets.QTableWidget(self.centralwidget)
        self.auditTable.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.auditTable.sizePolicy().hasHeightForWidth())
        self.auditTable.setSizePolicy(sizePolicy)
        self.auditTable.setMinimumSize(QtCore.QSize(500, 251))
        self.auditTable.setMaximumSize(QtCore.QSize(1000, 1000))
        self.auditTable.setBaseSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.small_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.auditTable.setFont(font)
        self.auditTable.setAutoFillBackground(False)
        self.auditTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.auditTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.auditTable.setAlternatingRowColors(True)
        self.auditTable.setIconSize(QtCore.QSize(0, 0))
        self.auditTable.setGridStyle(QtCore.Qt.SolidLine)
        self.auditTable.setWordWrap(True)
        self.auditTable.setRowCount(0)
        self.auditTable.setColumnCount(4)
        self.auditTable.setObjectName("auditTable")
        item = QtWidgets.QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.auditTable.setHorizontalHeaderItem(3, item)
        self.auditTable.horizontalHeader().setVisible(True)
        self.auditTable.horizontalHeader().setDefaultSectionSize(53)
        self.auditTable.verticalHeader().setVisible(False)
        self.auditTable.verticalHeader().setDefaultSectionSize(22)
        self.auditTable.verticalHeader().setMinimumSectionSize(11)
        self.gridLayout_2.addWidget(self.auditTable, 1, 1, 15, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 16, 1, 1, 1)
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.exportButton.setFont(font)
        self.exportButton.setObjectName("exportButton")
        self.gridLayout_2.addWidget(self.exportButton, 15, 10, 1, 2)
        self.mainPageSectionLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPageSectionLabel.sizePolicy().hasHeightForWidth())
        self.mainPageSectionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.mainPageSectionLabel.setFont(font)
        self.mainPageSectionLabel.setAutoFillBackground(True)
        self.mainPageSectionLabel.setIndent(20)
        self.mainPageSectionLabel.setObjectName("mainPageSectionLabel")
        self.gridLayout_2.addWidget(self.mainPageSectionLabel, 0, 1, 1, 12)
        self.statusLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.large_font_size)
        self.statusLabel.setFont(font)
        self.statusLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statusLabel.setIndent(0)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout_2.addWidget(self.statusLabel, 5, 10, 1, 2)
        self.electionDetailsSectionLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.electionDetailsSectionLabel.setFont(font)
        self.electionDetailsSectionLabel.setAutoFillBackground(True)
        self.electionDetailsSectionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.electionDetailsSectionLabel.setIndent(0)
        self.electionDetailsSectionLabel.setObjectName("electionDetailsSectionLabel")
        self.gridLayout_2.addWidget(self.electionDetailsSectionLabel, 1, 3, 2, 4)
        self.recomputeButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.recomputeButton.setFont(font)
        self.recomputeButton.setObjectName("recomputeButton")
        self.gridLayout_2.addWidget(self.recomputeButton, 14, 10, 1, 2)
        self.toleranceLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(False)
        font.setWeight(50)
        self.toleranceLabel.setFont(font)
        self.toleranceLabel.setObjectName("toleranceLabel")
        self.gridLayout_2.addWidget(self.toleranceLabel, 10, 10, 1, 1)
        self.specialValueValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(False)
        font.setWeight(50)
        self.specialValueValue.setFont(font)
        self.specialValueValue.setObjectName("specialValueValue")
        self.gridLayout_2.addWidget(self.specialValueValue, 11, 11, 1, 1)
        self.toleranceValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(False)
        font.setWeight(50)
        self.toleranceValue.setFont(font)
        self.toleranceValue.setObjectName("toleranceValue")
        self.gridLayout_2.addWidget(self.toleranceValue, 10, 11, 1, 1)
        self.auditDetailsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.auditDetailsLabel.setFont(font)
        self.auditDetailsLabel.setAutoFillBackground(True)
        self.auditDetailsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.auditDetailsLabel.setObjectName("auditDetailsLabel")
        self.gridLayout_2.addWidget(self.auditDetailsLabel, 8, 10, 1, 1)
        self.specialValueLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(False)
        font.setWeight(50)
        self.specialValueLabel.setFont(font)
        self.specialValueLabel.setObjectName("specialValueLabel")
        self.gridLayout_2.addWidget(self.specialValueLabel, 11, 10, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 6, 10, 1, 2)
        self.actualValueComboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.small_font_size)
        font.setBold(False)
        font.setWeight(50)
        self.actualValueComboBox_2.setFont(font)
        self.actualValueComboBox_2.setMaxVisibleItems(5)
        self.actualValueComboBox_2.setMaxCount(20)
        self.actualValueComboBox_2.setMinimumContentsLength(1)
        self.actualValueComboBox_2.setObjectName("actualValueComboBox_2")
        self.gridLayout_2.addWidget(self.actualValueComboBox_2, 9, 11, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 9, 10, 1, 1)
        self.tLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.large_font_size)
        self.tLabel.setFont(font)
        self.tLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.tLabel.setIndent(0)
        self.tLabel.setObjectName("tLabel")
        self.gridLayout_2.addWidget(self.tLabel, 3, 10, 1, 1)
        self.auditSpecialValuesTable = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.large_font_size)
        self.tValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.large_font_size)
        self.tValue.setFont(font)
        self.tValue.setIndent(0)
        self.tValue.setObjectName("tValue")
        self.gridLayout_2.addWidget(self.tValue, 3, 11, 1, 1)

        fontSpecialTable = QtGui.QFont()
        fontSpecialTable.setFamily("Calibri")
        fontSpecialTable.setPointSize(UI.UIUtils.small_font_size)
        self.auditSpecialValuesTable.setFont(fontSpecialTable)
        self.auditSpecialValuesTable.setShowGrid(False)
        self.auditSpecialValuesTable.setRowCount(0)
        self.auditSpecialValuesTable.setColumnCount(2)
        self.auditSpecialValuesTable.setObjectName("auditSpecialValuesTable")
        self.auditSpecialValuesTable.horizontalHeader().setVisible(False)
        self.auditSpecialValuesTable.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.auditSpecialValuesTable, 11, 10, 3, 2)
        self.auditSpecialValuesTable.raise_()
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.large_font_size)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 4, 2, 3)
        self.contestantTable = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.small_font_size)
        self.contestantTable.setFont(font)
        self.contestantTable.setRowCount(10)
        self.contestantTable.setColumnCount(2)
        self.contestantTable.setObjectName("contestantTable")
        self.contestantTable.horizontalHeader().setVisible(False)
        self.contestantTable.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.contestantTable, 4, 4, 2, 2)
        self.contestantsSubSectionLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contestantsSubSectionLabel.sizePolicy().hasHeightForWidth())
        self.contestantsSubSectionLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.contestantsSubSectionLabel.setFont(font)
        self.contestantsSubSectionLabel.setAutoFillBackground(False)
        self.contestantsSubSectionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.contestantsSubSectionLabel.setObjectName("contestantsSubSectionLabel")
        self.gridLayout_2.addWidget(self.contestantsSubSectionLabel, 3, 4, 1, 2)
        self.justSaveButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.small_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.justSaveButton.setFont(font)
        self.justSaveButton.setObjectName("justSaveButton")
        self.gridLayout_2.addWidget(self.justSaveButton, 15, 4, 1, 1)
        self.saveAndNextButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.small_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.saveAndNextButton.setFont(font)
        self.saveAndNextButton.setObjectName("saveAndNextButton")
        self.gridLayout_2.addWidget(self.saveAndNextButton, 15, 5, 1, 1)
        self.reportedValueComboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.small_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.reportedValueComboBox.setFont(font)
        self.reportedValueComboBox.setObjectName("reportedValueComboBox")
        self.reportedValueComboBox.addItem("")
        self.reportedValueComboBox.addItem("")
        self.reportedValueComboBox.addItem("")
        self.reportedValueComboBox.addItem("")
        self.reportedValueComboBox.addItem("")
        self.gridLayout_2.addWidget(self.reportedValueComboBox, 14, 4, 1, 1)
        self.actualValueComboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.small_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.actualValueComboBox.setFont(font)
        self.actualValueComboBox.setMaxVisibleItems(6)
        self.actualValueComboBox.setMaxCount(20)
        self.actualValueComboBox.setMinimumContentsLength(1)
        self.actualValueComboBox.setObjectName("actualValueComboBox")
        self.actualValueComboBox.addItem("")
        self.actualValueComboBox.addItem("")
        self.actualValueComboBox.addItem("")
        self.actualValueComboBox.addItem("")
        self.actualValueComboBox.addItem("")
        self.gridLayout_2.addWidget(self.actualValueComboBox, 14, 5, 1, 1)
        self.reportedValueLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.small_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.reportedValueLabel.setFont(font)
        self.reportedValueLabel.setObjectName("reportedValueLabel")
        self.gridLayout_2.addWidget(self.reportedValueLabel, 13, 4, 1, 1)
        self.actualValueLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.small_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.actualValueLabel.setFont(font)
        self.actualValueLabel.setObjectName("actualValueLabel")
        self.gridLayout_2.addWidget(self.actualValueLabel, 13, 5, 1, 1)
        self.auditedBallotLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.small_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.auditedBallotLabel.setFont(font)
        self.auditedBallotLabel.setObjectName("auditedBallotLabel")
        self.gridLayout_2.addWidget(self.auditedBallotLabel, 12, 4, 1, 1)
        self.auditedBallotValue = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.small_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.auditedBallotValue.setFont(font)
        self.auditedBallotValue.setObjectName("auditedBallotValue")
        self.gridLayout_2.addWidget(self.auditedBallotValue, 12, 5, 1, 1)
        self.currentBallotLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.medium_font_size)
        font.setBold(True)
        font.setWeight(75)
        self.currentBallotLabel.setFont(font)
        self.currentBallotLabel.setAutoFillBackground(True)
        self.currentBallotLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentBallotLabel.setObjectName("currentBallotLabel")
        self.gridLayout_2.addWidget(self.currentBallotLabel, 11, 4, 1, 1)
        self.reportedResultsTable = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(UI.UIUtils.small_font_size)
        self.reportedResultsTable.setFont(font)
        self.reportedResultsTable.setRowCount(5)
        self.reportedResultsTable.setColumnCount(2)
        self.reportedResultsTable.setObjectName("reportedResultsTable")
        self.reportedResultsTable.horizontalHeader().setVisible(False)
        self.reportedResultsTable.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.reportedResultsTable, 8, 4, 3, 2)
        self.auditTable.raise_()
        self.mainPageSectionLabel.raise_()
        self.electionDetailsSectionLabel.raise_()
        self.label_4.raise_()
        self.line_5.raise_()
        self.pushButton.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.exportButton.raise_()
        self.recomputeButton.raise_()
        self.specialValueLabel.raise_()
        self.specialValueValue.raise_()
        self.toleranceValue.raise_()
        self.toleranceLabel.raise_()
        self.label_5.raise_()
        self.actualValueComboBox_2.raise_()
        self.auditDetailsLabel.raise_()
        self.line_3.raise_()
        self.tLabel.raise_()
        self.tValue.raise_()
        self.statusLabel.raise_()
        self.contestantsSubSectionLabel.raise_()
        self.contestantTable.raise_()
        self.reportedResultsTable.raise_()
        self.justSaveButton.raise_()
        self.saveAndNextButton.raise_()
        self.reportedValueComboBox.raise_()
        self.actualValueComboBox.raise_()
        self.reportedValueLabel.raise_()
        self.actualValueLabel.raise_()
        self.auditedBallotLabel.raise_()
        self.auditedBallotValue.raise_()
        self.currentBallotLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.auditSpecialValuesTable.raise_()

        self.retranslateUi(MainWindow)
        self.reportedValueComboBox.setCurrentIndex(0)
        self.actualValueComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        header = self.auditTable.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        headerAuditSpecialValuesTable = self.auditSpecialValuesTable.horizontalHeader()
        headerAuditSpecialValuesTable.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        headerAuditSpecialValuesTable.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)


        # headerAuditSpecialValuesTableVertical = self.auditSpecialValuesTable.verticalHeader()
        # headerAuditSpecialValuesTableVertical.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        # headerAuditSpecialValuesTableVertical.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.auditSpecialValuesTable.verticalScrollBar().setDisabled(True)

       # self.auditSpecialValuesTable.resizeRowsToContents()


        headerContestantTable = self.contestantTable.horizontalHeader()
        headerContestantTable.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        headerReportedResultsTable = self.reportedResultsTable.horizontalHeader()
        headerReportedResultsTable.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        headerReportedResultsTable.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.contestantTable.setShowGrid(False)
        self.reportedResultsTable.setShowGrid(False)
        self.auditTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.contestantTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.reportedResultsTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.auditTable.clicked.connect(self.setCurrentBallotInformation)

        self.recomputeButton.clicked.connect(self.recompute_audit)
        self.justSaveButton.clicked.connect(self.save_ballot)
        self.saveAndNextButton.clicked.connect(self.save_and_add_ballot)
        self.actualValueComboBox_2.currentIndexChanged.connect(self.modify_UI_listener)


    def retranslateUi_backup(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.auditTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Audit #"))
        item = self.auditTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Actual Ballot #"))
        item = self.auditTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Reported Value"))
        item = self.auditTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Actual Value"))
        self.recomputeButton.setText(_translate("MainWindow", "Recompute"))
        self.pushButton.setText(_translate("MainWindow", "Edit Election"))
        self.exportButton.setText(_translate("MainWindow", "Export Results"))
        self.mainPageSectionLabel.setText(_translate("MainWindow", "RI WAVE - AUDIT"))
        self.statusLabel.setText(_translate("MainWindow", "Status: OK"))
        self.electionDetailsSectionLabel.setText(_translate("MainWindow", "Election Details"))
        self.specialValueValue.setText(_translate("MainWindow", "0.1"))
        self.toleranceValue.setText(_translate("MainWindow", "10%"))
        self.auditDetailsLabel.setText(_translate("MainWindow", "Audit Details"))
        self.specialValueLabel.setText(_translate("MainWindow", "Risk-limit:"))
        self.actualValueComboBox_2.setCurrentText(_translate("MainWindow", "Risk-limiting"))
        self.actualValueComboBox_2.setItemText(0, _translate("MainWindow", "Risk-limiting"))
        self.actualValueComboBox_2.setItemText(1, _translate("MainWindow", "Bayesian"))
        self.label_5.setText(_translate("MainWindow", "Type:"))
        self.tLabel.setText(_translate("MainWindow", "T= "))
        self.tValue.setText(_translate("MainWindow", "8.99"))
        self.label_4.setText(_translate("MainWindow", "Reported Results"))
        self.contestantsSubSectionLabel.setText(_translate("MainWindow", "Contestants:"))
        self.justSaveButton.setText(_translate("MainWindow", "Save Changes"))
        self.saveAndNextButton.setText(_translate("MainWindow", "Save and Continue"))
        self.reportedValueComboBox.setCurrentText(_translate("MainWindow", "Select Candidate"))
        self.reportedValueComboBox.setItemText(0, _translate("MainWindow", "Select Candidate"))
        self.reportedValueComboBox.setItemText(1, _translate("MainWindow", "Trump"))
        self.reportedValueComboBox.setItemText(2, _translate("MainWindow", "Clinton"))
        self.reportedValueComboBox.setItemText(3, _translate("MainWindow", "Johnson"))
        self.reportedValueComboBox.setItemText(4, _translate("MainWindow", "Stein"))
        self.actualValueComboBox.setCurrentText(_translate("MainWindow", "Select Candidate"))
        self.actualValueComboBox.setItemText(0, _translate("MainWindow", "Select Candidate"))
        self.actualValueComboBox.setItemText(1, _translate("MainWindow", "Trump"))
        self.actualValueComboBox.setItemText(2, _translate("MainWindow", "Clinton"))
        self.actualValueComboBox.setItemText(3, _translate("MainWindow", "Johnson"))
        self.actualValueComboBox.setItemText(4, _translate("MainWindow", "Stein"))
        self.reportedValueLabel.setText(_translate("MainWindow", "Reported Value"))
        self.actualValueLabel.setText(_translate("MainWindow", "Actual Value"))
        self.auditedBallotLabel.setText(_translate("MainWindow", "Audited Ballot #"))
        self.auditedBallotValue.setText(_translate("MainWindow", "1"))
        self.currentBallotLabel.setText(_translate("MainWindow", "Current Ballot"))

    def getSpecialValueLabel(self):
        return self.specialValueLabel;

    def getAuditTable(self):
        return self.auditTable;

    def getCandidateGridLayout(self):
        return self.gridLayout;

    def getCandidateNameReportedResultsVeriticalLayout(self):
        return self.verticalLayout;

    def getCandidateValueReportedResultsVerticalLayout(self):
        return self.gridLayout_2;

    def getAuditedBallotValue(self):
        return self.auditedBallotValue;

    def getBallotReportedValueName(self):
        return self.reportedValueName;

    def getBallotActualValueComboBox(self):
        return self.actualValueComboBox;

    def getBallotActualValueComboBoxIndex(self):
        return self.actualValueComboBox.currentIndex();

    def getEditElectionButton(self):
        return self.pushButton;

    def getJustSaveChangesButton(self):
        return self.justSaveButton;

    def getSaveChangesAndContinueButton(self):
        return self.saveAndNextButton;

    def getRecomputeButton(self):
        return self.recomputeButton;

    def getExportResultsButton(self):
        return self.exportButton;

    def getToleranceLabel(self):
        return self.toleranceLabel;

    def getToleranceValueLabel(self):
        return self.toleranceValue;

    def getSpecialValueLabel(self):
        return self.specialValueLabel;

    def getSpecialValueValue(self):
        return self.specialValueValue;

    def getAuditTypeComboBox(self):
        return self.actualValueComboBox_2;

    def getAuditTypeComboBoxSelectedIndex(self):
        return str(self.actualValueComboBox_2.currentIndex());

    def getStatusLabel(self):
        return self.statusLabel;

    def setProgressValueLabel(self, newValue):
        self.tLabel.setText(newValue)

    def setProgressValue(self,newValue):
        self.tValue.setText(newValue)

    def setProgressLabel(self, newValue):
        self.statusLabel.setText(newValue)

    # def getTValueValueLabel(self):
    #     return self.tValue;

    # def getTLabelLabel(self):
    #     return self.tLabel;
    #TODO: Change this to get the actual audit type, the return value is a placeholder
    def get_audit_type(self):
        return self.getAuditTypeComboBox().currentIndex()

    def setTableCell(self, row, col, value):
        self.auditTable.setItem(row, col, QtWidgets.QTableWidgetItem(value))

    def setAuditTableCell(self, row, col, value):
        self.auditTable.setItem(row, col, QtWidgets.QTableWidgetItem(value))

    def setReportedResultsTableCell(self, row, col, value):
        self.reportedResultsTable.setItem(row, col, QtWidgets.QTableWidgetItem(value))

    def setContestantTableCell(self, row, col, value):
        self.contestantTable.setItem(row, col, QtWidgets.QTableWidgetItem(value))

    def getCurrentlySelectedAuditTableRow(self, tableItem):
        self.auditTable.setItem(1, 1, QtWidgets.QTableWidgetItem(tableItem))
        return tableItem.currentRow()

    def setAuditSpecialValueTableCell(self,row,col, value):
        self.auditSpecialValuesTable.setItem(row, col, QtWidgets.QTableWidgetItem(value))

    def getCurrentAuditIndex(self, current_audit):
        audit_index = 0

        for i, audit in enumerate(self._audits):
            if isinstance(current_audit, audit):
                audit_index = i

        return audit_index

    def setCurrentBallotInformation(self, tableItem):
        self._current_ballot = list(filter(lambda b: b.get_audit_seq_num() == self.auditTable.currentRow(),
                                           self._election.get_ballots()))[0]

        self.auditedBallotValue.setText(str(self.auditTable.currentRow()))

        reportedValueName = self.auditTable.item(self.auditTable.currentRow(), 2).text()
        index = self.reportedValueComboBox.findText(str(reportedValueName)) #findText(str(name))
        self.reportedValueComboBox.setCurrentIndex(index)

        actualValueName = self.auditTable.item(self.auditTable.currentRow(), 3).text()

        if not actualValueName:
            print("VALUE IS NULL")
        else:
            actualValueIndex = self.reportedValueComboBox.findText(str(actualValueName))  # findText(str(name))
            self.actualValueComboBox.setCurrentIndex(actualValueIndex)

    def save_ballot(self):
        if self._current_ballot is None:
            return

        reported_value_text = self.reportedValueComboBox.currentText()
        actual_value_text = self.actualValueComboBox.currentText()

        if reported_value_text == "Select Candidate" or actual_value_text == "Select Candidate":
            return

        reported_value = list(filter(lambda x: x.get_name() == reported_value_text, self._election.get_contestants()))[0]
        actual_value = list(filter(lambda x: x.get_name() == actual_value_text, self._election.get_contestants()))[0]

        self._current_ballot.set_reported_value(reported_value)
        self._current_ballot.set_actual_value(actual_value)
        self.audited_ballots[self._current_ballot.get_audit_seq_num()].set_actual_value(actual_value)
        self.audited_ballots[self._current_ballot.get_audit_seq_num()].set_reported_value(reported_value)



        self.reload_audit_table()
        self._audit.recompute(self.audited_ballots, self._election.get_reported_results())
        self.recompute_and_highlight()
        self.refresh_audit_status()

    def save_and_add_ballot(self):
        self.choose_next_ballot()
        if not self.auditedBallotValue.text().isdigit():
            pass
        elif int(self.auditedBallotValue.text()) >= self.auditTable.rowCount():
            audit_seq = int(self.auditedBallotValue.text())

            reported_value_text = self.reportedValueComboBox.currentText()
            actual_value_text = self.actualValueComboBox.currentText()

            print("Reported Value Text")
            print(reported_value_text)
            print("Actual Value Text")
            print(actual_value_text)

            if reported_value_text == "Select Candidate" or actual_value_text == "Select Candidate":
                return

            reported_value = list(filter(lambda x: x.get_name() == reported_value_text,
                                         self._election.get_contestants()))[0]

            actual_value = list(filter(lambda x: x.get_name() == actual_value_text,
                                       self._election.get_contestants()))[0]

            # TODO: FIX THIS JANK
            physical_seq = -1

            ballot = election.Ballot()
            ballot.set_audit_seq_num(audit_seq)
            ballot.set_physical_ballot_num(physical_seq)
            ballot.set_reported_value(reported_value)
            ballot.set_actual_value(actual_value)

            self._election.add_ballot(ballot)
            self.reload_audit_table()
            #self._audit.recompute(self._election.get_ballots(), self._election.get_reported_results())
            # self._audit.recompute(self.audited_ballots, self._election.get_reported_results())
            # self.refresh_audit_status()
        else:
            self.save_ballot()
        #TODO: IS IT OK TO RECOMPUTE AFTER JUST CLICKING THE BUTTON WITHOUT HAVING TO MESS WITH THE VALUES?
        self._audit.recompute(self.audited_ballots, self._election.get_reported_results())
        self.refresh_audit_status()
        self.auditedBallotValue.setText(str(self.auditTable.rowCount()))
        self.reportedValueComboBox.setCurrentIndex(0)
        self.actualValueComboBox.setCurrentIndex(0)

    def reload_audit_table(self):
        _translate = QtCore.QCoreApplication.translate

        self.auditTable.setRowCount(0)

        # Table Setup
        self.auditTable.horizontalHeaderItem(Ui_MainWindow.TableNum.AUDIT_NUM).setText(
            _translate("MainWindow", "Audit #"))
        self.auditTable.horizontalHeaderItem(Ui_MainWindow.TableNum.BALLOT_NUM).setText(
            _translate("MainWindow", "Actual Ballot #"))
        self.auditTable.horizontalHeaderItem(Ui_MainWindow.TableNum.REPORTED_VALUE).setText(
            _translate("MainWindow", "Reported Value"))
        self.auditTable.horizontalHeaderItem(Ui_MainWindow.TableNum.ACTUAL_VALUE).setText(
            _translate("MainWindow", "Actual Value"))

        # for i, ballot in enumerate(sorted(self._election.get_ballots(), key=lambda x: x.get_audit_seq_num())):
        for i in range(0, self.current_audit_ballot):#ballot in self.audited_ballots:
            self.auditTable.insertRow(i)
            ballot = self.audited_ballot_nums[i]
            print ("BALLOT NUM: " + str(ballot))
            self.setTableCell(i, Ui_MainWindow.TableNum.AUDIT_NUM, str(i))
            self.setTableCell(i, Ui_MainWindow.TableNum.BALLOT_NUM, str(self.audited_ballots[i].get_physical_ballot_num()))
            #self.setTableCell(i, Ui_MainWindow.TableNum.BALLOT_NUM, str(self.audited_ballots[i].get_physical_ballot_num()))
            self.setTableCell(i, Ui_MainWindow.TableNum.REPORTED_VALUE, self.audited_ballots[i].get_reported_value().get_name())
            self.setTableCell(i, Ui_MainWindow.TableNum.ACTUAL_VALUE, self.audited_ballots[i].get_actual_value().get_name())



    def choose_next_ballot(self):
        if(self.total_rows == 0):
            self.set_csv_total_rows(self.filename)
       # next_ballot = round(random.random() * self.total_rows*10) % self.total_rows
        next_ballot = random.randint(2, self.total_rows)
        print(next_ballot)
        self.auditTable.insertRow(self.current_audit_ballot)
        if self._election.get_ballots is None:
            print("NULL")
        # else:
        #     print(len(self._election.get_ballots))
        ballot = self._election.get_ballot(next_ballot-2)
        ballot.set_audit_seq_num(self.current_audit_ballot)
        self.audited_ballots.append(ballot)

        self.audited_ballot_nums.append(ballot.get_physical_ballot_num())

        self.current_audit_ballot = self.current_audit_ballot + 1
        self.reload_audit_table()

    def set_csv_total_rows(self, filename):
        input_file = open(filename, "r+")
        reader_file = csv.reader(input_file)
        self.total_rows = len(list(reader_file))
        random.seed(self.seed)

    def recompute_audit(self):
        self.reload_audit_table()
        param = []

        for i in range(self.auditSpecialValuesTable.rowCount()):
            param.append(self.auditSpecialValuesTable.item(i, 1).text())

        self._audit.set_parameters(param)

        if self._audit.get_name() != self.getAuditTypeComboBox().currentText():
            self._audit = self._audits[int(self.getAuditTypeComboBoxSelectedIndex())]()
            self._audit.init(self._election.get_reported_results(),
                    self._election.get_ballot_count())

            self.refresh_parameters()

        else:
            self._audit.set_parameters(param)
            self.recompute_and_highlight()
            self.refresh_audit_status()

    def recompute_and_highlight(self):
        stopped_ballot = self._audit.recompute(self.audited_ballots, 
            self._election.get_reported_results())
        
        if stopped_ballot is not None and stopped_ballot.get_audit_seq_num() <= self.auditTable.rowCount():
            for i in range(self.auditTable.columnCount()):
                self.auditTable.item(stopped_ballot.get_audit_seq_num(), i).setBackground(
                        QtGui.QColor(255, 154, 0))

    def refresh_parameters(self):
        self.auditSpecialValuesTable.setRowCount(0)

        for i, param in enumerate(self._audit.get_parameters()):
            self.auditSpecialValuesTable.insertRow(i)

            self.setAuditSpecialValueTableCell(i, 0, param[0])
            self.setAuditSpecialValueTableCell(i, 1, param[1])

    def refresh_audit_status(self):
        if self._audit is not None:
            self.setProgressValueLabel(self._audit.get_progress())
            self.setProgressLabel(self._audit.get_status())
        else:
            self.setProgressValueLabel("Please Select")
            self.setProgressLabel("an audit")

    def retranslateUi(self, MainWindow):
        # Generate the Basic Window
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", 
                                             "MainWindow"))
        self.mainPageSectionLabel.setText(_translate("MainWindow", "RI WAVE - AUDIT"))

        # Setup audit table
        self.reload_audit_table()

        # Edit Election
        self.pushButton.setText(_translate("MainWindow", "Edit Election"))

        # Election Details
        self.electionDetailsSectionLabel.setText(_translate("MainWindow", "Election Details"))

        # Contestant Selection
        self.contestantsSubSectionLabel.setText(_translate("MainWindow", "Contestants:"))

        for i, candidate in enumerate(self._election.get_contestants()):
            self.setContestantTableCell(i, 0, str(candidate.get_id()))
            self.setContestantTableCell(i, 1, candidate.get_name())

        self.label_4.setText(_translate("MainWindow", "Reported Results"))

        for i, result in enumerate(sorted(self._election.get_reported_results(),
                                          key=lambda x: x.get_percentage(),
                                          reverse=True)):
            self.setReportedResultsTableCell(i, 0, result.get_contestant().get_name())
            self.setReportedResultsTableCell(i, 1, "%.1f" % (result.get_percentage() * 100) + "%")

        # Current Ballot
        # === Current Ballot Info
        self.auditedBallotValue.setText(_translate("MainWindow", ""))

        self.currentBallotLabel.setText(_translate("MainWindow", "Current Ballot"))
        self.auditedBallotLabel.setText(_translate("MainWindow", "Audited Ballot #"))

        self.actualValueLabel.setText(_translate("MainWindow", "Actual Value"))
        self.actualValueComboBox.setItemText(0, _translate("MainWindow", "Select Candidate"))

        self.reportedValueLabel.setText(_translate("MainWindow", "Reported Value"))
        self.reportedValueComboBox.setItemText(0, _translate("MainWindow", "Select Candidate"))

        if self._current_ballot is not None:
            self.auditedBallotValue.setText(_translate("MainWindow", self._current_ballot.get_audit_seq_num()))

            self.actualValueComboBox.setCurrentText(
                _translate("MainWindow", self._current_ballot.get_actual_value().get_name()))
            self.reportedValueComboBox.setCurrentText(
                _translate("MainWindow", self._current_ballot.get_reported_value().get_name()))
        else:
            self.auditedBallotValue.setText(_translate("MainWindow", " "))

            self.actualValueComboBox.setCurrentText(_translate("MainWindow", "Select Candidate"))
            self.reportedValueComboBox.setCurrentText(_translate("MainWindow", "Select Candidate"))

        for i, candidate in enumerate(self._election.get_contestants()):
            self.actualValueComboBox.setItemText(i + 1, _translate("MainWindow", candidate.get_name()))
            self.reportedValueComboBox.setItemText(i + 1, _translate("MainWindow", candidate.get_name()))

        # ==== Save Buttons

        self.justSaveButton.setText(_translate("MainWindow", "Save Changes"))
        self.saveAndNextButton.setText(_translate("MainWindow", "Save and Continue"))

        # Audit Status
        # Populate audit selector dropdown
        for i, current_audit in enumerate(self._audits):
            self.actualValueComboBox_2.addItem(current_audit.get_name())

        if self._audit is not None:
            # Set the audit selector drop down to the current audit
            self.actualValueComboBox_2.setCurrentIndex(self.getCurrentAuditIndex(self._audit))

            # Populate audit parameters
            self.refresh_parameters()

        else:
            # Set the audit selector drop down to "Select Audit"
            self.actualValueComboBox_2.setCurrentIndex(0)

            # Reset audit parameters
            self.auditSpecialValuesTable.setRowCount(0)

        # Audit status
        self.refresh_audit_status()

        # Audit details
        self.auditDetailsLabel.setText(_translate("MainWindow", "Audit Details"))

        # Audit option buttons
        # self.tLabel.setText(_translate("MainWindow", "Progress Value: "))
        # self.statusLabel.setText(_translate("MainWindow", "Status: Keep Going"))
        # self.tValue.setText(_translate("MainWindow", "0.0"))
        self.recomputeButton.setText(_translate("MainWindow", "Recompute"))
        self.exportButton.setText(_translate("MainWindow", "Export Results"))
        self.choose_next_ballot()
        if (self.get_audit_type() == 1):
            self.set_bprla_UI()
        elif (self.get_audit_type() == 2):
            self.set_comp_rla_UI()


    def set_bprla_UI(self):
        self.auditTable.setColumnHidden(2, True)
        self.reportedValueComboBox.setDisabled(True)
        # self.reportedValueComboBox.setHidden(True)
        # self.reportedValueLabel.setHidden(True)
        # self.actualValueComboBox.setMaximumWidth()

        #self.gridLayout_2.addWidget(self.actualValueLabel, 13, 5, 1, 1)

    def set_comp_rla_UI(self):
        self.auditTable.setColumnHidden(2, False)
        self.reportedValueComboBox.setDisabled(False)

    def modify_UI_listener(self):
        if (self.get_audit_type() == 1):
            self.set_bprla_UI()
        elif (self.get_audit_type() == 2):
            self.set_comp_rla_UI()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

