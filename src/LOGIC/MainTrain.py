# USAGE
# python train.py --dataset dataset --model pokedex.model --labelbin lb.pickle

# set the matplotlib backend so figures can be saved in the background
import matplotlib

matplotlib.use("Agg")
# import the necessary packages
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.utils import img_to_array
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from LOGIC.smallervggnet import SmallerVGGNet
# from vgg16 import VGGNet16
import matplotlib.pyplot as plt
from imutils import paths
import numpy as np
import random
import pickle
import cv2
import os
from PyQt6.QtCore import QThread
from PyQt6.QtCore import QThread, pyqtSignal
from contextlib import redirect_stdout

from keras import backend as K

K.clear_session()

import tensorflow as tf

gpu_options = tf.compat.v1.GPUOptions(per_process_gpu_memory_fraction=0.75)
config = tf.compat.v1.ConfigProto(gpu_options=gpu_options)
config.gpu_options.allow_growth = True
session = tf.compat.v1.Session(config=config)

# construct the argument parse and parse the arguments
'''ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True,
	help="path to input dataset (i.e., directory of images)")
ap.add_argument("-m", "--model", required=True,
	help="path to output model")
ap.add_argument("-l", "--labelbin", required=True,
	help="path to output label binarizer")
ap.add_argument("-p", "--plot", type=str, default="plot.png",
	help="path to output accuracy/loss plot")
args = vars(ap.parse_args())'''


class MainTrain(QThread):
    '''
        - epochs INT
        - bs (batch size) INT
        - augmentator BOOL
        - clasificaciones BOOL: Si son 2 clases False, si hay mas True
    '''
    update_signal = pyqtSignal(str)

    def __init__(self,configGeneral,epochs=150,bs=2,augmentator=True,clasificaciones=False,plainText=None):
        QThread.__init__(self)
        self.configGeneral = configGeneral
        self.plainText = plainText
        
        self.nombreRed = str(self.configGeneral["nombre"])
        self.datasetDir = str(self.configGeneral["outputDir"])
        self.modelFile = str(self.configGeneral["modelPath"]) + self.nombreRed + ".h5"
        self.labelsFile = str(self.configGeneral["modelPath"]) + self.nombreRed + ".pickle"
        self.plotFile = str(self.configGeneral["modelPath"]) + "/plot.png"
        self.callback_path = str(self.configGeneral["modelPath"]) + "/best_model.h5"

        self.direct = os.listdir(self.datasetDir)

        try:
            if not os.path.exists(self.configGeneral["modelPath"]):
                os.mkdir(self.configGeneral["model"])
        except:
            pass
        
        # initialize the number of epochs to train for, initial learning rate,
        # batch size, and image dimensions
        self.epochs = epochs
        self.init_lr = 1e-3
        self.bs = bs  # 32
        self.augmentator = augmentator  # Uil
        # izar data augmentation para generar dataset augmentator = True
        self.clasificaciones = clasificaciones  # Especificar True si hay mas de 2 clasificaciones el dataset
        
        # initialize the data and labels
        self.data = []
        self.labels = []



    def start(self):


        data = []
        labels = []
        
        # Ver tamanho del ROIs y redimensionar dimensiones si es necesario
        for folder in self.direct:
            imgs = os.listdir(self.datasetDir + "/" + str(folder) + "/")
            for img in imgs:
                img = cv2.imread(self.datasetDir + "/" + folder + "/" + img)
                height, width = img.shape[:2]

                self.cropHeight = height
                self.cropWidth = width

                # REDIMENSIONAR A 100 SI O SI
                if width > height:
                    self.cropWidth = 100
                    self.cropHeight = height * 100 / width
                else:
                    self.cropHeight = 100
                    self.cropWidth = width * 100 / height

                # REDIMENSIONAR A 100 SOLO SI LOS LADOS SON MAYORES QUE 100
                # if width <= 100 and height <= 100:
                #     cropWidth = width
                #     cropHeight = height
                # else:
                #     if width > height:
                #         cropWidth = 100
                #         cropHeight = height * 100 / width
                #     else:
                #         cropHeight = 100
                #         cropWidth = width * 100 / height
                print("Tamanho imagen: " + str(self.cropHeight) + ", " + str(self.cropWidth))
        
        self.update_signal.emit("Tamanho imagen: " + str(self.cropHeight) + ", " + str(self.cropWidth))


                
        self.image_dims = (int(self.cropHeight), int(self.cropWidth), 3)
        print(self.image_dims)
        self.update_signal.emit("(" + str(self.image_dims[0]) + "," + str(self.image_dims[1]) + "," + str(self.image_dims[2]) + ")")

        print("[INFO] loading images...")
        self.update_signal.emit("[INFO] loading images...")

        # grab the image paths and randomly shuffle them
        imagePaths = sorted(list(paths.list_images(self.datasetDir)))  # args["dataset"])))

        # random.seed(5) # Para obtener siempre los mismos resultados al barajar, descomentar
        random.shuffle(imagePaths)

        # loop over the input images
        for imagePath in imagePaths:
            # load the image, pre-process it, and store it in the data list
            image = cv2.imread(imagePath)
            
            image = cv2.resize(image, (int(self.image_dims[1]), int(self.image_dims[0])))
            image = img_to_array(image)
            data.append(image)

            # extract the class label from the image path and update the
            # labels list
            label = imagePath.split(os.path.sep)[-2]
            labels.append(label)

            
        # scale the raw pixel intensities to the range [0, 1]
        data = np.array(data, dtype="float") / 255.0
        labels = np.array(labels)

        print("[INFO] data matrix: {:.2f}MB".format(
            data.nbytes / (1024 * 1000.0)))

        self.update_signal.emit("[INFO] data matrix: {:.2f}MB".format(
            data.nbytes / (1024 * 1000.0)))

        # binarize the labels
        lb = LabelBinarizer()

        labels = lb.fit_transform(labels)
        print(len(lb.classes_))
        #self.plainText.appendPlainText(str(len(lb.classes_)))
        self.update_signal.emit(str(len(lb.classes_)))

        # partition the data into training and testing splits using 80% of
        # the data for training and the remaining 20% for testing
        (trainX, testX, trainY, testY) = train_test_split(data,
                                                        labels, test_size=0.2)

        # construct the image generator for data augmentation
        aug = ImageDataGenerator(height_shift_range=0.1,width_shift_range=0.1, fill_mode="nearest")
        
        
        # initialize the model
        print("[INFO] compiling model...")
        self.update_signal.emit("[INFO] compiling model...")

        model = SmallerVGGNet.build(width=self.image_dims[1], height=self.image_dims[0],
                                    depth=self.image_dims[2], classes=len(lb.classes_))

        # model = VGGNet16.build(width=IMAGE_DIMS[1], height=IMAGE_DIMS[0],
        #                             depth=IMAGE_DIMS[2], classes=len(lb.classes_))
        opt = Adam(learning_rate=self.init_lr, decay=self.init_lr / self.epochs)

        # Funcion de perdida para una o mas clasificaciones
        if self.clasificaciones:
            loss = "categorical_crossentropy"
        else:
            loss = "sparse_categorical_crossentropy"

        model.compile(loss=loss, optimizer=opt,
                    metrics=["accuracy"])

        # train the network
        print("[INFO] training network...")
        self.update_signal.emit("[INFO] training network...")

        # Keras callbacks, guardar el mejor modelo priorizando una variable, como el error de validacion
        mc = ModelCheckpoint(self.callback_path, monitor='val_loss', mode='min', save_best_only=True, verbose=1)

        # Keras callbacks, Parar de entrenar el modelo si una variable, como el error de validacion no mejora durante N epochs
        es = EarlyStopping(monitor='val_accuracy', mode='max', verbose=1, patience=20)

        with redirect_stdout(TextEditWriter(self.plainText,self.update_signal)):
            if self.augmentator:
                # save_to_dir = "../datasetGen", save_format = "jpeg"
                H = model.fit_generator(
                    aug.flow(trainX, trainY, batch_size=self.bs),
                    validation_data=(testX, testY),
                    steps_per_epoch=len(trainX) // self.bs,
                    epochs=self.epochs, verbose=2,callbacks=[mc])
            else:
                H = model.fit(trainX, trainY,
                            epochs=self.epochs,
                            validation_data=(testX, testY),
                            batch_size=self.bs,
                            verbose=2, callbacks=[mc])



        # save the model to disk
        print("[INFO] serializing network...")
        self.update_signal.emit("[INFO] serializing network...")
        model.save(self.modelFile)  # args["model"])

        # save the label binarizer to disk
        print("[INFO] serializing label binarizer...")
        self.update_signal.emit("[INFO] serializing label binarizer...")
        # f = open(args["labelbin"], "wb")
        f = open(self.labelsFile, "wb")
        f.write(pickle.dumps(lb))
        f.close()

        # plot the training loss and accuracy
        plt.style.use("ggplot")
        plt.figure()
        N = len(H.history["loss"])
        plt.plot(np.arange(0, N), H.history["loss"], label="train")
        plt.plot(np.arange(0, N), H.history["val_loss"], label="val_loss")
        plt.plot(np.arange(0, N), H.history["accuracy"], label="train_acc")
        plt.plot(np.arange(0, N), H.history["val_accuracy"], label="val_accuracy")
        plt.title("Training Loss and Accuracy")
        plt.xlabel("Epoch #")
        plt.ylabel("Loss/Accuracy")
        plt.legend(loc="upper left")
        plt.savefig(self.plotFile)  # args["plot"])


class TextEditWriter:
    def __init__(self, text_edit,u):
        self.text_edit = text_edit
        self.u = u

    def write(self, message):
 
        self.u.emit(message)
    
    def flush(self):
        pass

    
