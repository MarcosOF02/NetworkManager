from PyQt6.QtWidgets import QApplication
import os
import fnmatch
import time
import cv2
import shutil
from PyQt6.QtCore import QThread

class samplesExtraction(QThread):

    def __init__(self,appdir, configGeneral, inputDir ,roisDir,offset,referencesDir, patternDir,outputDir,draw,plainText):
        QThread.__init__(self)
        self.appdir, self.inputDir ,self.roisDir,self.offset,self.referencesDir, self.patternDir, self.outputDir ,self.draw, self.PlainText = appdir, inputDir ,roisDir,offset,referencesDir, patternDir, outputDir ,draw, plainText



    def coordsRoi(self, fil):


        rois = []
        x1,x2,y1,y1=0,0,0,0
        f = open(self.roisDir + fil,'r')
        
        for line in f:
            rois.append(line) 
            
        f.close()
        
        return rois


    def get_image_list(self, images_folder):
        images_list = []
        images_names = []
        if os.path.exists(images_folder):
            images_names = fnmatch.filter(os.listdir(images_folder), '*.jpeg')
            images_names.sort()
        for image_name in images_names:
            full_path = os.path.join(images_folder, image_name)
            images_list.append([image_name, full_path])
        return images_list


    def create_empty_folder(self, folder_name):
        try:
            shutil.rmtree(folder_name)
        except Exception as e:
            print("ERROR: Aviso eliminando directorio: %s" % e)
            self.PlainText.appendPlainText("ERROR: Aviso eliminando directorio: %s" % e)
            QApplication.processEvents()
        if not os.path.exists(folder_name):
            try:
                os.makedirs(folder_name)
            except Exception as e:
                print("ERROR: Aviso creando directorio: %s" % e)
                self.PlainText.appendPlainText("ERROR: Aviso creando directorio: %s" % e)
                QApplication.processEvents()
        return

    def CalcularOffsets(self, img,pat,pos,srch):
        dx = 0
        dy = 0


        # Leer imagen patron
        patternImage = pat.copy()
        
        if patternImage is None:
            print("No hay imagen patron")
            self.PlainText.appendPlainText("No hay imagen patron")
            QApplication.processEvents()
            return dx, dy
        x0, y0, x1, y1 = map(int,pos)
        xmin, ymin, xmax, ymax =map(int,srch)

        
        posRoi = patternImage[y0:y1,x0:x1]    
        imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        searchRoi = imgGray[ymin:ymax, xmin:xmax]
        

        res = cv2.matchTemplate(searchRoi, posRoi, cv2.TM_CCOEFF_NORMED)
        _min_val, _max_val, _min_loc, max_loc = cv2.minMaxLoc(res)
        xl = xmin + max_loc[0]
        yl = ymin + max_loc[1]
        print (_max_val*100)

        #Dibuja las regiones de busqueda de reposicionado en las imagenes originales	
        if self.draw:
            cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,0,255),2,4)
            cv2.rectangle(img,( xmin + max_loc[0],ymin + max_loc[1]),(xmax + max_loc[0], ymax + max_loc[1]),(0,255,255),2,4)

        dx = xl - x0; dy = yl - y0


        return dx, dy

    def getOffset(self, fil):

        x0,x1,y0,y1=0,0,0,0
        xmin, ymin, xmax, ymax=0,0,0,0
        
        f = open(self.referencesDir + fil,'r')

        x0, y0, x1, y1, xmin, ymin, xmax, ymax = map(int,f.readline().split()) 
        f.close()
        
        pos = [x0,y0,x1,y1]
        srch = [xmin,ymin,xmax,ymax]


        return pos, srch




    def start(self):
 
        created = False

        if self.offset:
            for file in os.listdir(self.patternDir):

                rois= None
                pos, srch = None,None
                # ROI
                for roi in os.listdir(self.roisDir):
                    if roi.strip(".txt") == file.strip(".jpeg"):
                        rois = self.coordsRoi(roi)  
                        break

                for ref in os.listdir(self.referencesDir):
                    if ref.strip(".txt") == file.strip(".jpeg"):
                        pos, srch = self.getOffset(ref)

                        break
                
                    
                for dr in os.listdir(self.inputDir):
                    c = 0
                    if created == False:
                        self.create_empty_folder(self.outputDir + str(dr) + "/")
                    
                    if dr == os.listdir(self.inputDir)[-1]:
                        created = True
                    
                    for z in range(len(rois)):
                        
                        # output crops folder            
                        outputFolder = self.outputDir + str(dr)+"/"
                        # Creamos el directorio de salida. Si no existe lo crea si existe lo vacia
                        
                        imageList = self.get_image_list(self.inputDir +str(dr)+"/")
                        nFiles = len(imageList)
                        nFile = 1
                        


                        for imageName, imageFullName in imageList:
                            
                            if file.strip(".txt") in imageName:
                                
                                rois[z] = rois[z].strip("\n")
                                xmin, ymin, xmax, ymax = map(int,rois[z].split(" "))


                                # Dimensiones de los recortes. Vamos a tratar de que la dimension mayor sea 100px manteniendo relacion aspecto
                                roiWidth = xmax - xmin
                                roiHeight = ymax - ymin
                                
                                if roiHeight <0:
                                    roiHeight = roiHeight * -1

                                if roiWidth <0:
                                    roiWidth = roiWidth * -1
                                
                                if roiWidth > roiHeight:
                                    cropWidth = 100
                                    cropHeight = roiHeight * 100/roiWidth
                                else:
                                    cropHeight = 100
                                    cropWidth = roiWidth * 100/roiHeight

                                

                                time1 = time.time()
                                print("\nProcessing %s file %i of %i" % (imageName, nFile, nFiles))
                                self.PlainText.appendPlainText("\nProcessing %s file %i of %i" % (imageName, nFile, nFiles))

                                
                                img = cv2.imread(imageFullName)
                            
                                imgPat = cv2.imread(self.patternDir + file,0)

                                dx, dy = self.CalcularOffsets(img,imgPat,pos,srch)


                                y1=ymin+dy
                                y2=ymax+dy
                                x1=xmin+dx
                                x2=xmax+dx
                                
                                

                                if x2 > 1920:
                                    dif = x2 - 1920
                                    x2 = x2 - dif
                                    x1 = x1 - dif
                                if y2 > 1080:
                                    dif = y2 - 1080
                                    y2 = y2 - dif
                                    y1 = y1 - dif
                                if x1 < 0:
                                    x2 = x2 - (x1)
                                    x1 = x1 - x1
                                if y1 < 0:
                                    y2 = y2 - (y1)
                                    y1 = y1 - y1

                                print("ROI Post Offset x1:%i x2:%i y1:%i y2:%i" % (x1,x2,y1,y2))
                                self.PlainText.appendPlainText("ROI Post Offset x1:%i x2:%i y1:%i y2:%i" % (x1,x2,y1,y2))
                                QApplication.processEvents()

                                imgCrop = img[y1:y2,x1:x2]
                                imgRes = cv2.resize(imgCrop, (int(cropWidth), int(cropHeight)))
                            
                                    
                                imageName = imageName[0:-5] + "_ROI-" + str(c) + ".jpeg"
                                
                                
                                c +=1
                                
                                
                                #Dibuja las regiones de busqueda de reposicionado en las imagenes originales y las guarda en su caperta
                                if self.draw:
                                    cv2.rectangle(img,(xmin+dx,ymin+dy),(xmax+dx,ymax+dy),(255,0,0),2,4)	
                                    cv2.imwrite(outputFolder + imageName, img)
                                else:
                                    cv2.imwrite(outputFolder + imageName, imgRes)

                                nFile += 1
                        
        else:
            rois= None
            # ROI
            for roiFile in os.listdir(self.roisDir):
                rois = self.coordsRoi(roiFile)  
                    
                for dr in os.listdir(self.inputDir):
                    c = 0
                    if created == False:
                        self.create_empty_folder(self.outputDir + str(dr) + "/")
                    
                    if dr == os.listdir(self.inputDir)[-1]:
                        created = True
                    
                    for z in range(len(rois)):
                        
                        # output crops folder            
                        outputFolder = self.outputDir + str(dr)+"/"
                        # Creamos el directorio de salida. Si no existe lo crea si existe lo vacia
                        
                        imageList = self.get_image_list(self.inputDir +str(dr)+"/")
                        nFiles = len(imageList)
                        nFile = 1
                        


                        for imageName, imageFullName in imageList:
                            
                            if roiFile.strip(".txt") in imageName:
                                
                                rois[z] = rois[z].strip("\n")
                                xmin, ymin, xmax, ymax = map(int,rois[z].split(" "))


                                # Dimensiones de los recortes. Vamos a tratar de que la dimension mayor sea 100px manteniendo relacion aspecto
                                roiWidth = xmax - xmin
                                roiHeight = ymax - ymin
                                
                                if roiHeight <0:
                                    roiHeight = roiHeight * -1

                                if roiWidth <0:
                                    roiWidth = roiWidth * -1
                                
                                if roiWidth > roiHeight:
                                    cropWidth = 100
                                    cropHeight = roiHeight * 100/roiWidth
                                else:
                                    cropHeight = 100
                                    cropWidth = roiWidth * 100/roiHeight

                                
                                print("\nProcessing %s file %i of %i" % (imageName, nFile, nFiles))
                                self.PlainText.appendPlainText("\nProcessing %s file %i of %i" % (imageName, nFile, nFiles))
                                QApplication.processEvents()
                                
                                img = cv2.imread(imageFullName)
                            
                                imgCrop = img[ymin:ymax,xmin:xmax]
                                imgRes = cv2.resize(imgCrop, (int(cropWidth), int(cropHeight)))
                            
                                    
                                imageName = imageName[0:-5] + "_ROI-" + str(c) + ".jpeg"
                                
                                
                                c +=1
                                
                                if self.draw:
                                    #Dibuja las regiones de busqueda de reposicionado en las imagenes originales y las guarda en su caperta
                                    cv2.rectangle(img,(xmin+dx,ymin+dy),(xmax+dx,ymax+dy),(255,0,0),2,4)	
                                    cv2.imwrite(outputFolder + imageName, img)
                                else:
                                    cv2.imwrite(outputFolder + imageName, imgRes)
                                    
                                nFile += 1





                        
