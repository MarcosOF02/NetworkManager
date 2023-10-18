'''
Created on 1 abr. 2019

@author: Guille L

@modified by: Marcos OF
'''

from PyQt6 import QtCore
_fromUtf8 = str
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QInputDialog, QLineEdit, QFileDialog
import os
import cv2
import time
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import img_to_array
from keras.utils import load_img
import numpy as np

from UTIL.ConfigFileClass import ConfigFile

mode = 1

###########################################################
#CLASE PARA EVENTOS DE RATON
#Clase hija de la ventana grafica QGraphicsScene
class GraphicsScene(QGraphicsScene):
    
    initialPosition = QtCore.QPointF(0,0)
    finalPosition = QtCore.QPointF(0,0)
    saveMsg = pyqtSignal()

    def __init__ (self, controlPanel):
        super(GraphicsScene, self).__init__ ()
        self.mouseEnable = False
        self.track = False
        self.x1new,self.x2new,self.y1new,self.y2new = 0,0,0,0
        self.cPanel = controlPanel


    def mousePressEvent(self, event):  
            
        if self.mouseEnable == True:
            super(GraphicsScene, self).mousePressEvent(event)
            
            #Detener el track con el click del raton
            self.cPanel.ui.graphicsView.setMouseTracking(False)
            
            self.initialPosition = QtCore.QPointF(event.scenePos()) #- item.rectF.center()
            ##Accion a realizar segun el proceso en el que se encuentre el programa    
            self.x1new = int(self.initialPosition.x())
            self.y1new = int(self.initialPosition.y())
            self.x2new = self.x1new
            self.y2new = self.y1new
            try:
                self.renderScene(mode)
            except:
                print("No hay regiones en el config")
                
    def mouseMoveEvent(self, event):
        
        if self.mouseEnable == True:
            if self.cPanel.ui.comboAccion.currentText() == "Create Roi":
                super(GraphicsScene, self).mouseMoveEvent(event)                
                self.finalPosition = QtCore.QPointF(event.scenePos()) #- item.rectF.center()
                self._mouse_button = event.buttons()
                if (self._mouse_button == QtCore.Qt.LeftButton):
                    self.x2new = int(self.finalPosition.x())
                    self.y2new = int(self.finalPosition.y())
                        

                    self.renderScene(0) 
            if self.cPanel.ui.comboAccion.currentText() == "Roi Maker" and self.cPanel.ui.radioButton.isChecked() == True:
                super(GraphicsScene, self).mouseMoveEvent(event)
  
                self.finalPosition = QtCore.QPointF(event.scenePos()) #- item.rectF.center()
                

                self._mouse_button = event.buttons()
                if (self._mouse_button == QtCore.Qt.LeftButton):
                    self.x2new = int(self.finalPosition.x())
                    self.y2new = int(self.finalPosition.y())
                    
                    self.renderScene(0) 
            
            if self.cPanel.ui.comboAccion.currentText() == "Reference Maker" and (self.cPanel.ui.radioButton_3.isChecked() == True or self.cPanel.ui.radioButton_4.isChecked() == True):
                super(GraphicsScene, self).mouseMoveEvent(event)
                self.finalPosition = QtCore.QPointF(event.scenePos()) #- item.rectF.center()
                self._mouse_button = event.buttons()
                if (self._mouse_button == QtCore.Qt.LeftButton):
                    self.x2new = int(self.finalPosition.x())
                    self.y2new = int(self.finalPosition.y())
                    
                    self.renderScene(0) 

        if self.track == True and self.cPanel.ui.radioButton.isChecked() == False:
            self.initialPosition = QtCore.QPointF(event.scenePos()) #- item.rectF.center()   
            self.x1new = int(self.initialPosition.x())
            self.y1new = int(self.initialPosition.y()) 
            self.renderScene(0)       
                
    def mouseReleaseEvent(self, event):        
        if self.mouseEnable == True:
            if self.y2new < self.y1new:
                self.y1new,self.y2new = self.y2new,self.y1new

            if self.x2new < self.x1new:
                self.x1new,self.x2new = self.x2new,self.x1new 
                
            if self.cPanel.ui.comboAccion.currentText() == "Create Roi":
                super(GraphicsScene, self).mouseReleaseEvent(event)
                self.finalPosition = QtCore.QPointF(event.scenePos()) #- item.rectF.center()
                self.x2new = int(self.finalPosition.x())
                self.y2new = int(self.finalPosition.y())
                self.renderScene(0)
            
            if self.cPanel.ui.comboAccion.currentText() == "Reference Maker" and (self.cPanel.ui.radioButton_3.isChecked() == True or self.cPanel.ui.radioButton_4.isChecked() == True):
                super(GraphicsScene, self).mouseReleaseEvent(event)
                self.finalPosition = QtCore.QPointF(event.scenePos()) #- item.rectF.center()
                self.x2new = int(self.finalPosition.x())
                self.y2new = int(self.finalPosition.y())
                self.renderScene(0)
            
            if self.cPanel.ui.comboAccion.currentText() == "Roi Maker":
                self.track = False


            
    def getPoints(self):
        return self.x1new,self.x2new,self.y1new,self.y2new
    
    def renderScene(self,ind):          

        #global imagen2, boxTexto, puntoAux, detalleMouse
        if self.cPanel.ui.comboAccion.currentText() == "Create Roi":
            if (abs(self.x1new-self.x2new) > 1) and (abs(self.y1new-self.y2new) > 1):
                image = self.cPanel.image.copy()
                cv2.rectangle(image,(self.x1new,self.y1new),(self.x2new,self.y2new),(0,255,0),1,4)
                self.cPanel.showImage(image,1)
            else:
                image = self.cPanel.image.copy()
                self.cPanel.showImage(image,1)  
                 
        if self.cPanel.ui.comboAccion.currentText() == "Data Generator":
            coords = self.cPanel.cfgFile.ReadRoiSize(str(self.cPanel.ui.comboReg.currentText()))
            self.x2new = self.x1new + int(coords[0])/2
            self.x1new -= int(coords[0])/2
            self.y2new = self.y1new + int(coords[1])/2
            self.y1new -= int(coords[1])/2
            
            if self.x1new<0:
                d = 0 - self.x1new
                self.x1new = 0
                self.x2new += d
            if self.x2new>1919:
                d = self.x2new - 1919
                self.x2new = 1919
                self.x1new -= d
            if self.y1new<0:
                d = 0 - self.y1new
                self.y1new = 0
                self.y2new += d
            if self.y2new>1079:
                d = self.y2new - 1079
                self.y2new = 1079
                self.y1new -= d
                
            image = self.cPanel.image.copy()

            self.x1new = int(self.x1new)
            self.y1new = int(self.y1new)
            self.x2new = int(self.x2new)
            self.y2new = int(self.y2new)
            cv2.rectangle(image,(self.x1new,self.y1new),(self.x2new,self.y2new),(0,255,0),1,4)
            self.cPanel.showImage(image,1)
            if ind == 1:
                self.cPanel.guardarImg()
            if ind == 0:
                self.saveMsg.emit()
            '''else:
                image = controlPanel.image.copy()
                controlPanel.showImage(image,1)'''
            
        if self.cPanel.ui.comboAccion.currentText() == "Roi Maker":
            self.track = True
            if self.cPanel.ui.comboBox.currentText() == "Añadir Rois":
                if self.cPanel.ui.lineEdit_2.text() != "" and self.cPanel.ui.lineEdit_2.text() != "" and self.cPanel.ui.radioButton_2.isChecked() == True:
                    coords = [int(self.cPanel.ui.lineEdit_2.text()),int(self.cPanel.ui.lineEdit.text())]

                    self.x2new = self.x1new + int(coords[0])/2
                    self.x1new -= int(coords[0])/2
                    self.y2new = self.y1new + int(coords[1])/2
                    self.y1new -= int(coords[1])/2
                    
                    if self.x1new<0:
                        d = 0 - self.x1new
                        self.x1new = 0
                        self.x2new += d
                    if self.x2new>1919:
                        d = self.x2new - 1919
                        self.x2new = 1919
                        self.x1new -= d
                    if self.y1new<0:
                        d = 0 - self.y1new
                        self.y1new = 0
                        self.y2new += d
                    if self.y2new>1079:
                        d = self.y2new - 1079
                        self.y2new = 1079
                        self.y1new -= d
                    
                    image = self.cPanel.image.copy()
                    self.x1new = int(self.x1new)
                    self.y1new = int(self.y1new)
                    self.x2new = int(self.x2new)
                    self.y2new = int(self.y2new)
                    cv2.rectangle(image,(self.x1new,self.y1new),(self.x2new,self.y2new),(0,255,0),1,4)
                    self.cPanel.showImage(image,1)
                    if ind == 1:
                        self.cPanel.guardarImg()
                    if ind == 0:
                        self.saveMsg.emit()
                    '''else:
                        image = controlPanel.image.copy()
                        controlPanel.showImage(image,1)'''
                    
                if self.cPanel.ui.radioButton.isChecked() == True:
                    if (abs(self.x1new-self.x2new) > 1) and (abs(self.y1new-self.y2new) > 1):
                        image = self.cPanel.image.copy()
                        
                        cv2.rectangle(image,(self.x1new,self.y1new),(self.x2new,self.y2new),(0,255,0),1,4)
                        sizex = (int(self.x2new)-int(self.x1new))
                        if sizex < 0:
                            sizex = sizex *-1

                        sizey = (int(self.y2new)-int(self.y1new))
                        if sizey < 0:
                            sizey = sizey *-1
                        
                        self.cPanel.ui.label_6.setText(f"Actual size: {sizex} {sizey}")
                        self.cPanel.showImage(image,1)
                    else:
                        image = self.cPanel.image.copy()
                        self.cPanel.showImage(image,1)  

                self.saveMsg.emit()

            else:
                if ind == 1:
                    lineDel = ""
                    if os.path.exists(f"../Outputs/Rois/{self.cPanel.actualIM.split('/')[-1].split('.')[0] + '.txt'}"):
                        with open (f"../Outputs/Rois/{self.cPanel.actualIM.split('/')[-1].split('.')[0] + '.txt'}","r") as f:
                            lines = f.readlines()
                            for line in lines:
                                x1,y1,x2,y2 = line.split(" ")

                                if int(self.x1new) > int(x1) and int(self.x1new) < int(x2) and int(self.y1new) > int(y1) and int(self.y1new) < int(y2):
                                    lineDel = line
                                    f.close()
                        lineDel = lineDel.strip("\n")
                        #print(self.x1new,self.y1new, lines)
                        if lineDel != "":
                            with open (f"../Outputs/Rois/{self.cPanel.actualIM.split('/')[-1].split('.')[0] + '.txt'}","w") as f:
                               
                                for line in lines:
                                    if line.strip("\n") != lineDel:
                                        f.write(line)
                                
                                f.close()

                            self.cPanel.showImage(cv2.imread(self.cPanel.imageList[self.cPanel.puntero][1]),0)   
                            image = self.cPanel.image.copy()
                            self.cPanel.showImage(image,1) 
                            
        if self.cPanel.ui.comboAccion.currentText() == "Reference Maker" and (self.cPanel.ui.radioButton_3.isChecked() == True or self.cPanel.ui.radioButton_4.isChecked() == True):   
            if (abs(self.x1new-self.x2new) > 1) and (abs(self.y1new-self.y2new) > 1):
                image = self.cPanel.image.copy()
                cv2.rectangle(image,(self.x1new,self.y1new),(self.x2new,self.y2new),(0,255,0),1,4)
                if self.cPanel.ui.radioButton_3.isChecked() == True:
                    self.cPanel.ui.label_pat.setText(f"{self.x1new} {self.y1new} {self.x2new} {self.y2new}")

                if self.cPanel.ui.radioButton_4.isChecked() == True:
                    self.cPanel.ui.label_search.setText(f"{self.x1new} {self.y1new} {self.x2new} {self.y2new}")

                sizex = (int(self.x2new)-int(self.x1new))
                if sizex < 0:
                    sizex = sizex *-1

                sizey = (int(self.y2new)-int(self.y1new))
                if sizey < 0:
                    sizey = sizey *-1
                
                self.cPanel.ui.label_6.setText(f"Actual size: {sizex} {sizey}")
                self.cPanel.showImage(image,1)
            else:
                image = self.cPanel.image.copy()
                self.cPanel.showImage(image,1)

            self.saveMsg.emit()
    
    def __exit__(self, parent=None):        
        super(GraphicsScene, self).__exit__ (parent)




###########################################################
#PANEL DE CONTROL


class ConfControlPanel(QMainWindow):
    #keyPressed = QtCore.pyqtSignal(int)
    def __init__(self, config,guiManager):
        QMainWindow.__init__(self)
        self.appDir = os.path.dirname(os.path.abspath(__file__))
        
        self.GuiManager = guiManager

        #Creacion objetos ventana grafica
        self.ui = self.GuiManager.ui
        
        self.sceneImg = None

        self.configuration = config
        self.imagesDir = self.configuration["inputDir"]
        self.refsDir = self.configuration["ReferencesDir"]
        self.roisDir = self.configuration["RoisDir"]
        self.patternsDir = self.configuration["PatternsDir"]
        self.refsDir = self.configuration["ReferencesDir"]
        self.outputDir = self.configuration["outputDir"]

        #Creacion objeto config
        self.cfgFile = ConfigFile(self.appDir + self.configuration["datasetBuilderCfg"])


        
        self.imageList = []
        self.puntero = 0
        
        

        
    def initialization(self):
        #Widget que se inicializa
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.setTabEnabled(0,True)
        self.ui.tabWidget.setTabEnabled(1,False)
        self.ui.tabWidget.setTabEnabled(2,False)
        self.ui.tabWidget.setTabEnabled(3,False)
        self.ui.tabWidget.setTabEnabled(4,False)
        
        self.ui.buttonDeleteRoi.setEnabled(False)
        self.ui.buttonEditRoi.setEnabled(False)
        self.listWidgetUpdate()
        self.ui.listWidget.currentRowChanged.connect(self.listWidgetSelection)   
        
        #Botones
        self.ui.prevButton.setEnabled(False)
        self.ui.prevButton.clicked.connect(self.prevImg)
        self.ui.nextButton.setEnabled(False)
        self.ui.nextButton.clicked.connect(self.nextImg)
        self.ui.buttonSave.clicked.connect(self.guardarImg)
        self.ui.buttonSave.setEnabled(False)
        self.ui.pushButton_SaveRois.clicked.connect(self.guardarImgNewRoi)
        self.ui.pushButton_SaveRois.setEnabled(False)

        self.ui.pushButton_SaveReference.clicked.connect(self.guardarImgNewRef)
        self.ui.pushButton_SaveReference.setEnabled(False)

        self.ui.radioButton_3.clicked.connect(lambda: self.loadImages)
        self.ui.radioButton_4.clicked.connect(lambda: self.loadImages)

        self.ui.buttonAddRoi.clicked.connect(self.newRoi)
        self.ui.buttonEditRoi.clicked.connect(self.editRoi)
        self.ui.buttonDeleteRoi.clicked.connect(self.deleteRoi)
        
        self.ui.buttonGo.clicked.connect(self.modeChange)
        self.sceneImg.saveMsg.connect(lambda: self.saveButtonEnable(True))
        self.ui.comboReg.currentIndexChanged.connect(lambda: self.saveButtonEnable(False))


        self.ui.pushButton_gen.clicked.connect(self.generateData)

        #Radios de Roi Maker
        self.ui.radioButton_2.clicked.connect(lambda: self.ui.label_6.setEnabled(False))
        self.ui.radioButton.clicked.connect(lambda: self.ui.label_6.setEnabled(True))
        #self.ui.graphicsView.keyPressed.connect(self.on_click)
        self.ui.graphicsView.keyPressEvent = self.on_click
        
        
        
        return
    
    def on_click(self, key):
        if key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Space or int(key.key()) == 32:
            if self.ui.tab_4.isVisible() == True:
                self.ui.pushButton_SaveRois.click()
            elif self.ui.tab_5.isVisible() == True:
                self.ui.pushButton_SaveReference.click()
        


    def printRef(self, patx1, patx2, paty1, paty2, srchx1, srchx2, srchy1, srchy2):
        img = cv2.imread(self.imageList[self.puntero][1])
        img = cv2.rectangle(img,(int(patx1),int(paty1)),(int(patx2),int(paty2)),(255,0,255),2)
        img = cv2.rectangle(img,(int(srchx1),int(srchy1)),(int(srchx2),int(srchy2)),(255,0,255),2)

        self.showImage(img,0)
        

    def modeChange(self):
        modo = str(self.ui.comboAccion.currentText())
        if modo == "Create Roi":
            self.ui.tabWidget.setCurrentIndex(1)
            self.ui.tabWidget.setTabEnabled(0,False)
            self.ui.tabWidget.setTabEnabled(1,True)
            self.ui.tabWidget.setTabEnabled(2,False)
            self.ui.tabWidget.setTabEnabled(3,False)
            self.ui.tabWidget.setTabEnabled(4,False)
            self.startMode(modo)
        if modo == "Data Generator":
            self.ui.tabWidget.setCurrentIndex(2)
            self.ui.tabWidget.setTabEnabled(0,False)
            self.ui.tabWidget.setTabEnabled(1,False)
            self.ui.tabWidget.setTabEnabled(2,True)
            self.ui.tabWidget.setTabEnabled(3,False)
            self.ui.tabWidget.setTabEnabled(4,False)
            self.startMode(modo)
        if modo == "Roi Maker":
            self.ui.tabWidget.setCurrentIndex(3)
            self.ui.tabWidget.setTabEnabled(0,False)
            self.ui.tabWidget.setTabEnabled(1,False)
            self.ui.tabWidget.setTabEnabled(2,False)
            self.ui.tabWidget.setTabEnabled(3,True)
            self.ui.tabWidget.setTabEnabled(4,False)
            self.startMode(modo)
        if modo == "Reference Maker":
            self.ui.tabWidget.setCurrentIndex(4)
            self.ui.tabWidget.setTabEnabled(0,False)
            self.ui.tabWidget.setTabEnabled(1,False)
            self.ui.tabWidget.setTabEnabled(2,False)
            self.ui.tabWidget.setTabEnabled(3,False)
            self.ui.tabWidget.setTabEnabled(4,True)
            self.startMode(modo)
        return
    
    
    def startMode(self , modo):
        quit_msg = "No hay imagen en el directorio, recargar?"
        
        while True:
            
            if modo == "Create Roi":
                ruta = self.patternsDir
                
                self.sceneImg.track = False
                self.ui.graphicsView.setMouseTracking(False)
                
                try:
                    imgdir = os.listdir(ruta)
                    if imgdir==[]:
                        reply = QtWidgets.QMessageBox.question(self, 'Message', quit_msg, QtWidgets.QMessageBox.No , QtWidgets.QMessageBox.Yes)
                        if reply == QtWidgets.QMessageBox.No:
                            break 
                        if reply == QtWidgets.QMessageBox.Yes:
                            continue 
                    
                    else:
                        self.imageList = self.loadImages(ruta , imgdir)
                        if len(self.imageList)>1:
                            self.ui.prevButton.setEnabled(True)
                            self.ui.nextButton.setEnabled(True)
                        break
                except:
                    print("Error, no existe el directorio")
                    break
                    
            if modo == "Data Generator":
                
                self.sceneImg.track = True

                
                ruta = self.imagesDir
                try:
                    imgdir = os.listdir(ruta)
                except Exception as e:
                    print("Error, no existe el directorio: " + str(e))
                    break
                if imgdir==[]:
                    reply = QtWidgets.QMessageBox.question(self, 'Message', quit_msg, QtWidgets.QMessageBox.No , QtWidgets.QMessageBox.Yes)
                    if reply == QtWidgets.QMessageBox.No:
                        break 
                    if reply == QtWidgets.QMessageBox.Yes:
                        continue 
                        
                else:
                    rois = self.cfgFile.ReadRois()
                    if rois != {}:
                        self.ui.graphicsView.setMouseTracking(True)
                    self.ui.comboReg.clear()
                    for value in rois.items():
                        self.ui.comboReg.addItem(value[0]) 
                    self.imageList = self.loadImagesInput(ruta , imgdir)
                    if len(self.imageList)>1:
                        self.ui.prevButton.setEnabled(True)
                        self.ui.nextButton.setEnabled(True) 
                    break
        
            if modo == "Roi Maker":
                
                if self.ui.radioButton.isChecked() == True:
                    self.ui.label_6.setEnabled(True)
                    ruta = self.patternsDir
                
                    self.sceneImg.track = False
                    self.ui.graphicsView.setMouseTracking(False)
                    
                    try:
                        imgdir = os.listdir(ruta)
                        if imgdir==[]:
                            reply = QtWidgets.QMessageBox.question(self, 'Message', quit_msg, QtWidgets.QMessageBox.No , QtWidgets.QMessageBox.Yes)
                            if reply == QtWidgets.QMessageBox.No:
                                break 
                            if reply == QtWidgets.QMessageBox.Yes:
                                continue 
                        
                        else:
                            self.imageList = self.loadImages(ruta , imgdir)
                            if len(self.imageList)>1:
                                self.ui.prevButton.setEnabled(True)
                                self.ui.nextButton.setEnabled(True)
                            break
                    except:
                        print("Error, no existe el directorio")
                        break
                
                if self.ui.radioButton_2.isChecked() == True:
                    
                    self.ui.label_6.setEnabled(False)
                    self.sceneImg.track = True
                
                    ruta = self.imagesDir
                    try:
                        imgdir = os.listdir(ruta)
                    except Exception as e:
                        print("Error, no existe el directorio: " + str(e))
                        break
                    if imgdir==[]:
                        reply = QtWidgets.QMessageBox.question(self, 'Message', quit_msg, QtWidgets.QMessageBox.No , QtWidgets.QMessageBox.Yes)
                        if reply == QtWidgets.QMessageBox.No:
                            break 
                        if reply == QtWidgets.QMessageBox.Yes:
                            continue 
                            
                    else:
                        self.ui.graphicsView.setMouseTracking(True)
                        
                        self.imageList = self.loadImagesInput(ruta , imgdir)
                        if len(self.imageList)>1:
                            self.ui.prevButton.setEnabled(True)
                            self.ui.nextButton.setEnabled(True) 
                        break
                
                else:

                    self.ui.label_6.setEnabled(False)
                    self.sceneImg.track = False
                
                    ruta = self.imagesDir
                    try:
                        imgdir = os.listdir(ruta)
                    except Exception as e:
                        print("Error, no existe el directorio: " + str(e))
                        break
                    if imgdir==[]:
                        reply = QtWidgets.QMessageBox.question(self, 'Message', quit_msg, QtWidgets.QMessageBox.No , QtWidgets.QMessageBox.Yes)
                        if reply == QtWidgets.QMessageBox.No:
                            break 
                        if reply == QtWidgets.QMessageBox.Yes:
                            continue 
                            
                    else:
                        self.ui.graphicsView.setMouseTracking(True)
                        
                        self.imageList = self.loadImagesInput(ruta , imgdir)
                        if len(self.imageList)>1:
                            self.ui.prevButton.setEnabled(True)
                            self.ui.nextButton.setEnabled(True) 
                        break

            if modo == "Reference Maker":
                
                
                ruta = self.patternsDir
            
                self.sceneImg.track = False
                self.ui.graphicsView.setMouseTracking(False)
                
                try:
                    imgdir = os.listdir(ruta)
                    if imgdir==[]:
                        reply = QtWidgets.QMessageBox.question(self, 'Message', quit_msg, QtWidgets.QMessageBox.No , QtWidgets.QMessageBox.Yes)
                        if reply == QtWidgets.QMessageBox.No:
                            break 
                        if reply == QtWidgets.QMessageBox.Yes:
                            continue 
                    
                    else:
                        self.imageList = self.loadImages(ruta , imgdir)
                        if len(self.imageList)>1:
                            self.ui.prevButton.setEnabled(True)
                            self.ui.nextButton.setEnabled(True)
                            try:
                                if self.ui.tab_5.isVisible() or self.ui.tab_4.isVisible():
                                    if os.path.exists(f"{self.refsDir}{self.actualIM.split('/')[-1].split('.')[0] + '.txt'}"):
                                            with open(f"{self.refsDir}{self.actualIM.split('/')[-1].split('.')[0] + '.txt'}","r") as f:
                                                for line in f.readlines():
                                                    #print(line)
                                                    patx1,paty1,patx2,paty2,srchx1,srchy1,srchx2,srchy2 = line.split(" ")
                                                    
                                                    self.ui.label_pat.setText(f"{patx1} {paty1} {patx2} {paty2}")
                                                    self.ui.label_search.setText(f"{srchx1} {srchy1} {srchx2} {srchy2}")
                            except:
                                pass
                        break
                except Exception as e:
                    print(f"Error, no existe el directorio {e}")
                    break
                            
                

                    
    def getVariableSize(self):
        x1new,x2new,y1new,y2new = self.sceneImg.getPoints()
        return x1new,x2new,y1new,y2new


    def loadImagesInput(self , ruta , imgdir):
        imgdir.sort()
        for d in imgdir:
            fullPathD = os.path.join(ruta,d)
            for imageName in os.listdir(fullPathD):
                fullPath = os.path.join(fullPathD, imageName)
                self.imageList.append([imageName, fullPath])

        self.puntero = 0
        self.actualIM = self.imageList[self.puntero][1]
        self.showImage(cv2.imread(self.imageList[self.puntero][1]),0)    
        return self.imageList

               
    def loadImages(self , ruta , imgdir):
        imgdir.sort()
        for imageName in imgdir:
            fullPath = os.path.join(ruta,imageName)
            self.imageList.append([imageName, fullPath])
        self.puntero = 0
        self.actualIM = self.imageList[self.puntero][1]
        self.showImage(cv2.imread(self.imageList[self.puntero][1]),0)    
        return self.imageList
    
    
    def prevImg(self):
        self.ui.label_pat.setText("0 0 0 0")
        self.ui.label_search.setText("0 0 0 0")

        self.ui.label_6.setText("Actual size:")
        if self.puntero==0:
            _ = QtWidgets.QMessageBox.question(self, 'Advertencia',"Has llegado a la primera imagen",QtWidgets.QMessageBox.Abort)
            self.puntero=len(self.imageList)-1
        else:
            self.puntero-=1
        self.actualIM = self.imageList[self.puntero][1]

        # Si se esta en modo Reference Maker ponemos la referencia correspondiente en las labels
        try:
            if self.ui.tab_5.isVisible() or self.ui.tab_4.isVisible():
                if os.path.exists(f"{self.refsDir}{self.actualIM.split('/')[-1].split('.')[0] + '.txt'}"):
                        with open(f"{self.refsDir}{self.actualIM.split('/')[-1].split('.')[0] + '.txt'}","r") as f:
                            for line in f.readlines():
                                #print(line)
                                patx1,paty1,patx2,paty2,srchx1,srchy1,srchx2,srchy2 = line.split(" ")
                                
                                self.ui.label_pat.setText(f"{patx1} {paty1} {patx2} {paty2}")
                                self.ui.label_search.setText(f"{srchx1} {srchy1} {srchx2} {srchy2}")
        except:
            pass
        self.showImage(cv2.imread(self.imageList[self.puntero][1]),0)
        self.saveButtonEnable(False)
        
        return 
    
    
    def nextImg(self):
        self.ui.label_pat.setText("0 0 0 0")
        self.ui.label_search.setText("0 0 0 0")

        self.ui.label_6.setText("Actual size:")
        if self.puntero >=len(self.imageList)-1:
            _ = QtWidgets.QMessageBox.question(self, 'Advertencia',"Has llegado a la ultima imagen",QtWidgets.QMessageBox.Abort)
            self.puntero=0
        else:
            self.puntero+=1

        self.actualIM = self.imageList[self.puntero][1]
        # Si se esta en modo Reference Maker ponemos la referencia correspondiente en las labels
        try:
            if self.ui.tab_5.isVisible() or self.ui.tab_4.isVisible():
                if os.path.exists(f"{self.refsDir}{self.actualIM.split('/')[-1].split('.')[0] + '.txt'}"):
                        with open(f"{self.refsDir}{self.actualIM.split('/')[-1].split('.')[0] + '.txt'}","r") as f:
                            for line in f.readlines():
                                #print(line)
                                patx1,paty1,patx2,paty2,srchx1,srchy1,srchx2,srchy2 = line.split(" ")
                                
                                self.ui.label_pat.setText(f"{patx1} {paty1} {patx2} {paty2}")
                                self.ui.label_search.setText(f"{srchx1} {srchy1} {srchx2} {srchy2}")
        except:
            pass

        self.showImage(cv2.imread(self.imageList[self.puntero][1]),0)
        self.saveButtonEnable(False)
        

        return 
    
    
    def showImage(self , img , flag):
        self.sceneImg.mouseEnable = True
        self.sceneImg.clear()
        
        if self.ui.tab_4.isVisible() or self.ui.tab_5.isVisible():
                if os.path.exists(f"{self.roisDir}{self.actualIM.split('/')[-1].split('.')[0] + '.txt'}"):
                    with open(f"{self.roisDir}{self.actualIM.split('/')[-1].split('.')[0] + '.txt'}","r") as f:
                        for line in f.readlines():
                            x1,y1,x2,y2 = line.split(" ")

                            cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(255,0,0),1,4)
    
        if self.ui.pushButton_SaveReference.isEnabled() == True and (self.ui.tab_5.isVisible() or self.ui.tab_4.isVisible()):
            patx1, paty1, patx2, paty2 = self.ui.label_pat.text().split(" ")
            srchx1, srchy1, srchx2, srchy2 = self.ui.label_search.text().split(" ")

            cv2.rectangle(img,(int(patx1),int(paty1)),(int(patx2),int(paty2)),(255,90,255),1,4)
            cv2.rectangle(img,(int(srchx1),int(srchy1)),(int(srchx2),int(srchy2)),(255,90,255),1,4)
        elif self.ui.tab_5.isVisible() or self.ui.tab_4.isVisible():
            
            if os.path.exists(f"{self.refsDir}{self.actualIM.split('/')[-1].split('.')[0] + '.txt'}"):
                    with open(f"{self.refsDir}{self.actualIM.split('/')[-1].split('.')[0] + '.txt'}","r") as f:
                        for line in f.readlines():
                            try:
                                #print(line)
                                patx1,paty1,patx2,paty2,srchx1,srchy1,srchx2,srchy2 = line.split(" ")
                                
                                cv2.rectangle(img,(int(patx1),int(paty1)),(int(patx2),int(paty2)),(255,90,255),1,4)
                                cv2.rectangle(img,(int(srchx1),int(srchy1)),(int(srchx2),int(srchy2)),(255,90,255),1,4)

                            except:
                                pass

        #Para no sobreescribir lo que se pinta, se usa un flag
        if flag != 1:
            self.image = img.copy()
        

        border = 8
        resizeWidth = self.ui.graphicsView.width()-border
        resizeHeight = int(resizeWidth * (9.0/16.0))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   
        height, width, channels = img.shape
        bytesPerLine = channels * width
        frame = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888) 
        self.sceneImg.addPixmap(QPixmap.fromImage(frame))
        self.sceneImg.update()
        self.ui.graphicsView.setScene(self.sceneImg)
        QApplication.processEvents()
        
    
    
    
    #####################################
    #MODULO RECORTE
    
    def saveButtonEnable(self , bool):
        self.ui.buttonSave.setEnabled(bool)
        self.ui.pushButton_SaveRois.setEnabled(bool)
        self.ui.pushButton_SaveReference.setEnabled(bool)
        return
    
    def guardarImg(self):
        selloTemporal = str(time.strftime("%Y%m%d_%H%M%S_"))
        img = self.image.copy()
        var = str(self.ui.comboReg.currentText())
        
        sizex , sizey = self.cfgFile.ReadRoiSize(var)
        x1,_,y1,_ = self.sceneImg.getPoints()
        img = img[y1:y1+int(sizey),x1:x1+int(sizex)]
        
        ruta = self.outputDir + var + "/"
        if os.path.exists(ruta):
                pass
        else:
                os.makedirs(ruta)
        n = len(os.listdir(ruta))
        cv2.imwrite(ruta + str(n+1) + selloTemporal + ".jpeg",img)
        self.saveButtonEnable(False)
        self.ui.graphicsView.setMouseTracking(True)
        #img = self.image
        return
        
    def guardarImgNewRoi(self):
        selloTemporal = str(time.strftime("%Y%m%d_%H%M%S_"))
        img = self.image.copy()
        self.actualIM = self.actualIM.split("/")[-1]
        if self.ui.label_6.isEnabled() == True:
            _, _, sizex,sizey = self.ui.label_6.text().split(" ")

        else:
            sizex = self.ui.lineEdit_2.text()
            sizey = self.ui.lineEdit.text()

        x1,x2,y1,y2 = self.sceneImg.getPoints()
        img = img[y1:y1+int(sizey),x1:x1+int(sizex)]
        
        ruta = self.roisDir
        if os.path.exists(ruta):
                pass
        else:
                os.makedirs(ruta)
        n = len(os.listdir(ruta))
        #cv2.imwrite(ruta + str(n+1) + selloTemporal + ".jpeg",img)
        self.saveButtonEnable(False)
        self.ui.graphicsView.setMouseTracking(True)
        #img = self.image

        if os.path.exists(ruta + self.actualIM.split(".")[0] + ".txt"):
            with open(ruta + self.actualIM.split(".")[0] + ".txt","a") as f:
                
                f.write(str(x1) + " " + str(y1) + " " +  str(x2) + " " +  str(y2) + "\n")
                f.close()
        else:
            os.system(f"touch {ruta}{self.actualIM.split('.')[0] + '.txt'}")
            with open(ruta + self.actualIM.split(".")[0] + ".txt","w") as f:
                f.truncate(0)
                f.write(str(x1) + " " + str(y1) + " " +  str(x2) + " " +  str(y2) + "\n")
                f.close()


        image = self.image.copy()
        self.showImage(image,1) 


        return
    
    

    def guardarImgNewRef(self):
        selloTemporal = str(time.strftime("%Y%m%d_%H%M%S_"))
        img = self.image.copy()
        self.actualIM = self.actualIM.split("/")[-1]
        if self.ui.label_6.isEnabled() == True:
            _, _, sizex,sizey = self.ui.label_6.text().split(" ")

        else:
            sizex = self.ui.lineEdit_2.text()
            sizey = self.ui.lineEdit.text()

        patx1, paty1, patx2, paty2 = self.ui.label_pat.text().split(" ")
        srchx1, srchy1, srchx2, srchy2 = self.ui.label_search.text().split(" ")
        
        ruta = self.refsDir
        if os.path.exists(ruta):
                pass
        else:
                os.makedirs(ruta)
        n = len(os.listdir(ruta))
        #cv2.imwrite(ruta + str(n+1) + selloTemporal + ".jpeg",img)
        self.saveButtonEnable(False)
        self.ui.graphicsView.setMouseTracking(True)
        #img = self.image

        if os.path.exists(ruta + self.actualIM.split(".")[0] + ".txt"):
            with open(ruta + self.actualIM.split(".")[0] + ".txt","a") as f:
                f.truncate(0)
                f.write(str(patx1) + " " + str(paty1) + " " +  str(patx2) + " " +  str(paty2) + " " + str(srchx1) + " " + str(srchy1) + " " +  str(srchx2) + " " +  str(srchy2) + "\n")
                f.close()
        else:
            os.system(f"touch {ruta}{self.actualIM.split('.')[0] + '.txt'}")
            with open(ruta + self.actualIM.split(".")[0] + ".txt","w") as f:
                f.truncate(0)
                f.write(str(patx1) + " " + str(paty1) + " " +  str(patx2) + " " +  str(paty2) + " " + str(srchx1) + " " + str(srchy1) + " " +  str(srchx2) + " " +  str(srchy2) + "\n")
                f.close()


        image = cv2.imread(self.imageList[self.puntero][1])
        #self.printRef(patx1, patx2, paty1, paty2, srchx1, srchx2, srchy1, srchy2)
        self.showImage(image,0)


        return
    
    
    
    
    
    
    #####################################
    #MODULO ROIS
        
    def listWidgetUpdate(self):
        rois = self.cfgFile.ReadRois()
        self.ui.listWidget.clear()
        for value in rois.items():
            val = value[0]
            size = self.cfgFile.ReadRoiSize(val)
            self.ui.listWidget.addItem(val + " : " + size[0] + " " + size[1])
        if self.ui.listWidget.count()<1:
            self.ui.buttonDeleteRoi.setEnabled(False)
            self.ui.buttonEditRoi.setEnabled(False)
        #sizes = self.cfgFile.ReadRoiSize(roi)
        
        return
    
    def listWidgetSelection(self):
        if self.ui.listWidget.count()<1:
            self.ui.buttonDeleteRoi.setEnabled(False)
            self.ui.buttonEditRoi.setEnabled(False)
        else:
            self.ui.buttonDeleteRoi.setEnabled(True)
            self.ui.buttonEditRoi.setEnabled(True)
            
    def newRoi(self):
        x1new,x2new,y1new,y2new = self.sceneImg.getPoints()
        width = (abs(x1new-x2new))
        height = (abs(y1new-y2new))
        if (width < 1) and (height < 1):
            _ = QtWidgets.QMessageBox.question(self, 'Error',"Selecciona region primero",QtWidgets.QMessageBox.Abort)
            return
        text, okPressed = QInputDialog.getText(self, "Roi","Introduce nombre de ROI:", QLineEdit.Normal, "")
        text = str(text)
        if okPressed and text != '':
            listRoi = self.cfgFile.ReadRois()
            try:
                listRoi[text]
                _ = QtWidgets.QMessageBox.question(self, 'Error',"Roi ya existente",QtWidgets.QMessageBox.Abort)
                return
            except:
                self.cfgFile.WriteRois(text)
                self.cfgFile.WriteRoiSize(text , width , height)
                self.listWidgetUpdate()
        
    def editRoi(self):
        x1new,x2new,y1new,y2new = self.sceneImg.getPoints()
        width = (abs(x1new-x2new))
        height = (abs(y1new-y2new))
        if (width < 1) and (height < 1):
            _ = QtWidgets.QMessageBox.question(self, 'Error',"Selecciona region primero",QtWidgets.QMessageBox.Abort)
            return
        try:
            text = str(self.ui.listWidget.currentItem().text()).split(" ")[0]
        except:
            print("No se ha seleccionado ROI")
            return
        msg2 = "Sobreescribir dimensiones de ROI?"
        reply = QtWidgets.QMessageBox.question(None, 'Message', msg2, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.cfgFile.WriteRois(text)
            self.cfgFile.WriteRoiSize(text , width , height)
            self.listWidgetUpdate()
            self.ui.buttonDeleteRoi.setEnabled(False)
            self.ui.buttonEditRoi.setEnabled(False)
        else:
            pass
        
        return
    
    def deleteRoi(self):
        try:
            text = str(self.ui.listWidget.currentItem().text()).split(" ")[0]
        except:
            print("No se ha seleccionado ROI")
        msg2 = "Eliminar ROI?"
        reply = QtWidgets.QMessageBox.question(None, 'Message', msg2, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.cfgFile.RemoveRois(text)
            self.listWidgetUpdate()
        return


    #####################################
    #MODULO ROI MAKER
        
    def listWidgetUpdateM(self):
        rois = self.cfgFile.ReadRois()
        self.ui.listWidget.clear()
        for value in rois.items():
            val = value[0]
            size = self.cfgFile.ReadRoiSize(val)
            self.ui.listWidget.addItem(val + " : " + size[0] + " " + size[1])
        if self.ui.listWidget.count()<1:
            self.ui.buttonDeleteRoi.setEnabled(False)
            self.ui.buttonEditRoi.setEnabled(False)
        #sizes = self.cfgFile.ReadRoiSize(roi)
        
        return
    
    def listWidgetSelectionM(self):
        if self.ui.listWidget.count()<1:
            self.ui.buttonDeleteRoi.setEnabled(False)
            self.ui.buttonEditRoi.setEnabled(False)
        else:
            self.ui.buttonDeleteRoi.setEnabled(True)
            self.ui.buttonEditRoi.setEnabled(True)
            
    def newRoiM(self):
        x1new,x2new,y1new,y2new = self.sceneImg.getPoints()
        width = (abs(x1new-x2new))
        height = (abs(y1new-y2new))
        if (width < 1) and (height < 1):
            _ = QtWidgets.QMessageBox.question(self, 'Error',"Selecciona region primero",QtWidgets.QMessageBox.Abort)
            return
        text, okPressed = QInputDialog.getText(self, "Roi","Introduce nombre de ROI:", QLineEdit.Normal, "")
        text = str(text)
        if okPressed and text != '':
            listRoi = self.cfgFile.ReadRois()
            try:
                listRoi[text]
                _ = QtWidgets.QMessageBox.question(self, 'Error',"Roi ya existente",QtWidgets.QMessageBox.Abort)
                return
            except:
                self.cfgFile.WriteRois(text)
                self.cfgFile.WriteRoiSize(text , width , height)
                self.listWidgetUpdate()
        
    def editRoiM(self):
        x1new,x2new,y1new,y2new = self.sceneImg.getPoints()
        width = (abs(x1new-x2new))
        height = (abs(y1new-y2new))
        if (width < 1) and (height < 1):
            _ = QtWidgets.QMessageBox.question(self, 'Error',"Selecciona region primero",QtWidgets.QMessageBox.Abort)
            return
        try:
            text = str(self.ui.listWidget.currentItem().text()).split(" ")[0]
        except:
            print("No se ha seleccionado ROI")
            return
        msg2 = "Sobreescribir dimensiones de ROI?"
        reply = QtWidgets.QMessageBox.question(None, 'Message', msg2, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.cfgFile.WriteRois(text)
            self.cfgFile.WriteRoiSize(text , width , height)
            self.listWidgetUpdate()
            self.ui.buttonDeleteRoi.setEnabled(False)
            self.ui.buttonEditRoi.setEnabled(False)
        else:
            pass
        
        return
    
    def deleteRoiM(self):
        try:
            text = str(self.ui.listWidget.currentItem().text()).split(" ")[0]
        except:
            print("No se ha seleccionado ROI")
        msg2 = "Eliminar ROI?"
        reply = QtWidgets.QMessageBox.question(None, 'Message', msg2, QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.cfgFile.RemoveRois(text)
            self.listWidgetUpdate()
        return

    def generateData(self):
        dirs = os.listdir(self.outputDir)
        
        for d in dirs:
            if d != "Gen":
                imageList = os.listdir(self.outputDir + str(d))
                for i in imageList:
                    image = load_img(self.outputDir + str(d) + "/" + i)
                    image = img_to_array(image)
                    # image=image[651:803,343:567]
                    image = np.expand_dims(image, axis=0)
                    # construct the image generator for data augmentation then
                    # initialize the total number of images generated thus far
                    if self.ui.radioButton_sampT.isChecked():
                        samp = True
                    else:
                        samp = False

                    if self.ui.radioButton_hflipT.isChecked():
                        hflip = True
                    else:
                        hflip = False
                        
                    if self.ui.radioButton_vflipT.isChecked():
                        vflip = True
                    else:
                        vflip = False
                    
                    csr = float(self.ui.lineEdit_csr.text())
                    hsr = float(self.ui.lineEdit_hsr.text())
                    wsr = float(self.ui.lineEdit_wsr.text())
                    fmode = str(self.ui.lineEdit_fmode.text())
                    rrange = int(self.ui.spinBox_rRange.text())
                    zep = float(self.ui.lineEdit_8.text())

                    
                    aug = ImageDataGenerator(samplewise_center= samp,channel_shift_range= csr,height_shift_range=hsr,width_shift_range=wsr,fill_mode=fmode,rotation_range=rrange,horizontal_flip=hflip,vertical_flip=vflip,zca_epsilon=zep)
                    
                    self.create_empty_folder(f"{self.outputDir}Gen/{d}/")

                    imageGen = aug.flow(image, batch_size=1, save_to_dir=f"{self.outputDir}Gen/{d}/",
            save_prefix=i, save_format="jpeg")
                    
                    total = 0
                    for image in imageGen:

                        cv2.imwrite(f"{self.outputDir}Gen/" + str(d) + "/" + i,image)
                        total +=1

                        if total == 10:
                            break

                    
                    
                

    def create_empty_folder(self,folder_name):
        if not os.path.exists(folder_name):
            try:
                os.makedirs(folder_name)
            except Exception as e:
                print("ERROR: Aviso creando directorio: %s" % e)
        return    



