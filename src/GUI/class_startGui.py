
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QFileDialog, QDialog, QWidget
from PyQt6.QtCore import pyqtSignal
import os
import json

from GUI.startGui import Ui_startGui
from GUI.newConfGUI import Ui_newConfGUI

class confCreator(QDialog, Ui_newConfGUI):
    newDataset = pyqtSignal()
    openMain = pyqtSignal(str)
    
    def __init__(self, appDir):
        super().__init__()
        self.setupUi(self)
        self.appDir = appDir
        self.configsPath = appDir + "../cfg/configs/"
        jsonExamplePath = appDir + "../cfg/example.json"
        self.mode = "Individual"


        with open(jsonExamplePath, "r") as j:
            self.configGral = json.load(j)

        self.tab.setEnabled(True)
        self.tab_2.setEnabled(False)

        self.radioButton.clicked.connect(self.all4One)
        self.radioButton_2.clicked.connect(self.one4All)

        self.pushButton_saveNew.clicked.connect(self.exportDataset)
        self.pushButton_input.clicked.connect(lambda _: self.SelectDirectory("input"))
        self.pushButton_output.clicked.connect(lambda _: self.SelectDirectory("output"))
        self.pushButton_ref.clicked.connect(lambda _: self.SelectDirectory("References"))
        self.pushButton_roi.clicked.connect(lambda _: self.SelectDirectory("Rois"))
        self.pushButton_val.clicked.connect(lambda _: self.SelectDirectory("Validation"))
        self.pushButton_pat.clicked.connect(lambda _: self.SelectDirectory("Patterns"))
        self.pushButton_selectModelDir.clicked.connect(lambda _: self.SelectDirectory("Models"))
        # Para modo Multiple (Selecciona la carpeta raiz y el programa crea la estructura)
        self.pushButton_root.clicked.connect(lambda _: self.SelectDirectory("Multiple"))

        
    def all4One(self):
        self.tab.setEnabled(True)
        self.tabWidget.setCurrentWidget(self.tab)
        self.tab_2.setEnabled(False)
        self.mode = "Individual"

        

    def one4All(self):
        self.tab_2.setEnabled(True)
        self.tabWidget.setCurrentWidget(self.tab_2)
        self.tab.setEnabled(False)
        self.mode = "Multiple"
        
        


    def openFolderDialog(self):
        dialogoSeleccionFolder = QFileDialog()
        dialogoSeleccionFolder.setOption(QFileDialog.DontUseNativeDialog,True)
        dialogoSeleccionFolder.setOption(QFileDialog.ReadOnly, True)
        dialogoSeleccionFolder.setFileMode(QFileDialog.Directory) # Set para configurar solo directorios como seleccionables
        
        pathSelected = dialogoSeleccionFolder.getExistingDirectory(self, "Select Directory")
        
        return pathSelected

    def exportDataset(self):
        
        nameDataset = str(self.lineEdit_name.text())

        self.configGral["nombre"] = nameDataset
        self.configGral["datasetBuilderCfg"] = "/" + self.lineEdit.text()
        
        datasetPath = self.configsPath + nameDataset + ".json"
        with open(datasetPath, "w+") as f:
            f.seek(0)
            f.write(json.dumps(self.configGral,indent=4))
            f.close()


        self.newDataset.emit()
        self.accept()

    def SelectDirectory(self, mode):
        pathSelected = self.openFolderDialog()
        if mode == "output":
            self.configGral["outputDir"] = pathSelected + "/"
            #label = self.label_outputDetect
        elif mode == "Patterns":
            self.configGral["PatternsDir"] = pathSelected + "/"
            #label = self.label_yoloOutput
        elif mode == "Validation":
            self.configGral["ValidationDir"] = pathSelected + "/"
            #label = self.label_outputMask
        elif mode == "input":
            self.configGral["inputDir"] = pathSelected + "/"
        elif mode == "Rois":
            self.configGral["RoisDir"] = pathSelected + "/"
        elif mode == "References":
            self.configGral["ReferencesDir"] = pathSelected + "/"
        elif mode == "Models":
            self.configGral["modelPath"] = pathSelected + "/"
        elif mode == "Multiple":
            self.configGral["outputDir"] = pathSelected + "/" + "output"
            self.configGral["PatternsDir"] = pathSelected + "/" + "patterns"
            self.configGral["ValidationDir"] = pathSelected + "/" + "validation"
            self.configGral["inputDir"] = pathSelected + "/" + "input"
            self.configGral["RoisDir"] = pathSelected + "/" + "rois"
            self.configGral["ReferencesDir"] = pathSelected + "/" + "references"
            self.configGral["modelPath"] = pathSelected + "/" + "model"

            try:
                os.mkdir(pathSelected + "/" + "output")
                os.mkdir(pathSelected + "/" + "patterns")
                os.mkdir(pathSelected + "/" + "validation")
                os.mkdir(pathSelected + "/" + "input")
                os.mkdir(pathSelected + "/" + "rois")
                os.mkdir(pathSelected + "/" + "references")
                os.mkdir(pathSelected + "/" + "model")
            except Exception as e:
                print(f"No se han podido crear todas las carpetas {e}")

            



    def openCreator(self):
        self.show()



class startGui(QWidget, Ui_startGui):
    
    openMain = pyqtSignal(str)

    def __init__(self, appDir):
        super().__init__()
        self.setupUi(self)
        self.appDir = appDir
        self.configsPath = appDir + "../cfg/configs/"

        self.datasetCreator = confCreator(self.appDir)
        if not os.path.exists(self.configsPath):
            os.mkdir(self.configsPath)
            
        for file in os.listdir(self.configsPath):
            if file.endswith("json"):
                self.comboBox_Selector.addItem(file.split(".")[0])
        

        self.datasetCreator.newDataset.connect(self.refreshCombo)

        self.pushButton_Load.clicked.connect(self.openApp)
        self.pushButton_Crear.clicked.connect(self.showCreator)


        self.show()

    def refreshCombo(self):
        self.comboBox_Selector.clear()
        for file in os.listdir(self.configsPath):
            if file.endswith("json"):
                self.comboBox_Selector.addItem(file.split(".")[0])


    def showCreator(self):
        self.datasetCreator.openCreator()

    def openApp(self):
        dataset = self.configsPath + str(self.comboBox_Selector.currentText()) + ".json"
        self.openMain.emit(dataset)
        self.close()