'''
Created on 16 ene. 2018

@author: mdlago
'''
import configparser as ConfigParser
from fileinput import filename
import os

#fileName = "prueba1.cfg"


class ConfigFile:
    
    def __init__(self, fileName):
        self.config = ConfigParser.ConfigParser()
        self.fileName = fileName
        # if the file doesn't exists we create it
        if not os.path.exists(fileName):
            print(fileName)
            print("Direccion de archivo config no valida")

        self.config.read(fileName)

    def ReadImageSize(self):
        return self.config.getint('IMAGE', 'IMAGE_WIDTH') , self.config.getint('IMAGE', 'IMAGE_HEIGHT')
    
    def ReadImageFolder(self):
        return self.config.get('IMG_ROUTE', 'DIR')
    
    def ReadRois(self):
        section = 'ROI_NAME'
        values = list(self.config.items(section))
        roisList = {}
        for line in values:
            roisList[line[0]] = line[1]
        return roisList
    
    def ReadRoiSize(self , roi):
        section = 'ROI_DIMENSION'
        values = self.config.get(section , roi)
        values = values.split(" ")
        for value in values:
            value = int(value)
        return values
    
    def WriteRois(self , param):
        self.config.set('ROI_NAME', param, param)
        self.Reload()
        return
    
    def WriteRoiSize(self, param , width , height):
        self.config.set('ROI_DIMENSION' , param , str(width) + " " + str(height))
        self.Reload()
        return

    def RemoveRois(self , key):
        self.config.remove_option('ROI_DIMENSION', key)
        self.config.remove_option('ROI_NAME', key)
        self.Reload()
        return
    
    def Reload(self):
        cfgFile = open(self.fileName,'w')
        self.config.write(cfgFile)
        cfgFile.close()
        self.config.read(self.fileName)
        
    
      
'''fileName = "../Config/configFile.cfg"
conf = ConfigFile(fileName)
val = conf.ReadRois()
print val
conf.WriteRois("hola")
val = conf.ReadRois()
print val
conf.WriteRoiSize("hola", 1920, 1080)'''

