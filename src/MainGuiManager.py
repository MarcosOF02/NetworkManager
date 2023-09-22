import os, shutil
from GUI.MainGUI import Ui_MainWindow

from PyQt6.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import pyqtSignal, QProcess, QDate
from PyQt6.QtGui import QTextCharFormat, QFont


class MainGuiManager(QMainWindow):
    confModify = pyqtSignal(object)
    extractSamples = pyqtSignal(bool,bool)
    startTrain = pyqtSignal(int,int,bool,bool)
    startVal = pyqtSignal(bool)

    def __init__(self,configGeneral, mainController, appdir):
        QMainWindow.__init__(self)
        self.appdir = appdir
        self.configGeneral = configGeneral

        self.mainController = mainController
        self.offset = True
        self.draw = False

        valDirs =[ name for name in os.listdir(self.configGeneral["ValidationDir"]) if os.path.isdir(os.path.join(self.configGeneral["ValidationDir"], name)) ]

        for dir in valDirs:
            shutil.rmtree(self.configGeneral["ValidationDir"] + "/" + dir,)

        # Init interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        # Put config into interface
        self.ui.label_Pat.setText("Actual: {}".format(self.configGeneral["PatternsDir"]))
        self.ui.label_9.setText("Actual: {}".format(self.configGeneral["modelPath"]))
        self.ui.label_RefDir.setText("Actual: {}".format(self.configGeneral["ReferencesDir"]))
        self.ui.label_RoiDir.setText("Actual: {}".format(self.configGeneral["RoisDir"]))
        self.ui.label_ValDir.setText("Actual: {}".format(self.configGeneral["ValidationDir"]))
        self.ui.label_inputDir.setText("Actual: {}".format(self.configGeneral["inputDir"]))
        self.ui.label_outputDir.setText("Actual: {}".format(self.configGeneral["outputDir"]))
        self.ui.lineEdit_netName.setText("{}".format(self.configGeneral["nombre"]))

        
        self.refreshTables()

        self.initSignals()



    def initSignals(self):
        self.ui.pushButton_input.clicked.connect(lambda _: self.SelectDirectory("input"))
        self.ui.pushButton_output.clicked.connect(lambda _: self.SelectDirectory("output"))
        self.ui.pushButton_ref.clicked.connect(lambda _: self.SelectDirectory("References"))
        self.ui.pushButton_rois.clicked.connect(lambda _: self.SelectDirectory("Rois"))
        self.ui.pushButton_val.clicked.connect(lambda _: self.SelectDirectory("Validation"))
        self.ui.pushButton_pat.clicked.connect(lambda _: self.SelectDirectory("Patterns"))
        self.ui.pushButton_modelPath.clicked.connect(lambda _: self.SelectDirectory("Model"))


        self.ui.pushButton_modifiConf.clicked.connect(self.confModded)
        self.ui.pushButton_openInput.clicked.connect(self.openInput)
        self.ui.pushButton_openDataset.clicked.connect(self.openDataset)
        self.ui.pushButton_openValDir.clicked.connect(self.openValidation)

        self.ui.radioButto_offTrue.clicked.connect(lambda: setattr(self, 'offset', True))
        self.ui.radioButton_offFalse.clicked.connect(lambda: setattr(self, 'offset', False))

        self.ui.radioButton_drawTrue.clicked.connect(lambda: setattr(self, 'draw', True))
        self.ui.radioButton_drawFalse.clicked.connect(lambda: setattr(self, 'draw', False))

        self.ui.pushButton_extractSamples.clicked.connect(self.executeExtract)
        self.ui.pushButton_trainStart.clicked.connect(self.executeTrain)
        self.ui.pushButton_validation.clicked.connect(self.executeValidation)




    def openInput(self):
        command = f"nautilus {self.configGeneral['inputDir']}"
        process = QProcess()
        process.startCommand(command)
        process.waitForFinished(-1)
        return
    
    
    def openDataset(self):
        
        command = f"nautilus {self.configGeneral['outputDir']}"
        process = QProcess()
        process.startCommand(command)
        process.waitForFinished(-1)
        self.refreshTables()
        return
    
    def openValidation(self):
        command = f"nautilus {self.configGeneral['ValidationDir']}"
        process = QProcess()
        process.startCommand(command)
        process.waitForFinished(-1)
        return


    def openFolderDialog(self):
        dialogoSeleccionFolder = QFileDialog()
        dialogoSeleccionFolder.setOption(QFileDialog.Option.DontUseNativeDialog,True)
        dialogoSeleccionFolder.setOption(QFileDialog.Option.ReadOnly, True)
        dialogoSeleccionFolder.setOption(QFileDialog.Option.ShowDirsOnly) # Set para configurar solo directorios como seleccionables
        
        pathSelected = dialogoSeleccionFolder.getExistingDirectory(self, "Select Directory")
        
        #dialogoSeleccionFolder = QFileDialog.getExistingDirectory(options=QFileDialog.Option.DontUseNativeDialog)
        
        return pathSelected
    

    def SelectDirectory(self, mode):
        pathSelected = self.openFolderDialog()

        if mode == "output":
            self.configGeneral["outputDir"] = pathSelected + "/"
            self.ui.label_outputDir = "Actual dir: " + pathSelected + "/"
            #label = configGeneral.label_outputDetect
        elif mode == "Patterns":
            self.configGeneral["PatternsDir"] = pathSelected + "/"
            
            self.ui.label_PatDir = "Actual dir: " + pathSelected + "/"
            #label = self.label_yoloOutput
        elif mode == "Validation":
            self.configGeneral["ValidationDir"] = pathSelected + "/"
            self.ui.label_valDir = "Actual dir: " + pathSelected + "/"
            #label = self.label_outputMask
        elif mode == "input":
            self.configGeneral["inputDir"] = pathSelected + "/"
            self.ui.label_InputDir = "Actual dir: " + pathSelected + "/"
        elif mode == "Rois":
            self.configGeneral["RoisDir"] = pathSelected + "/"
            self.ui.label_RoiDir = "Actual dir: " + pathSelected + "/"
        elif mode == "References":
            self.configGeneral["ReferencesDir"] = pathSelected + "/"
            self.ui.label_RefDir = "Actual dir: " + pathSelected + "/"
        
        elif mode == "Model":
            self.configGeneral["modelPath"] = pathSelected + "/"
            self.ui.label_9 = "Actual dir: " + pathSelected + "/"


    def confModded(self):
        self.refreshTables()
        self.ui.label_Pat.setText("Actual: {}".format(self.configGeneral["PatternsDir"]))
        self.ui.label_9.setText("Actual: {}".format(self.configGeneral["modelPath"]))
        self.ui.label_RefDir.setText("Actual: {}".format(self.configGeneral["ReferencesDir"]))
        self.ui.label_RoiDir.setText("Actual: {}".format(self.configGeneral["RoisDir"]))
        self.ui.label_ValDir.setText("Actual: {}".format(self.configGeneral["ValidationDir"]))
        self.ui.label_inputDir.setText("Actual: {}".format(self.configGeneral["inputDir"]))
        self.ui.label_outputDir.setText("Actual: {}".format(self.configGeneral["outputDir"]))
        
        
        if self.ui.lineEdit_netName.text() != "" or self.ui.lineEdit_netName.text() != None:
            self.configGeneral["nombre"] = self.ui.lineEdit_netName.text()
            self.ui.lineEdit_netName.setText("{}".format(self.configGeneral["nombre"]))


        self.confModify.emit(self.configGeneral)


    def refreshTables(self):
        try:
            clases = os.listdir(self.configGeneral["outputDir"])
            
            c = 0
            for clase in clases:
                nIm = len(os.listdir(self.configGeneral["outputDir"] + "/" + clase + "/"))
                
                #self.ui.table_Clases.clear()
                self.ui.table_Clases.setRowCount(len(clases))
                self.ui.table_Clases.setColumnCount(2)
                self.ui.table_Clases.setHorizontalHeaderLabels(["Clases", "Nº Imagenes"])
                self.ui.table_Clases.setItem(c, 0, QTableWidgetItem(clase))
                self.ui.table_Clases.setItem(c, 1, QTableWidgetItem(str(nIm)))
            
                c +=1
        except:
            pass
        

        try:
            validationClases = [ name for name in os.listdir(self.configGeneral["ValidationDir"]) if os.path.isdir(os.path.join(self.configGeneral["ValidationDir"], name)) ]
            
            c = 0
            for clase in validationClases:
                nIm = len(os.listdir(self.configGeneral["ValidationDir"] + "/" + clase + "/"))
                
                #self.ui.table_Clases.clear()
                self.ui.tableWidget_validation.setRowCount(len(os.listdir(self.configGeneral["ValidationDir"])))
                self.ui.tableWidget_validation.setColumnCount(2)
                self.ui.tableWidget_validation.setHorizontalHeaderLabels(["Clases", "Nº Imagenes"])
                self.ui.tableWidget_validation.setItem(c, 0, QTableWidgetItem(clase))
                self.ui.tableWidget_validation.setItem(c, 1, QTableWidgetItem(str(nIm)))
            
                c +=1
        except:
            pass


    
    def addDay(self):
        self.ui.plainTextEdit_daysSelected.appendPlainText(str(self.ui.calendarWidget_selectDays.selectedDate().toString("yyyy_MM_dd")))




    def executeExtract(self):
        
        self.extractSamples.emit(self.offset, self.draw)
        self.refreshTables()


    def executeTrain(self):
        aum = False
        clasi = False
        if self.ui.radioButton_aumFalse.isChecked:
            aum = False
        else:
            aum = True
        
        if self.ui.radioButton_clasiTrue.isChecked():
            clasi = True

        else:
            clasi = False
        
        self.startTrain.emit(int(self.ui.spinBox_epochs.text()), int(self.ui.spinBox_bs.text()),aum,clasi)
        

    def executeValidation(self):
        offset = True
        if self.ui.radioButton.isChecked():
            offset = True
        else:
            offset = False

        self.startVal.emit(offset)

