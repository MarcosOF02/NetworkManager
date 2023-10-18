import os, sys
from PyQt6 import QtCore
_fromUtf8 = str
import qtmodern.styles
import qtmodern.windows
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QMessageBox
from GUI.class_startGui import startGui
from LOGIC.MainController import MainController
from MainGuiManager import MainGuiManager
from MainDatasetBuilder import ConfControlPanel
from MainDatasetBuilder import GraphicsScene
import json


class MainProgram(QApplication):

    def __init__(self):
        QApplication.__init__(self,sys.argv)
        self.appdir = os.path.dirname(os.path.abspath(__file__)) + "/"
        self.selector = startGui(self.appdir)
        self.selector.openMain.connect(self.selectConf)
        


    def selectConf(self,confPath):
        self.confPath = confPath
        self.getConfigFiles()

        self.mainController = MainController(self.configGeneral, self.appdir)
        self.mainGUIManager = MainGuiManager(self.configGeneral, self.mainController, self.appdir)
        self.mainDatasetBuilder = ConfControlPanel(self.configGeneral,self.mainGUIManager)
                
        #Creacion escenas 
        sceneImg = GraphicsScene(self.mainDatasetBuilder)
        self.mainGUIManager.ui.graphicsView.setScene(sceneImg)
        
        self.mainDatasetBuilder.sceneImg = sceneImg

        self.mainDatasetBuilder.initialization()

        self.ui = qtmodern.windows.ModernWindow(self.mainGUIManager)
        self.ui.showMaximized()

        

        self.initSignals()
        

        
    def getConfigFiles(self):
        with open(self.confPath, "r") as j:
            self.configGeneral = json.load(j)
        
    

        
    def initSignals(self):
        self.mainGUIManager.confModify.connect(self.onConfigGeneralChange)     
        self.mainGUIManager.extractSamples.connect(self.extractSamples)
        self.mainGUIManager.startTrain.connect(self.startTrain)
        self.mainGUIManager.startVal.connect(self.startVal)


    def onConfigGeneralChange(self, configGeneral):
        
        self.configGeneral = configGeneral
        self.confPath = self.confPath.split("/")
        self.confPath[-1] = self.configGeneral["nombre"] + ".json"
        self.confPath = '/'.join(self.confPath)
        
        self.mainController.configGeneral = self.configGeneral


        with open(self.confPath,"w+") as f:
            f.seek(0)
            f.write(json.dumps(configGeneral,indent=4))
            f.truncate()
            f.close()


    def extractSamples(self,offset,draw):


        QApplication.setOverrideCursor(QtCore.Qt.ForbiddenCursor)
        self.mainGUIManager.ui.tabWidget.setEnabled(False)
        self.mainController.extractSamples(offset=offset,draw=draw,plainText=self.mainGUIManager.ui.plainTextEdit_samplesExtraction)
        
        msg = QMessageBox()
        msg.setText("Se han hecho los recortes")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Importante")
        
        QApplication.restoreOverrideCursor()

        self.mainGUIManager.ui.tabWidget.setEnabled(True)

        msg.show()

        
    def startTrain(self,epochs,bs,aug,clasi,python):

        QApplication.setOverrideCursor(QtCore.Qt.ForbiddenCursor)
        self.mainGUIManager.ui.groupBox_3.setDisabled(True)
        self.mainGUIManager.ui.label_14.setDisabled(True)
        self.mainGUIManager.ui.pushButton_trainStart.setDisabled(True)
        self.mainGUIManager.ui.tab.setDisabled(True)
        self.mainGUIManager.ui.tab_2.setDisabled(True)
        self.mainGUIManager.ui.tab_3.setDisabled(True)
        self.mainGUIManager.ui.tab_5.setDisabled(True)
        if python == 3:
            self.mainController.startTrain(epochs=epochs,bs=bs,aug=aug,clasi=clasi,plainText=self.mainGUIManager.ui.plainTextEdit_trainOutput)
        else:
            self.mainController.startTrain2(epochs=epochs,bs=bs,aug=aug,clasi=clasi)

        msg = QMessageBox()
        msg.setText("Se ha acabado el entrenamiento")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Importante")
        self.mainGUIManager.ui.groupBox_3.setDisabled(False)
        self.mainGUIManager.ui.label_14.setDisabled(False)
        self.mainGUIManager.ui.pushButton_trainStart.setDisabled(False)
        self.mainGUIManager.ui.tab.setDisabled(False)
        self.mainGUIManager.ui.tab_2.setDisabled(False)
        self.mainGUIManager.ui.tab_3.setDisabled(False)
        self.mainGUIManager.ui.tab_5.setDisabled(False)
        
        QApplication.restoreOverrideCursor()

        msg.show()


    def startVal(self,offset):

        QApplication.setOverrideCursor(QtCore.Qt.ForbiddenCursor)

        self.mainController.startVal(offset=offset,plainText=self.mainGUIManager.ui.plainTextEdit_valOutput,uiMan=self.mainGUIManager)


        msg = QMessageBox()
        msg.setText("Se ha acabado la validacion")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Importante")
        
        QApplication.restoreOverrideCursor()

        msg.show()
    

    def startSearch (self):

        self.mainController.startSearch(self.mainGUIManager.ui.plainTextEdit_daysSelected.toPlainText(),self.mainGUIManager.ui.lineEdit_idsSelected.text(),self.mainGUIManager.ui.spinBox_montaje.text(),self.mainGUIManager.ui.comboBox_linea.currentText(),self.mainGUIManager.ui.plainTextEdit_searchOut)




def onExit():        
    sys.exit()  

if __name__ == '__main__':
    program = MainProgram()

    
    qtmodern.styles.dark(program)

    sys.exit(program.exec_())  
    pass



