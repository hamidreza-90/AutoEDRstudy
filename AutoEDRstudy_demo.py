# Economic Development Request Study
# Developed by: Hamidreza Sadeghian
# August 2019

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import multiprocessing as mp
#from AutoEDRstudy_main import main, get_bus_data, get_brn_data, get_nontrans_brn_data
#from Test_input import main_test
import subprocess
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # MainWindow.setObjectName("Economic Development Request Study")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 676)
        MainWindow.setWindowIcon(QtGui.QIcon('DVP_logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_caseStudy = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_caseStudy.setGeometry(QtCore.QRect(10, 120, 75, 24))
        self.pushButton_caseStudy.setObjectName("pushButton_caseStudy")
        self.lineEdit_studycase = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_studycase.setGeometry(QtCore.QRect(100, 120, 301, 20))
        self.lineEdit_studycase.setObjectName("lineEdit_studycase")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 148, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_bus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bus.setGeometry(QtCore.QRect(10, 170, 75, 24))
        self.pushButton_bus.setObjectName("pushButton_bus")
        self.lineEdit_bus = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_bus.setGeometry(QtCore.QRect(100, 172, 301, 20))
        self.lineEdit_bus.setObjectName("lineEdit_bus")
        self.pushButton_line = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_line.setGeometry(QtCore.QRect(10, 200, 75, 24))
        self.pushButton_line.setObjectName("pushButton_line")
        self.lineEdit_LineFB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_LineFB.setGeometry(QtCore.QRect(100, 202, 301, 20))
        self.lineEdit_LineFB.setObjectName("lineEdit_LineFB")
        self.pushButton_single = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_single.setGeometry(QtCore.QRect(10, 230, 75, 24))
        self.pushButton_single.setObjectName("pushButton_single")
        self.lineEdit_Single = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Single.setGeometry(QtCore.QRect(100, 232, 301, 20))
        self.lineEdit_Single.setObjectName("lineEdit_Single")
        self.pushButton_tower = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_tower.setGeometry(QtCore.QRect(10, 260, 75, 24))
        self.pushButton_tower.setObjectName("pushButton_tower")
        self.lineEdit_Tower = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Tower.setGeometry(QtCore.QRect(100, 262, 301, 20))
        self.lineEdit_Tower.setObjectName("lineEdit_Tower")

        self.checkbox_addCon = QCheckBox("   Add single branch contingency (target zone).", self.centralwidget)
        self.checkbox_addCon.setGeometry(QtCore.QRect(67, 275, 300, 43))
        self.checkbox_addCon.setDisabled(False)
        self.checkbox_addCon.setChecked(True)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 120, 91, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 310, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox_StudySize = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_StudySize.setGeometry(QtCore.QRect(560, 150, 121, 22))
        self.comboBox_StudySize.setObjectName("comboBox_StudySize")
        self.comboBox_StudySize.addItems(["Area","Zone","Single Branch"])
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(440, 150, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_55 = QtWidgets.QLabel(self.centralwidget)
        self.label_55.setGeometry(QtCore.QRect(720, 150, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")

        self.lineEdit_precision = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_precision.setGeometry(QtCore.QRect(801, 150, 31, 20))
        self.lineEdit_precision.setText("5")
        self.lineEdit_precision.setObjectName("lineEdit_precision")
        self.label_199 = QtWidgets.QLabel(self.centralwidget)
        self.label_199.setGeometry(QtCore.QRect(838, 150, 111, 20))
        self.label_199.setObjectName("label_199")



        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 180, 81, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_AreNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_AreNumber.setGeometry(QtCore.QRect(583, 180, 61, 20))
        self.lineEdit_AreNumber.setObjectName("lineEdit_AreNumber")
        self.lineEdit_AreNumber.setText("")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(660, 180, 81, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_ZoneNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ZoneNumber.setGeometry(QtCore.QRect(743, 180, 61, 20))
        self.lineEdit_ZoneNumber.setText("")
        self.lineEdit_ZoneNumber.setObjectName("lineEdit_ZoneNumber")
        self.lineEdit_ToBus = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ToBus.setGeometry(QtCore.QRect(743, 210, 61, 20))
        self.lineEdit_ToBus.setText("")
        self.lineEdit_ToBus.setObjectName("lineEdit_ToBus")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(500, 210, 71, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_FromBus = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_FromBus.setGeometry(QtCore.QRect(583, 210, 61, 20))
        self.lineEdit_FromBus.setObjectName("lineEdit_FromBus")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(660, 210, 71, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(820, 210, 21, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ID.setGeometry(QtCore.QRect(840, 210, 21, 20))
        self.lineEdit_ID.setText("")
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(440, 240, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(580, 240, 211, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setTickInterval(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(50)
        self.lineEdit_BusLocationPercent = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_BusLocationPercent.setGeometry(QtCore.QRect(820, 240, 41, 20))
        self.lineEdit_BusLocationPercent.setText("")
        self.lineEdit_BusLocationPercent.setObjectName("lineEdit_BusLocationPercent")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(440, 270, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.comboBox_studyViolations = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_studyViolations.setGeometry(QtCore.QRect(560, 270, 155, 22))
        self.comboBox_studyViolations.setObjectName("comboBox_studyViolations")
        # self.comboBox_studyViolations.addItems(["Thermal & Voltage With Fiction Switched Shunts", "Thermal & Voltage Without Fiction Switched Shunts", "Thermal Violation"])
        self.comboBox_studyViolations.addItems(["Thermal Only", "Thermal & Voltage"])
        self.checkbox_violatio = QCheckBox("   Convert Fixed to \nSwitched Capacitors", self.centralwidget)
        self.checkbox_violatio.setGeometry(QtCore.QRect(722, 260, 200, 43))
        self.checkbox_violatio.setDisabled(True)
        self.checkbox_violatio.setChecked(False)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 600, 861, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.comboBox_solutionMethod = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_solutionMethod.setGeometry(QtCore.QRect(140, 330, 150, 22))
        self.comboBox_solutionMethod.setObjectName("comboBox_solutionMethod")
        self.comboBox_solutionMethod.addItems(["Fixed slope decoupled N-R", "Full N-R", "Decoupled N-R"])
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 330, 121, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(330, 330, 111, 20))
        self.label_14.setObjectName("label_14")
        self.comboBox_tapAdjustments = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_tapAdjustments.setGeometry(QtCore.QRect(450, 330, 150, 22))
        self.comboBox_tapAdjustments.setObjectName("comboBox_tapAdjustments")
        self.comboBox_tapAdjustments.addItems(["Lock taps", "Stepping", "Direct"])
        self.comboBox_shuntAdjustment = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_shuntAdjustment.setGeometry(QtCore.QRect(140, 360, 150, 22))
        self.comboBox_shuntAdjustment.setObjectName("comboBox_shuntAdjustment")
        self.comboBox_shuntAdjustment.addItems(["Enable all","Lock all", "Continuous"])
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 360, 121, 20))
        self.label_15.setObjectName("label_15")
        self.comboBox_areaInterchange = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_areaInterchange.setGeometry(QtCore.QRect(450, 360, 150, 22))
        self.comboBox_areaInterchange.setObjectName("comboBox_areaInterchange")
        self.comboBox_areaInterchange.addItems(["Disabled", "Ties only", "Tie lines and loads"])
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(330, 360, 111, 20))
        self.label_16.setObjectName("label_16")

        self.comboBox_varlimit = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_varlimit.setGeometry(QtCore.QRect(710, 330, 150, 22))
        self.comboBox_varlimit.setObjectName("comboBox_areaInterchange")
        self.comboBox_varlimit.addItems(["Apply immediately", "Apply automatically", "Ignore VAR limits"])
        self.label_166 = QtWidgets.QLabel(self.centralwidget)
        self.label_166.setGeometry(QtCore.QRect(640, 330, 111, 20))
        self.label_166.setObjectName("label_16")



        self.comboBox_baseRating = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_baseRating.setGeometry(QtCore.QRect(170, 410, 161, 22))
        self.comboBox_baseRating.setObjectName("comboBox_baseRating")
        self.comboBox_baseRating.addItems(["Rating A", "Rating B", "Rating C"])
        self.comboBox_countRating = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_countRating.setGeometry(QtCore.QRect(170, 440, 161, 22))
        self.comboBox_countRating.setObjectName("comboBox_countRating")
        self.comboBox_countRating.addItems(["Rating A", "Rating B", "Rating C"])
        self.comboBox_countRating.setCurrentText("Rating B")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(20, 440, 141, 20))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(20, 410, 111, 20))
        self.label_18.setObjectName("label_18")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 390, 221, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_baseRating = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_baseRating.setGeometry(QtCore.QRect(340, 410, 31, 20))
        self.lineEdit_baseRating.setText("100")
        self.lineEdit_baseRating.setObjectName("lineEdit_baseRating")
        self.lineEdit_contRating = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_contRating.setGeometry(QtCore.QRect(340, 440, 31, 20))
        self.lineEdit_contRating.setText("100")
        self.lineEdit_contRating.setObjectName("lineEdit_contRating")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(380, 410, 111, 20))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(380, 440, 111, 20))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(490, 440, 201, 20))
        self.label_21.setObjectName("label_21")
        self.comboBox_transThermalmode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_transThermalmode.setGeometry(QtCore.QRect(700, 440, 161, 22))
        self.comboBox_transThermalmode.setObjectName("comboBox_transThermalmode")
        self.comboBox_transThermalmode.addItems(["MVA rating", "AMP rating"])
        self.comboBox_lineThermalmode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_lineThermalmode.setGeometry(QtCore.QRect(700, 410, 161, 22))
        self.comboBox_lineThermalmode.setObjectName("comboBox_lineThermalmode")
        self.comboBox_lineThermalmode.addItems(["MVA rating", "AMP rating"])
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(490, 410, 171, 20))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(10, 470, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.comboBox_cores = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_cores.setGeometry(QtCore.QRect(170, 490, 161, 22))
        self.comboBox_cores.setObjectName("comboBox_cores")
        self.comboBox_cores.addItems(["CPU cores", "CPU cores - 1", "User input"])
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(20, 490, 111, 20))
        self.label_24.setObjectName("label_24")
        self.lineEdit_cores = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cores.setGeometry(QtCore.QRect(340, 490, 31, 20))
        self.lineEdit_cores.setText("")
        self.lineEdit_cores.setObjectName("lineEdit_cores")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(480, 470, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(510, 490, 91, 20))
        self.label_26.setObjectName("label_26")
        self.comboBox_contScenarios = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_contScenarios.setGeometry(QtCore.QRect(600, 490, 261, 22))
        self.comboBox_contScenarios.setObjectName("comboBox_contScenarios")
        self.comboBox_contScenarios.addItems(["N-1, N-2, and N-1-1", "N-1 and N-2", "Single"])
        self.lineEdit_outputFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_outputFile.setGeometry(QtCore.QRect(100, 550, 301, 20))
        self.lineEdit_outputFile.setText("")
        self.lineEdit_outputFile.setObjectName("lineEdit_outputFile")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(10, 526, 101, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")

        self.checkbox_saveEveryStep = QCheckBox("Report all simulation steps", self.centralwidget)
        self.checkbox_saveEveryStep.setGeometry(QtCore.QRect(10, 535, 200, 103))
        self.checkbox_saveEveryStep.setDisabled(False)
        self.checkbox_saveEveryStep.setChecked(True)

        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(10, 550, 75, 23))
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_run.setGeometry(QtCore.QRect(410, 530, 75, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_run.setFont(font)
        self.pushButton_run.setObjectName("pushButton_run")
        self.pushButton_initiateOptions = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_initiateOptions.setGeometry(QtCore.QRect(777, 530, 85, 61))
        font = QtGui.QFont()
        font.setPointSize(8.5)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_initiateOptions.setFont(font)
        self.pushButton_initiateOptions.setObjectName("pushButton_initiateOptions")
        self.comboBox_studyEngine = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_studyEngine.setGeometry(QtCore.QRect(560, 120, 231, 22))
        self.comboBox_studyEngine.setObjectName("comboBox_studyEngine")
        self.comboBox_studyEngine.addItems(['PSS/E 33  &  PowerGEM TARA', 'PSS/E 33 Only'])

        self.comboBox_startinload = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_startinload.setGeometry(QtCore.QRect(600, 532, 165, 22))
        self.comboBox_startinload.setObjectName("comboBox_startinload")
        self.comboBox_startinload.addItems(["Percent (Base Case)", "MW (User input)"])
        self.label_133 = QtWidgets.QLabel(self.centralwidget)
        self.label_133.setGeometry(QtCore.QRect(495, 532, 121, 20))
        self.label_133.setObjectName("label_133")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_133.setFont(font)
        self.label_133.setObjectName("label_27")

        self.lineEdit_percentStaartLoad = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_percentStaartLoad.setGeometry(QtCore.QRect(555, 565, 31, 20))
        self.lineEdit_percentStaartLoad.setText("110")
        self.lineEdit_percentStaartLoad.setObjectName("lineEdit_contRating")
        self.label_19pl = QtWidgets.QLabel(self.centralwidget)
        self.label_19pl.setGeometry(QtCore.QRect(590, 555, 211, 40))
        self.label_19pl.setObjectName("label_19pl")
        # self.lineEdit_mwStaartLoad = QtWidgets.QLineEdit(self.centralwidget)
        # self.lineEdit_mwStaartLoad.setGeometry(QtCore.QRect(547, 575, 31, 18))
        # self.lineEdit_mwStaartLoad.setText("")
        # self.lineEdit_mwStaartLoad.setObjectName("lineEdit_contRating")
        # self.label_19mw = QtWidgets.QLabel(self.centralwidget)
        # self.label_19mw.setGeometry(QtCore.QRect(580, 575, 211, 20))
        # self.label_19mw.setObjectName("label_19mw")




        self.label_logo_tara = QLabel(MainWindow)
        self.label_logo_tara.setPixmap(QPixmap("TARA_logo.png"))
        self.label_logo_tara.setGeometry(805, 142, 26, 26)
        self.label_logo_tara.setObjectName("TARA_logo")
        self.label_logo_psse = QLabel(MainWindow)
        self.label_logo_psse.setPixmap(QPixmap("psse_logo.png"))
        self.label_logo_psse.setGeometry(835, 142, 26, 26)
        self.label_logo_psse.setObjectName("TARA_logo")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.doc = self.menuFile.addAction("Documentation")
        self.doc.triggered.connect(self.openDoc)



        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHelp.addAction("Economic Development Request Study (v1)")
        self.menuHelp.addAction("@ ET Planning and Strategic Initiatives")
        self.menuHelp.addAction("Developed by: Hamidreza Sadeghian")
        self.menuHelp.addAction("August 2019")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuHelp.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.lineEdit_BusLocationPercent.setText(str(self.horizontalSlider.value())+"%")

        self.lineEdit_AreNumber.setDisabled(False)
        self.lineEdit_ZoneNumber.setDisabled(True)
        self.lineEdit_FromBus.setDisabled(True)
        self.lineEdit_ToBus.setDisabled(True)
        self.lineEdit_ID.setDisabled(True)


        self.label_logo = QLabel(MainWindow)
        self.label_logo.setPixmap(QPixmap("DVP_logo.png"))
        self.label_logo.setGeometry(15, 30, 240, 100)
        self.label_logo.setObjectName("Dominion_Energy_logo")

        self.label_TransmissionPlanning = QtWidgets.QLabel(MainWindow)
        self.label_TransmissionPlanning.setGeometry(QtCore.QRect(480, 40, 400, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_TransmissionPlanning.setFont(font)
        self.label_TransmissionPlanning.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_TransmissionPlanning.setObjectName("label_TransmissionPlanning")

        process_core = mp.cpu_count()
        self.lineEdit_cores.setText(str(process_core))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_caseStudy.clicked.connect(self.openFileNameDialog_case)
        self.pushButton_bus.clicked.connect(self.openFileNameDialog_bus)
        self.pushButton_line.clicked.connect(self.openFileNameDialog_line)
        self.pushButton_single.clicked.connect(self.openFileNameDialog_single)
        self.pushButton_tower.clicked.connect(self.openFileNameDialog_tower)
        self.pushButton_save.clicked.connect(self.saveFileDialog)
        self.comboBox_StudySize.currentTextChanged.connect(self.studySizeSelect)
        self.horizontalSlider.valueChanged.connect(self.sliderValue)
        self.pushButton_run.clicked.connect(self.runMain)
        self.comboBox_studyViolations.currentTextChanged.connect(self.violationStudy)
        self.comboBox_cores.currentTextChanged.connect(self.coreNumber)
        self.pushButton_initiateOptions.clicked.connect(self.initiateOptions)
        self.comboBox_studyEngine.currentTextChanged.connect(self.logoPics)
        self.comboBox_contScenarios.currentTextChanged.connect(self.countScenarios)
        self.comboBox_startinload.currentTextChanged.connect(self.startingLoad)


        # self.checkbox_violatio.clicked.connect(self.checkbox_violation)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoEDRstudy"))
        self.pushButton_caseStudy.setText(_translate("MainWindow", "Study Case"))
        self.label.setText(_translate("MainWindow", "Contingency Files:"))
        self.pushButton_bus.setText(_translate("MainWindow", "Bus"))
        self.pushButton_line.setText(_translate("MainWindow", "Line_FB"))
        self.pushButton_single.setText(_translate("MainWindow", "Single"))
        self.pushButton_tower.setText(_translate("MainWindow", "Tower"))
        self.label_2.setText(_translate("MainWindow", "Study Engine:"))
        self.label_3.setText(_translate("MainWindow", "Load Flow Solutions:"))
        self.label_5.setText(_translate("MainWindow", "Study Size:"))
        self.label_55.setText(_translate("MainWindow", "Precision:"))
        self.label_6.setText(_translate("MainWindow", "Area Number:"))
        self.label_7.setText(_translate("MainWindow", "Zone Number:"))
        self.label_8.setText(_translate("MainWindow", "From Bus:"))
        self.label_9.setText(_translate("MainWindow", "To Bus:"))
        self.label_10.setText(_translate("MainWindow", "ID:"))
        self.label_11.setText(_translate("MainWindow", "Bus Location (%):"))
        self.label_12.setText(_translate("MainWindow", "Study Violations:"))
        self.label_13.setText(_translate("MainWindow", "Solution method:"))
        self.label_133.setText(_translate("MainWindow", "Starting Load:"))
        self.label_14.setText(_translate("MainWindow", "Tap Adjustment:"))
        self.label_15.setText(_translate("MainWindow", "Shunt Adjustment:"))
        self.label_16.setText(_translate("MainWindow", "Area Interchange:"))
        self.label_166.setText(_translate("MainWindow", "VAR limit:"))
        self.label_17.setText(_translate("MainWindow", "Contingency Case Rating:"))
        self.label_18.setText(_translate("MainWindow", "Base Case Rating:"))
        self.label_4.setText(_translate("MainWindow", "Contingency options:"))
        self.label_19.setText(_translate("MainWindow", "%, Rating"))
        self.label_199.setText(_translate("MainWindow", "MW"))
        self.label_19pl.setText(_translate("MainWindow", " % of initial remaining capacity"))
        # self.label_19mw.setText(_translate("MainWindow", "MW"))
        self.label_20.setText(_translate("MainWindow", "%, Rating"))
        self.label_21.setText(_translate("MainWindow", "Transformers Thermal Limit Mode:"))
        self.label_22.setText(_translate("MainWindow", "Lines Thermal Limit Mode:"))
        self.label_23.setText(_translate("MainWindow", "Parallel Processing:"))
        self.label_24.setText(_translate("MainWindow", "Number of Cores:"))
        self.label_25.setText(_translate("MainWindow", "Contingencies:"))
        self.label_26.setText(_translate("MainWindow", "Scenrios:"))
        self.label_27.setText(_translate("MainWindow", "Output File:"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_run.setText(_translate("MainWindow", "RUN"))
        self.pushButton_initiateOptions.setText(_translate("MainWindow", "Initiate\ndefault\noptions"))
        self.menuFile.setTitle(_translate("MainWindow", "Help"))
        self.menuHelp.setTitle(_translate("MainWindow", "About"))
        self.label_TransmissionPlanning.setText(
            _translate("Dialog", "Electric Transmission Planning\n      & Strategic Initiatives"))


    def openFileNameDialog_case(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        CASE, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "PSSE file (*.sav);;All Files (*)", options=options)
        if CASE:
            self.lineEdit_studycase.setText(CASE)

    def openFileNameDialog_bus(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        bus_con, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                              "CON file (*.con);;All Files (*)", options=options)
        if bus_con:
            self.lineEdit_bus.setText(bus_con)

    def openFileNameDialog_line(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        line_con, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                              "CON file (*.con);;All Files (*)", options=options)
        if line_con:
            self.lineEdit_LineFB.setText(line_con)

    def openFileNameDialog_single(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        single_con, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                              "CON file (*.con);;All Files (*)", options=options)
        if single_con:
            self.lineEdit_Single.setText(single_con)

    def openFileNameDialog_tower(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        tower_con, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                              "CON file (*.con);;All Files (*)", options=options)
        if tower_con:
            self.lineEdit_Tower.setText(tower_con)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        save_out, _ = QFileDialog.getSaveFileName(None,"QFileDialog.getSaveFileName()","","CSV files (*.csv);;All Files (*)", options=options)
        if save_out:
            save_out = save_out + ".csv"
            self.lineEdit_outputFile.setText(save_out)


    def studySizeSelect(self):
        # print self.comboBox_StudySize.currentText()
        if str(self.comboBox_StudySize.currentText()) == 'Area':
            self.lineEdit_AreNumber.setDisabled(False)
            self.lineEdit_ZoneNumber.setDisabled(True)
            self.lineEdit_FromBus.setDisabled(True)
            self.lineEdit_ToBus.setDisabled(True)
            self.lineEdit_ID.setDisabled(True)
        elif str(self.comboBox_StudySize.currentText()) == 'Zone':
            self.lineEdit_AreNumber.clear()
            self.lineEdit_AreNumber.setDisabled(True)
            self.lineEdit_ZoneNumber.setDisabled(False)
            self.lineEdit_FromBus.setDisabled(True)
            self.lineEdit_ToBus.setDisabled(True)
            self.lineEdit_ID.setDisabled(True)
        elif str(self.comboBox_StudySize.currentText()) == 'Single Branch':
            self.lineEdit_AreNumber.setDisabled(True)
            self.lineEdit_ZoneNumber.setDisabled(True)
            self.lineEdit_FromBus.setDisabled(False)
            self.lineEdit_ToBus.setDisabled(False)
            self.lineEdit_ID.setDisabled(False)

    def violationStudy(self):
        if str(self.comboBox_studyViolations.currentText()) == 'Thermal Only':
            self.checkbox_violatio.setChecked(False)
            self.checkbox_violatio.setDisabled(True)
        elif str(self.comboBox_studyViolations.currentText()) == 'Thermal & Voltage':
            self.checkbox_violatio.setChecked(True)
            self.checkbox_violatio.setDisabled(False)



    def sliderValue(self):
        value = self.horizontalSlider.value() + 1
        self.lineEdit_BusLocationPercent.setText(str(value)+"%")

    def openDoc(self):
        subprocess.Popen(["HelpDoc.pdf"], shell=True)

    def runMain(self):
        opts = {"busmsm": 0.5,
                "sysmsm": 5.0,
                "rating": 'a',
                "flowlimit": 100.0,
                "stype_cnt": 'contingency',
                "stype_trp": 'tripping',
                "stype_cact": 'caction',
                "DEV_opt": 1,
                "study_case": self.lineEdit_studycase.text(),
                "bus_con": self.lineEdit_bus.text(),
                "line_con": self.lineEdit_LineFB.text(),
                "single_con": self.lineEdit_Single.text(),
                "tower_con": self.lineEdit_Tower.text(),
                "study_engine": self.comboBox_studyEngine.currentText(),
                "study_size": self.comboBox_StudySize.currentText(),
                "precision": int(self.lineEdit_precision.text()),
                "area_number": self.lineEdit_AreNumber.text(),
                "zone_number": self.lineEdit_ZoneNumber.text(),
                "from_bus": self.lineEdit_FromBus.text(),
                "to_bus": self.lineEdit_ToBus.text(),
                "ID": self.lineEdit_ID.text(),
                "bus_location": float(float(self.horizontalSlider.value())/100),
                "study_violation": self.comboBox_studyViolations.currentText(),
                "switched_opt": self.checkbox_violatio.isChecked(),
                "solution_method": self.comboBox_solutionMethod.currentText(),
                "shunt_adjustment": self.comboBox_shuntAdjustment.currentText(),
                "tap_adjustment": self.comboBox_tapAdjustments.currentText(),
                "are_intechange": self.comboBox_areaInterchange.currentText(),
                "var_limit": self.comboBox_varlimit.currentText(),
                "base_case_rating": self.comboBox_baseRating.currentText(),
                "contingency_case_rating": self.comboBox_countRating.currentText(),
                "base_rate_multi": int(self.lineEdit_baseRating.text()),
                "cont_rate_multi": int(self.lineEdit_contRating.text()),
                "line_limit": self.comboBox_lineThermalmode.currentText(),
                "trans_limit": self.comboBox_transThermalmode.currentText(),
                "core_number": int(self.lineEdit_cores.text()),
                "cont_scenario": self.comboBox_contScenarios.currentText(),
                "output": self.lineEdit_outputFile.text(),
                "report_step": self.checkbox_saveEveryStep.isChecked(),
                "startingLoad_stat": self.comboBox_startinload.currentText(),
                "startingLoad_value": self.lineEdit_percentStaartLoad.text(),
                "addCon": self.checkbox_addCon.isChecked()
                }
        zone_flag = False
        if opts["study_size"] == "Zone":
            zones = range(351,366)
            try:
                zvalid = zones.index(int(opts["zone_number"]))
            except:
                zone_flag = True

        ## test bus numbers
        if not opts["study_case"]:
            QMessageBox.critical(None, "Error", "    Please select the study case.     ")
            Ui_MainWindow()
        elif opts["core_number"] > mp.cpu_count():
            mms = QMessageBox()
            mms.critical(None, "Error", "Your system has "+ str(mp.cpu_count()) +" logical cores.\nPlease select <= " + str(mp.cpu_count()) + " for parallel processing.")
            Ui_MainWindow()
        elif opts["core_number"] < 1:
            b = '\U0001F609'
            mms = QMessageBox()
            mms.critical(None, "Error",
                         "Your system has " + str(mp.cpu_count()) + " logical cores.\nPlease select a ratioanl number for parallel processing! " + b.decode('unicode-escape'))
            Ui_MainWindow()
        elif not opts["core_number"]:
            mms = QMessageBox()
            mms.critical(None, "Error", "  Please select the number of cores for study.  ")
            Ui_MainWindow()
        elif not opts["study_case"]:
            QMessageBox.critical(None, "Error", "    Please select the study case.     ")
            Ui_MainWindow()
        elif not opts["output"]:
            QMessageBox.critical(None, "Error", "    Please select the output directory.     ")
            Ui_MainWindow()
        elif opts["cont_scenario"] == "N-1, N-2, and N-1-1" and not opts["bus_con"]:
            QMessageBox.critical(None, "Error", "    Please upload the *Bus* contingency file.     ")
            Ui_MainWindow()
        elif opts["cont_scenario"] == "N-1, N-2, and N-1-1" and not opts["line_con"]:
            QMessageBox.critical(None, "Error", "    Please upload the *Line_FB* contingency file.     ")
            Ui_MainWindow()
        elif opts["cont_scenario"] == "N-1, N-2, and N-1-1" and not opts["single_con"]:
            QMessageBox.critical(None, "Error", "    Please upload the *Single* contingency file..     ")
            Ui_MainWindow()
        elif opts["cont_scenario"] == "N-1, N-2, and N-1-1" and not opts["tower_con"]:
            QMessageBox.critical(None, "Error", "    Please upload the *Tower* contingency file.     ")
            Ui_MainWindow()
        elif opts["cont_scenario"] == "N-1 and N-2" and not opts["bus_con"]:
            QMessageBox.critical(None, "Error", "    Please upload the *Bus* contingency file.     ")
            Ui_MainWindow()
        elif opts["cont_scenario"] == "N-1 and N-2" and not opts["line_con"]:
            QMessageBox.critical(None, "Error", "    Please upload the *Line_FB* contingency file.     ")
            Ui_MainWindow()
        elif opts["cont_scenario"] == "N-1 and N-2" and not opts["single_con"]:
            QMessageBox.critical(None, "Error", "    Please upload the *Single* contingency file..     ")
            Ui_MainWindow()
        elif opts["cont_scenario"] == "N-1 and N-2" and not opts["tower_con"]:
            QMessageBox.critical(None, "Error", "    Please upload the *Tower* contingency file.     ")
            Ui_MainWindow()
        elif opts["cont_scenario"] == "Single" and not opts["single_con"]:
            QMessageBox.critical(None, "Error", "    Please upload the *Single* contingency files.     ")
            Ui_MainWindow()
        elif opts["study_size"] == "Area" and opts["area_number"] != "0000":
            QMessageBox.critical(None, "Error", "    Please enter the area number, DVP is 0000.     ")
            Ui_MainWindow()
        elif opts["study_size"] == "Zone" and not opts["zone_number"]:
            QMessageBox.critical(None, "Error", "    Please enter the zone number.     ")
            Ui_MainWindow()
        elif opts["study_size"] == "Zone" and zone_flag:
            QMessageBox.critical(None, "Error", "    Zone number is not valid.     ")
            Ui_MainWindow()
        elif opts["study_size"] == "Single Branch" and not opts["from_bus"]:
            QMessageBox.critical(None, "Error", "    Please enter the FROM BUS number.     ")
            Ui_MainWindow()
        elif opts["study_size"] == "Single Branch" and not opts["to_bus"]:
            QMessageBox.critical(None, "Error", "    Please enter the TO BUS number.     ")
            Ui_MainWindow()
        elif opts["study_size"] == "Single Branch" and not opts["ID"]:
            QMessageBox.critical(None, "Error", "    Please enter the circuit ID.     ")
            Ui_MainWindow()
        elif opts["study_size"] == "Single Branch" and main_test(opts):  ## *Only the speciied branch
            QMessageBox.critical(None, "Error", "    Branch is not non-transformer branch.     ")
            Ui_MainWindow()
        else:
            # main(opts, progressBar=self.progressBar)
            # self.progressBar.setValue(100)
            # QMessageBox.information(None, "Results", "        Study Finished!        ")
            for i in range(1,101):
                time.sleep(0.05)
                self.progressBar.setValue(int(i))
            QMessageBox.information(None, "Results", "        Study Finished!        ")

    def coreNumber(self):
        if str(self.comboBox_cores.currentText()) == 'CPU cores':
            process_core = mp.cpu_count()
            self.lineEdit_cores.setText(str(process_core))
        if str(self.comboBox_cores.currentText()) == 'CPU cores - 1':
            process_core = mp.cpu_count()
            self.lineEdit_cores.setText(str(process_core - 1))
        if str(self.comboBox_cores.currentText()) == 'User input':
            self.lineEdit_cores.setText("")
    def initiateOptions(self):
        # self.lineEdit_AreNumber.setDisabled(False)
        # self.lineEdit_AreNumber.setText("345")
        # self.lineEdit_ZoneNumber.setDisabled(True)
        # self.lineEdit_FromBus.setDisabled(True)
        # self.lineEdit_ToBus.setDisabled(True)
        # self.lineEdit_ID.setDisabled(True)
        self.horizontalSlider.setValue(50)
        value = self.horizontalSlider.value()
        self.lineEdit_BusLocationPercent.setText(str(value) + "%")
        self.comboBox_studyEngine.setCurrentText("PSSE 33   &   PowerGEM TARA")
        self.comboBox_baseRating.setCurrentText("Rating A")
        self.lineEdit_baseRating.setText("100")
        self.comboBox_countRating.setCurrentText("Rating B")
        self.lineEdit_contRating.setText("100")
        self.lineEdit_precision.setText("5")
        self.comboBox_studyViolations.setCurrentText("Thermal Only")
        self.comboBox_cores.setCurrentText("CPU cores - 1")
        self.comboBox_contScenarios.setCurrentText("N-1, N-2, and N-1-1")
        self.comboBox_lineThermalmode.setCurrentText("MVA rating")
        self.comboBox_transThermalmode.setCurrentText("MVA rating")
        self.comboBox_studyEngine.setCurrentText('PSSE 33  &  PowerGEM TARA')
        self.comboBox_shuntAdjustment.setCurrentText("Enable all")
        self.comboBox_tapAdjustments.setCurrentText("Lock taps")
        self.comboBox_varlimit.setCurrentText("Apply immediately")
        self.comboBox_startinload.setCurrentText("Percent (Base Case)")
        self.lineEdit_percentStaartLoad.setText("110")
        self.checkbox_addCon.setChecked(True)


    def logoPics(self):
        if str(self.comboBox_studyEngine.currentText()) == 'PSS/E 33  &  PowerGEM TARA':
            self.label_logo_psse.setDisabled(False)
            self.label_logo_tara.setDisabled(False)
        if str(self.comboBox_studyEngine.currentText()) == 'PSS/E 33 Only':
            self.label_logo_psse.setDisabled(False)
            self.label_logo_tara.setDisabled(True)

    def countScenarios(self):
        if str(self.comboBox_contScenarios.currentText()) == 'Single':
            self.lineEdit_Tower.setDisabled(True)
            self.lineEdit_LineFB.setDisabled(True)
            self.lineEdit_bus.setDisabled(True)
        else:
            self.lineEdit_Tower.setDisabled(False)
            self.lineEdit_LineFB.setDisabled(False)
            self.lineEdit_bus.setDisabled(False)

    def startingLoad(self):
        _translate = QtCore.QCoreApplication.translate
        if str(self.comboBox_startinload.currentText()) == "Percent (Base Case)":
            self.label_19pl.setText(_translate("MainWindow", " % of initial remaining capacity"))
            self.lineEdit_percentStaartLoad.setText("")
        if str(self.comboBox_startinload.currentText()) == "MW (User input)":
            self.label_19pl.setText(_translate("MainWindow", "  MW"))
            self.lineEdit_percentStaartLoad.setText("")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

