import typing
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import numpy as np
import fnmatch
import argparse
import os
import shutil

from PyQt6.QtCore import QObject, QThread
from PyQt6.QtWidgets import QApplication

class DataGenerator(QThread):
	def __init__(self,inputdir,outputdir,appdir):
		QThread().__init__(self)
		self.inputdir = inputdir
		self.outputdir = outputdir
		self.imagesList = []
		self.imagesNames = []

		self.appDir = appdir
		self.create_empty_folder(self.outputdir)



	def create_empty_folder(self,folder_name):
		try:
			shutil.rmtree(folder_name)
		except Exception as e:
			print("ERROR: Aviso eliminando directorio: %s" % e)
		if not os.path.exists(folder_name):
			try:
				os.makedirs(folder_name)
			except Exception as e:
				print("ERROR: Aviso creando directorio: %s" % e)
		return
	def start(self):
		
		self.ap = argparse.ArgumentParser()
		self.ap.add_argument("-t", "--total", type=int, default=20,
			help="# of training samples to generate")
		self.args = vars(self.ap.parse_args())


		
		if os.path.exists(self.inputdir):
			imagesNames = fnmatch.filter(os.listdir(self.inputdir),'*.jpeg')
		for imageName in imagesNames:
			fullPath = os.path.join(self.inputdir,imageName)
			self.imagesList.append([imageName, fullPath])

		for imageName, imageFullName in self.imagesList:
			# load the input image, convert it to a NumPy array, and then
			# reshape it to have an extra dimension
			print("[INFO] loading example image...")
			image = load_img(imageFullName)
			# image=cv2.imread(imageFullName)
			# image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
			
			image = img_to_array(image)
			# image=image[651:803,343:567]
			image = np.expand_dims(image, axis=0)
			# construct the image generator for data augmentation then
			# initialize the total number of images generated thus far
			
			aug = ImageDataGenerator(samplewise_center= True,channel_shift_range= 2,height_shift_range=0.1,width_shift_range=0.1,fill_mode="nearest",rotation_range=360,horizontal_flip=False,vertical_flip=False,zca_epsilon=1e-03)
			total=0
			# print image
			# construct the actual Python generator
			print("[INFO] generating images...")

			imageGen = aug.flow(image, batch_size=1, save_to_dir=self.outputdir,
				save_prefix=imageName, save_format="jpeg")
			# loop over examples from our image data augmentation generator
			for image in imageGen:
				# increment our counter
				# cv2.imwrite(imageFullName,image)
				print(image)
				total += 1
				# if we have reached the specified number of examples, break
				# from the loop
				if total == self.args["total"]:
					break

				
