# Form implementation generated from reading ui file 'MainGUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 852)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout.setContentsMargins(101, -1, 101, 21)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton_openInput = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_openInput.setObjectName("pushButton_openInput")
        self.verticalLayout.addWidget(self.pushButton_openInput)
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButto_offTrue = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButto_offTrue.setChecked(True)
        self.radioButto_offTrue.setAutoExclusive(True)
        self.radioButto_offTrue.setObjectName("radioButto_offTrue")
        self.verticalLayout_4.addWidget(self.radioButto_offTrue)
        self.radioButton_offFalse = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButton_offFalse.setAutoExclusive(True)
        self.radioButton_offFalse.setObjectName("radioButton_offFalse")
        self.verticalLayout_4.addWidget(self.radioButton_offFalse)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tab_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButton_drawTrue = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton_drawTrue.setAutoExclusive(True)
        self.radioButton_drawTrue.setObjectName("radioButton_drawTrue")
        self.verticalLayout_5.addWidget(self.radioButton_drawTrue)
        self.radioButton_drawFalse = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButton_drawFalse.setChecked(True)
        self.radioButton_drawFalse.setAutoExclusive(True)
        self.radioButton_drawFalse.setObjectName("radioButton_drawFalse")
        self.verticalLayout_5.addWidget(self.radioButton_drawFalse)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.label_5 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.pushButton_extractSamples = QtWidgets.QPushButton(parent=self.tab_2)
        self.pushButton_extractSamples.setObjectName("pushButton_extractSamples")
        self.verticalLayout.addWidget(self.pushButton_extractSamples)
        self.plainTextEdit_samplesExtraction = QtWidgets.QPlainTextEdit(parent=self.tab_2)
        self.plainTextEdit_samplesExtraction.setObjectName("plainTextEdit_samplesExtraction")
        self.verticalLayout.addWidget(self.plainTextEdit_samplesExtraction)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 3)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(5, 2)
        self.verticalLayout.setStretch(7, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setContentsMargins(101, -1, 101, 21)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.table_Clases = QtWidgets.QTableWidget(parent=self.tab_3)
        self.table_Clases.setObjectName("table_Clases")
        self.table_Clases.setColumnCount(2)
        self.table_Clases.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_Clases.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Clases.setHorizontalHeaderItem(1, item)
        self.verticalLayout_3.addWidget(self.table_Clases)
        self.label_6 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.pushButton_openDataset = QtWidgets.QPushButton(parent=self.tab_3)
        self.pushButton_openDataset.setObjectName("pushButton_openDataset")
        self.verticalLayout_3.addWidget(self.pushButton_openDataset)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 2)
        self.verticalLayout_3.setStretch(4, 3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.tab_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 900, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.spinBox_epochs = QtWidgets.QSpinBox(parent=self.groupBox_3)
        self.spinBox_epochs.setMinimum(1)
        self.spinBox_epochs.setMaximum(999)
        self.spinBox_epochs.setProperty("value", 150)
        self.spinBox_epochs.setObjectName("spinBox_epochs")
        self.horizontalLayout_2.addWidget(self.spinBox_epochs)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, 900, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.spinBox_bs = QtWidgets.QSpinBox(parent=self.groupBox_3)
        self.spinBox_bs.setMinimum(1)
        self.spinBox_bs.setMaximum(128)
        self.spinBox_bs.setProperty("value", 2)
        self.spinBox_bs.setObjectName("spinBox_bs")
        self.horizontalLayout_3.addWidget(self.spinBox_bs)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.groupBox_3)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.radioButton_aumTrue = QtWidgets.QRadioButton(parent=self.groupBox_4)
        self.radioButton_aumTrue.setChecked(True)
        self.radioButton_aumTrue.setAutoExclusive(True)
        self.radioButton_aumTrue.setObjectName("radioButton_aumTrue")
        self.horizontalLayout_4.addWidget(self.radioButton_aumTrue)
        self.radioButton_aumFalse = QtWidgets.QRadioButton(parent=self.groupBox_4)
        self.radioButton_aumFalse.setAutoExclusive(True)
        self.radioButton_aumFalse.setObjectName("radioButton_aumFalse")
        self.horizontalLayout_4.addWidget(self.radioButton_aumFalse)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.groupBox_3)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_6.addWidget(self.label_13)
        self.radioButton_clasiTrue = QtWidgets.QRadioButton(parent=self.groupBox_5)
        self.radioButton_clasiTrue.setAutoExclusive(True)
        self.radioButton_clasiTrue.setObjectName("radioButton_clasiTrue")
        self.horizontalLayout_6.addWidget(self.radioButton_clasiTrue)
        self.radioButton_clasiFalse = QtWidgets.QRadioButton(parent=self.groupBox_5)
        self.radioButton_clasiFalse.setChecked(True)
        self.radioButton_clasiFalse.setAutoExclusive(True)
        self.radioButton_clasiFalse.setObjectName("radioButton_clasiFalse")
        self.horizontalLayout_6.addWidget(self.radioButton_clasiFalse)
        self.verticalLayout_7.addWidget(self.groupBox_5)
        self.verticalLayout_6.addWidget(self.groupBox_3)
        self.pushButton_trainStart = QtWidgets.QPushButton(parent=self.tab_4)
        self.pushButton_trainStart.setObjectName("pushButton_trainStart")
        self.verticalLayout_6.addWidget(self.pushButton_trainStart)
        self.label_14 = QtWidgets.QLabel(parent=self.tab_4)
        self.label_14.setAutoFillBackground(False)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_6.addWidget(self.label_14)
        self.plainTextEdit_trainOutput = QtWidgets.QPlainTextEdit(parent=self.tab_4)
        self.plainTextEdit_trainOutput.setObjectName("plainTextEdit_trainOutput")
        self.verticalLayout_6.addWidget(self.plainTextEdit_trainOutput)
        self.verticalLayout_6.setStretch(0, 7)
        self.verticalLayout_6.setStretch(1, 3)
        self.verticalLayout_6.setStretch(2, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_16 = QtWidgets.QLabel(parent=self.tab_5)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.pushButton_openValDir = QtWidgets.QPushButton(parent=self.tab_5)
        self.pushButton_openValDir.setObjectName("pushButton_openValDir")
        self.verticalLayout_8.addWidget(self.pushButton_openValDir)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.tab_5)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radioButton.setChecked(True)
        self.radioButton.setAutoExclusive(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_5.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.radioButton_2.setAutoExclusive(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_5.addWidget(self.radioButton_2)
        self.verticalLayout_8.addWidget(self.groupBox_6)
        self.label_18 = QtWidgets.QLabel(parent=self.tab_5)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_8.addWidget(self.label_18)
        self.pushButton_validation = QtWidgets.QPushButton(parent=self.tab_5)
        self.pushButton_validation.setObjectName("pushButton_validation")
        self.verticalLayout_8.addWidget(self.pushButton_validation)
        self.plainTextEdit_valOutput = QtWidgets.QPlainTextEdit(parent=self.tab_5)
        self.plainTextEdit_valOutput.setObjectName("plainTextEdit_valOutput")
        self.verticalLayout_8.addWidget(self.plainTextEdit_valOutput)
        self.label_17 = QtWidgets.QLabel(parent=self.tab_5)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_8.addWidget(self.label_17)
        self.tableWidget_validation = QtWidgets.QTableWidget(parent=self.tab_5)
        self.tableWidget_validation.setObjectName("tableWidget_validation")
        self.tableWidget_validation.setColumnCount(2)
        self.tableWidget_validation.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_validation.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_validation.setHorizontalHeaderItem(1, item)
        self.tableWidget_validation.horizontalHeader().setDefaultSectionSize(190)
        self.verticalLayout_8.addWidget(self.tableWidget_validation)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_57 = QtWidgets.QLabel(parent=self.tab_8)
        self.label_57.setObjectName("label_57")
        self.verticalLayout_12.addWidget(self.label_57)
        self.pushButton = QtWidgets.QPushButton(parent=self.tab_8)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_12.addWidget(self.pushButton)
        self.label_48 = QtWidgets.QLabel(parent=self.tab_8)
        self.label_48.setObjectName("label_48")
        self.verticalLayout_12.addWidget(self.label_48)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.tab_8)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_12.addWidget(self.pushButton_3)
        self.label_58 = QtWidgets.QLabel(parent=self.tab_8)
        self.label_58.setObjectName("label_58")
        self.verticalLayout_12.addWidget(self.label_58)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.tab_8)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_12.addWidget(self.pushButton_2)
        self.label_60 = QtWidgets.QLabel(parent=self.tab_8)
        self.label_60.setObjectName("label_60")
        self.verticalLayout_12.addWidget(self.label_60)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.tab_8)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_12.addWidget(self.pushButton_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_12.addItem(spacerItem2)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.tab_8)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_12.addWidget(self.pushButton_5)
        self.verticalLayout_12.setStretch(0, 2)
        self.verticalLayout_12.setStretch(1, 2)
        self.verticalLayout_12.setStretch(2, 1)
        self.verticalLayout_12.setStretch(3, 2)
        self.verticalLayout_12.setStretch(4, 2)
        self.verticalLayout_12.setStretch(5, 2)
        self.verticalLayout_12.setStretch(6, 1)
        self.verticalLayout_12.setStretch(7, 2)
        self.verticalLayout_12.setStretch(8, 2)
        self.verticalLayout_12.setStretch(9, 2)
        self.gridLayout_4.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_8, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(parent=self.tab)
        self.label_7.setStyleSheet("font: 18pt \"Ubuntu\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.lineEdit_netName = QtWidgets.QLineEdit(parent=self.tab)
        self.lineEdit_netName.setObjectName("lineEdit_netName")
        self.verticalLayout_2.addWidget(self.lineEdit_netName)
        self.label = QtWidgets.QLabel(parent=self.tab)
        self.label.setStyleSheet("font: 18pt \"Ubuntu\";")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_8 = QtWidgets.QLabel(parent=self.tab)
        self.label_8.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.pushButton_modelPath = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_modelPath.setObjectName("pushButton_modelPath")
        self.verticalLayout_2.addWidget(self.pushButton_modelPath)
        self.label_9 = QtWidgets.QLabel(parent=self.tab)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_3 = QtWidgets.QLabel(parent=self.tab)
        self.label_3.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.pushButton_pat = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_pat.setObjectName("pushButton_pat")
        self.verticalLayout_2.addWidget(self.pushButton_pat)
        self.label_Pat = QtWidgets.QLabel(parent=self.tab)
        self.label_Pat.setObjectName("label_Pat")
        self.verticalLayout_2.addWidget(self.label_Pat)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_Ref = QtWidgets.QLabel(parent=self.tab)
        self.label_Ref.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_Ref.setObjectName("label_Ref")
        self.verticalLayout_2.addWidget(self.label_Ref)
        self.pushButton_ref = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_ref.setObjectName("pushButton_ref")
        self.verticalLayout_2.addWidget(self.pushButton_ref)
        self.label_RefDir = QtWidgets.QLabel(parent=self.tab)
        self.label_RefDir.setObjectName("label_RefDir")
        self.verticalLayout_2.addWidget(self.label_RefDir)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label_Roi = QtWidgets.QLabel(parent=self.tab)
        self.label_Roi.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_Roi.setObjectName("label_Roi")
        self.verticalLayout_2.addWidget(self.label_Roi)
        self.pushButton_rois = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_rois.setObjectName("pushButton_rois")
        self.verticalLayout_2.addWidget(self.pushButton_rois)
        self.label_RoiDir = QtWidgets.QLabel(parent=self.tab)
        self.label_RoiDir.setObjectName("label_RoiDir")
        self.verticalLayout_2.addWidget(self.label_RoiDir)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.label_Input = QtWidgets.QLabel(parent=self.tab)
        self.label_Input.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_Input.setObjectName("label_Input")
        self.verticalLayout_2.addWidget(self.label_Input)
        self.pushButton_input = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_input.setObjectName("pushButton_input")
        self.verticalLayout_2.addWidget(self.pushButton_input)
        self.label_inputDir = QtWidgets.QLabel(parent=self.tab)
        self.label_inputDir.setObjectName("label_inputDir")
        self.verticalLayout_2.addWidget(self.label_inputDir)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.label_output = QtWidgets.QLabel(parent=self.tab)
        self.label_output.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_output.setObjectName("label_output")
        self.verticalLayout_2.addWidget(self.label_output)
        self.pushButton_output = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_output.setObjectName("pushButton_output")
        self.verticalLayout_2.addWidget(self.pushButton_output)
        self.label_outputDir = QtWidgets.QLabel(parent=self.tab)
        self.label_outputDir.setObjectName("label_outputDir")
        self.verticalLayout_2.addWidget(self.label_outputDir)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.label_val = QtWidgets.QLabel(parent=self.tab)
        self.label_val.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label_val.setObjectName("label_val")
        self.verticalLayout_2.addWidget(self.label_val)
        self.pushButton_val = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_val.setObjectName("pushButton_val")
        self.verticalLayout_2.addWidget(self.pushButton_val)
        self.label_ValDir = QtWidgets.QLabel(parent=self.tab)
        self.label_ValDir.setObjectName("label_ValDir")
        self.verticalLayout_2.addWidget(self.label_ValDir)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)
        self.label_15 = QtWidgets.QLabel(parent=self.tab)
        self.label_15.setStyleSheet("font: 14pt \"Ubuntu\";")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.lineEdit_Divider = QtWidgets.QLineEdit(parent=self.tab)
        self.lineEdit_Divider.setObjectName("lineEdit_Divider")
        self.verticalLayout_2.addWidget(self.lineEdit_Divider)
        self.pushButton_modifiConf = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton_modifiConf.setObjectName("pushButton_modifiConf")
        self.verticalLayout_2.addWidget(self.pushButton_modifiConf)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Open input dir:"))
        self.pushButton_openInput.setText(_translate("MainWindow", "Open"))
        self.groupBox.setTitle(_translate("MainWindow", "Offset¿?"))
        self.radioButto_offTrue.setText(_translate("MainWindow", "Yes"))
        self.radioButton_offFalse.setText(_translate("MainWindow", "No"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Only draw region¿?"))
        self.radioButton_drawTrue.setText(_translate("MainWindow", "Yes"))
        self.radioButton_drawFalse.setText(_translate("MainWindow", "No"))
        self.label_5.setText(_translate("MainWindow", "Extract samples:"))
        self.pushButton_extractSamples.setText(_translate("MainWindow", "Extract"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "SamplesExtraction"))
        self.label_2.setText(_translate("MainWindow", "Clases:"))
        item = self.table_Clases.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Clases"))
        item = self.table_Clases.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nº Imagenes"))
        self.label_6.setText(_translate("MainWindow", "Open dataset dir:"))
        self.pushButton_openDataset.setText(_translate("MainWindow", "Open"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "DatasetViewer"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Opciones de entrenamiento"))
        self.label_10.setText(_translate("MainWindow", "Epochs"))
        self.label_11.setText(_translate("MainWindow", "Batch Size"))
        self.label_12.setText(_translate("MainWindow", "Augmentator"))
        self.radioButton_aumTrue.setText(_translate("MainWindow", "True"))
        self.radioButton_aumFalse.setText(_translate("MainWindow", "False"))
        self.label_13.setText(_translate("MainWindow", "Clasificaciones"))
        self.radioButton_clasiTrue.setText(_translate("MainWindow", "True"))
        self.radioButton_clasiFalse.setText(_translate("MainWindow", "False"))
        self.pushButton_trainStart.setText(_translate("MainWindow", "Empezar entrenamiento"))
        self.label_14.setText(_translate("MainWindow", "La aplicacion no podra utilizarse mientras se entrena!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Train"))
        self.label_16.setText(_translate("MainWindow", "Open validation images dir"))
        self.pushButton_openValDir.setText(_translate("MainWindow", "Open"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Offset¿?"))
        self.radioButton.setText(_translate("MainWindow", "True"))
        self.radioButton_2.setText(_translate("MainWindow", "False"))
        self.label_18.setText(_translate("MainWindow", "Validar:"))
        self.pushButton_validation.setText(_translate("MainWindow", "Validar"))
        self.label_17.setText(_translate("MainWindow", "Clasificaciones:"))
        item = self.tableWidget_validation.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Clases detectadas"))
        item = self.tableWidget_validation.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nº Imagenes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Validation"))
        self.label_57.setText(_translate("MainWindow", "InputDir"))
        self.pushButton.setText(_translate("MainWindow", "Change"))
        self.label_48.setText(_translate("MainWindow", "Actual Dir:"))
        self.pushButton_3.setText(_translate("MainWindow", "Open Input Dir"))
        self.label_58.setText(_translate("MainWindow", "OutputDir"))
        self.pushButton_2.setText(_translate("MainWindow", "Change"))
        self.label_60.setText(_translate("MainWindow", "Actual Dir:"))
        self.pushButton_4.setText(_translate("MainWindow", "Open OutputDir"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "DataGen"))
        self.label_7.setText(_translate("MainWindow", "Nombre:"))
        self.label.setText(_translate("MainWindow", "Rutas:"))
        self.label_8.setText(_translate("MainWindow", "Model:"))
        self.pushButton_modelPath.setText(_translate("MainWindow", "Select Dir"))
        self.label_9.setText(_translate("MainWindow", "Actual dir:"))
        self.label_3.setText(_translate("MainWindow", "Patterns:"))
        self.pushButton_pat.setText(_translate("MainWindow", "Select Dir"))
        self.label_Pat.setText(_translate("MainWindow", "Actual dir:"))
        self.label_Ref.setText(_translate("MainWindow", "Reference:"))
        self.pushButton_ref.setText(_translate("MainWindow", "Select Dir"))
        self.label_RefDir.setText(_translate("MainWindow", "Actual dir:"))
        self.label_Roi.setText(_translate("MainWindow", "Rois"))
        self.pushButton_rois.setText(_translate("MainWindow", "Select Dir"))
        self.label_RoiDir.setText(_translate("MainWindow", "Actual dir:"))
        self.label_Input.setText(_translate("MainWindow", "Input Dir:"))
        self.pushButton_input.setText(_translate("MainWindow", "Select Dir"))
        self.label_inputDir.setText(_translate("MainWindow", "Actual dir:"))
        self.label_output.setText(_translate("MainWindow", "Output Dir:"))
        self.pushButton_output.setText(_translate("MainWindow", "Select Dir"))
        self.label_outputDir.setText(_translate("MainWindow", "Actual dir:"))
        self.label_val.setText(_translate("MainWindow", "Validation Dir:"))
        self.pushButton_val.setText(_translate("MainWindow", "Select Dir"))
        self.label_ValDir.setText(_translate("MainWindow", "Actual dir:"))
        self.label_15.setText(_translate("MainWindow", "Name Divider:"))
        self.pushButton_modifiConf.setText(_translate("MainWindow", "Save changes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Conf"))