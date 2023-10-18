from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import  QObject, pyqtSlot
from LOGIC.MainSamplesExtraction import samplesExtraction
from LOGIC.MainTrain import MainTrain
from LOGIC.MainCNNValidation import MainValidation
import os


class MainController(QObject):
    def __init__(self, configGeneral, appdir):
        super().__init__()
        self.appdir = appdir
        self.configGeneral = configGeneral



    def extractSamples(self,offset=True,draw=False,plainText=None):
        
        sampleExtraction = samplesExtraction(self.appdir,self.configGeneral,self.configGeneral["inputDir"],self.configGeneral["RoisDir"],offset,self.configGeneral["ReferencesDir"],self.configGeneral["PatternsDir"], self.configGeneral["outputDir"],draw,plainText)
        
        sampleExtraction.start()

        

       
    def startTrain(self,epochs,bs,aug,clasi,plainText):
        self.pltxt = plainText

        '''train = MainTrain(configGeneral=self.configGeneral,epochs=epochs,bs=bs,augmentator=aug,clasificaciones=clasi,plainText=plainText)
        train.start()'''
        self.worker_thread = MainTrain(configGeneral=self.configGeneral,epochs=epochs,bs=bs,augmentator=aug,clasificaciones=clasi,plainText=plainText)
        self.worker_thread.update_signal.connect(self.update_log)
        self.start_task()

    def startTrain2(self,epochs,bs,aug,clasi):

        os.system(f"/home/enxenia/anaconda3/envs/dos/bin/python LOGIC/MainTrainPythonDos.py -g \"{self.configGeneral}\" -e {int(epochs)} -b {int(bs)} -a {bool(aug)} -c {bool(clasi)}")        

    def startVal(self,offset,plainText,uiMan):
        
        val = MainValidation(configGeneral=self.configGeneral,offset=offset,plainText=plainText,uiMan=uiMan)

        val.start()

    def start_task(self):
        self.worker_thread.start()

    @pyqtSlot(str)
    def update_log(self, message):
        self.pltxt.appendPlainText(f"{message}")
        QApplication.processEvents()


