import numpy as np
import os
import fnmatch
import shutil
# USAGE
# python classify.py --model pokedex.model --labelbin lb.pickle --image examples/charmander_counter.png
# import the necessary packages
from keras.utils import img_to_array
from keras.models import load_model
import numpy as np
import pickle
import cv2
import os
import fnmatch
#from Logger import logger
import shutil
from keras import backend as K
from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QApplication
K.clear_session()

class MainValidation(QThread):
    def __init__(self,configGeneral,offset,plainText,uiMan):
        QThread.__init__(self)
        self.plainText = plainText
        self.uiMan = uiMan
        self.configGeneral = configGeneral
        self.offset = offset
        self.datasetDir = str(self.configGeneral["outputDir"])
        self.modelPath = str(self.configGeneral["modelPath"])
        self.callback_path = str(self.configGeneral["modelPath"]) + "/best_model.h5"
        self.roisDir = self.configGeneral["RoisDir"]
        self.referencesDir = self.configGeneral["ReferencesDir"]
        self.validationDir = self.configGeneral["ValidationDir"]
        self.patternsDir = self.configGeneral["PatternsDir"]
        self.inputDir = self.configGeneral["inputDir"]
        self.outputDir = self.configGeneral["outputDir"]

    def coordsRoi(self,fil):


        rois = []
        x1,x2,y1,y1=0,0,0,0
        f = open(self.roisDir + fil,'r')
        
        for line in f:
            rois.append(line) 
            xmin, ymin, xmax, ymax = map(int,line.split())
            
        f.close()

        return rois


    def get_image_list(self,images_folder):
        images_list = set()
        images_names = set()
        if os.path.exists(images_folder):
            images_names = fnmatch.filter(os.listdir(images_folder), '*.jpeg')
            images_names.sort()
        for image_name in images_names:
            full_path = os.path.join(images_folder, image_name)
            images_list.add((image_name, full_path))
        return images_list


    def create_empty_folder(self,folder_name):
        try:
            shutil.rmtree(folder_name)
        except Exception as e:
            print("ERROR: Aviso eliminando directorio: %s" % e)
            self.plainText.appendPlainText("ERROR: Aviso eliminando directorio: %s" % e)
            QApplication.processEvents()
        if not os.path.exists(folder_name):
            try:
                os.makedirs(folder_name)
            except Exception as e:
                print("ERROR: Aviso creando directorio: %s" % e)
                self.plainText.appendPlainText("ERROR: Aviso creando directorio: %s" % e)
                QApplication.processEvents()
        return

    def CalcularOffsets(self,img,pat,pos,srch):
        dx = 0
        dy = 0


        # Leer imagen patron
        patternImage = pat
        if patternImage is None:
            print("No hay imagen patron")
            self.plainText.appendPlainText("No hay imagen patron")
            QApplication.processEvents()
            return dx, dy
        x0, y0, x1, y1, = map(int,pos)
        xmin, ymin, xmax, ymax = map(int,srch)


        posRoi = patternImage[y0:y1,x0:x1]    
        imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        searchRoi = imgGray[ymin:ymax, xmin:xmax]

        res = cv2.matchTemplate(searchRoi, posRoi, cv2.TM_CCOEFF_NORMED)
        _min_val, _max_val, _min_loc, max_loc = cv2.minMaxLoc(res)
        xl = xmin + max_loc[0]
        yl = ymin + max_loc[1]
        print(_max_val*100)
        self.plainText.appendPlainText(str(_max_val*100))
        QApplication.processEvents()

        dx = xl - x0; dy = yl - y0

        cv2.rectangle(self.image2,(xmin,ymin),(xmax,ymax),(255,0,0),2,4)
        cv2.rectangle(self.image2,(xl,yl),(x1+dx,y1+dy),(255,0,0),2,4)
        #cv2.rectangle(img,( xmin + max_loc[0],ymin + max_loc[1]),(xmax + max_loc[0], ymax + max_loc[1]),(0,255,255),2,4)

        
        return dx, dy

    def getOffset(self,fil):

        x0,x1,y0,y1=0,0,0,0
        xmin, ymin, xmax, ymax=0,0,0,0
        
        f = open(self.referencesDir + fil,'r')

        x0, y0, x1, y1, xmin, ymin, xmax, ymax = map(int,f.readline().split()) 
        f.close()

        pos = [x0,y0,x1,y1]
        srch = [xmin,ymin,xmax,ymax]


        return pos, srch


    def GetImageList(self,imagesFolder):
        imagesList = []
        #imagesFolder = appDir + "/../TestImages/C01_" + model
        #imagesFolder = "/media/mdlago/Seagate Expansion Drive/CopoHR2/" + model
        imagesNames = []
        if os.path.exists(imagesFolder):
            imagesNames = fnmatch.filter(os.listdir(imagesFolder),'*.jpeg')
            imagesNames.sort()
        for imageName in imagesNames:
            fullPath = os.path.join(imagesFolder,imageName)
            imagesList.append([imageName, fullPath])
        return imagesList



    def start(self):

        imageList = self.get_image_list(self.validationDir)
        nFiles = len(imageList)

        inputDir = os.listdir(self.inputDir)
        self.offset = True

        try:
            directorios = set(os.listdir(self.patternsDir))
        except:
            self.offset = False

        roisDir = set(os.listdir(self.roisDir))
        refsDir = set(os.listdir(self.referencesDir))
        created = False

        modlist = set(os.listdir(self.modelPath))
        model, pick = "", ""

        for element in modlist:
            if ".model" in element or ".h5" in element:
                model = element
            if ".pickle" in element:
                pick = element
        model = self.modelPath + str(model)
        labels = self.modelPath + str(pick)

        print("[INFO] loading network...")
        self.plainText.appendPlainText("[INFO] loading network...")
        QApplication.processEvents()

        model = load_model(model, compile=False)
        lb = pickle.loads(open(labels, "rb").read())
        
        folder_name = self.validationDir + "/"


        if not os.path.exists(folder_name):
            try:
                os.makedirs(folder_name)
            except Exception as e:
                print("ERROR: Aviso creando directorio: %s" % e)
                self.plainText.appendPlainText("ERROR: Aviso creando directorio: %s" % e)
                QApplication.processEvents()

        for file in directorios:
            rois = None
            pos, srch = None, None
            for roi in roisDir:
                if roi.split("Pattern")[1].strip(".txt") == file.split("Pattern")[1].strip(".jpeg"):
                    rois = self.coordsRoi(roi)
                    coordenadas = self.coordsRoi(roi)
                    break
            if self.offset:
                for ref in refsDir:
                    if ref.split("Pattern")[1].strip(".txt") == file.split("Pattern")[1].strip(".jpeg"):
                        pos, srch = self.getOffset(ref)
                        break

            for dr in inputDir:
                c = 0
                if not created:
                    self.create_empty_folder(self.validationDir + str(dr) + "/")
                if dr == inputDir[-1]:
                    created = True

                
                
                nFile = 0
                nRois = len(rois)
                
                for imageName, imageFullName in imageList:
                    etiqueta, roi = [], []
                    self.uiMan.refreshTables()
                    QApplication.processEvents()

                    if file.split("Pattern")[1].strip(".txt") in imageName:
                        nRoi = 0
                        nFile += 1
                        img = cv2.imread(imageFullName)
                        image = img
                        self.image2 = img.copy()
                        imgPat = cv2.imread(self.patternsDir + file,0)

                        for z in range(len(rois)):
                            nRoi += 1
                        

                            rois[z] = rois[z].strip("\n")
                            xmin, ymin, xmax, ymax = map(int, rois[z].split(" "))


                            # Dimensiones de los recortes. Vamos a tratar de que la dimension mayor sea 100px manteniendo relacion aspecto
                            roiWidth = xmax - xmin
                            roiHeight = ymax - ymin
                            
                            if roiHeight <0:
                                roiHeight = roiHeight * -1

                            if roiWidth <0:
                                roiWidth = roiWidth * -1
                            
                            if roiWidth > roiHeight:
                                cropWidth = 100
                                cropHeight = int(roiHeight * 100/roiWidth)
                            else:
                                cropHeight = 100
                                cropWidth = int(roiWidth * 100/roiHeight)

                            
                            print("\nProcessing %s file %i of %i Roi %i of %i" % (imageName, nFile, nFiles,nRoi,nRois))
                            self.plainText.appendPlainText("\nProcessing %s file %i of %i Roi %i of %i" % (imageName, nFile, nFiles,nRoi,nRois))
                                                       
                            
                            
                            if self.offset:
                                dx, dy = self.CalcularOffsets(img,imgPat,pos,srch)
                            else:
                                dx, dy = 0, 0

                            ymin=ymin+dy
                            ymax=ymax+dy
                            xmin=xmin+dx
                            xmax=xmax+dx

                            if xmax > 1920:
                                dif = xmax - 1920
                                xmax = xmax - dif
                                xmin = xmin - dif
                            if ymax > 1080:
                                dif = ymax - 1080
                                ymax = ymax - dif
                                ymin = ymin - dif
                            if xmin < 0:
                                xmax = xmax - (xmin)
                                xmin = xmin - xmin
                            if ymin < 0:
                                ymax = ymax - (ymin)
                                ymin = ymin - ymin


                            # extract roi and resize
                            print("Tamanho imagen: " + str(cropHeight) + ", " + str(cropWidth))
                            self.plainText.appendPlainText("Tamanho imagen: " + str(cropHeight) + ", " + str(cropWidth))
                            
                            imgCrop = image.copy()[ymin:ymax,xmin:xmax]


                            imageC = imgCrop
                            imageC = cv2.resize(imgCrop, (cropWidth, cropHeight))
                            # alpha = 1.5 # Contrast control (1.0-3.0)
                            # beta = 0 # Brightness control (0-100)
                            # image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

                            output = imageC.copy()
                            imageC = imageC.astype("float") / 255.0
                            imageC = img_to_array(imageC)
                            imageC = np.expand_dims(imageC, axis=0)

                            # classify the input image
                            print("[INFO] classifying image...")
                            self.plainText.appendPlainText("[INFO] classifying image...")
                            
                            proba = model.predict(imageC)[0]
                            idx = np.argmax(proba)
                            
                            label = lb.classes_[idx]

                            # build the label and draw the label on the image
                            label = "{}: {:.2f}%".format(label, proba[idx] * 100)
                            label = label.split(":")
                            etiqueta.append(label[0])
                            etiqueta = etiqueta
                            roi.append([ xmin,ymin,xmax,ymax])
                            directorio = label[0]
                            
                            
                            for j in range(len(etiqueta)):
                            
                                if etiqueta[j]=="Bien":
                                    cv2.rectangle(self.image2,(roi[j][0],roi[j][1]),(roi[j][2],roi[j][3]),(0,255,0),1,4)
                                
                                elif etiqueta[j]=="Defecto":
                                    cv2.rectangle(self.image2,(roi[j][0],roi[j][1]),(roi[j][2],roi[j][3]),(0,0,255),1,4)
                                    cv2.putText(self.image2, etiqueta[j], (roi[j][0],roi[j][1]-50), cv2.FONT_HERSHEY_PLAIN, 2.0, (0,255,255), thickness=2)
                                    
                                else:
                                    
                                    cv2.rectangle(self.image2,(roi[j][0],roi[j][1]),(roi[j][2],roi[j][3]),(0,255,0),1,4)
                                    cv2.putText(self.image2, etiqueta[j], (roi[j][0],roi[j][1]-50), cv2.FONT_HERSHEY_PLAIN, 2.0, (0,255,255), thickness=2)
                            
                                if len(etiqueta)==1:
                                    if not os.path.exists(folder_name+directorio):
                                        try:
                                            os.makedirs(folder_name+directorio)
                                        except Exception as e:
                                            print("ERROR: Aviso creando directorio: %s" % e)
                                            self.plainText.appendPlainText("ERROR: Aviso creando directorio: %s" % e)
                                           

                                    
                                    # cv2.imwrite(folder_name+directorio+"/"+imageName,image2)
                                    
                                    cv2.imwrite(folder_name+directorio+"/"+imageName,self.image2)
                                    self.uiMan.refreshTables()
                                    
                                                                        
                                else:
                                    if not os.path.exists(folder_name + "Mix"):
                                            try:
                                                os.makedirs(folder_name+"Mix")
                                            except Exception as e:
                                                print("ERROR: Aviso creando directorio: %s" % e)
                                                self.plainText.appendPlainText("ERROR: Aviso creando directorio: %s" % e)
                                                                        

                                    # cv2.imwrite(folder_name+"Mix"+"/"+imageName,image2)
                                    
                                    cv2.imwrite(folder_name+"Mix"+"/"+imageName,self.image2)
                                    
                                    try:
                                        if os.path.isfile(folder_name + 'Bien' + '/' + imageName):
                                            os.system("rm {}".format(folder_name + 'Bien' + '/' + imageName))
                                    except:
                                        pass
                                    try:
                                        if os.path.isfile(folder_name + 'Defecto' + '/' + imageName):
                                            os.system("rm {}".format(folder_name + 'Defecto' + '/' + imageName))
                                    except:
                                        pass
                            
                            print("[INFO] {}".format(label))
                            self.plainText.appendPlainText("[INFO] {}".format(label))
                            QApplication.processEvents()

                    
                            
                        





                    
