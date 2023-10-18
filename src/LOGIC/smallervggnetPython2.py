# import the necessary packages
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers import GlobalAveragePooling2D
from keras.layers.core import Flatten
from keras.layers.core import Dropout
from keras.layers.core import Dense
from keras.layers import LeakyReLU
from keras import backend as K
from keras.regularizers import l2
from keras.initializers import RandomNormal, Constant

class SmallerVGGNet:
	@staticmethod
	def build(width, height, depth, classes):
		# initialize the model along with the input shape to be
		# "channels last" and the channels dimension itself
		model = Sequential()
		inputShape = (height, width, depth)
		chanDim = -1

		# if we are using "channels first", update the input shape
		# and channels dimension
		if K.image_data_format() == "channels_first":
			inputShape = (depth, height, width)
			chanDim = 1

		# CONV => RELU => POOL
		model.add(Conv2D(32, (3, 3), padding="same",
			input_shape=inputShape,kernel_regularizer=l2(0.000001), activation="relu",bias_initializer='zeros',kernel_initializer='he_uniform'))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(3, 3), padding="same"))
		model.add(Dropout(0.25))

		# (CONV => RELU) * 2 => POOL
		model.add(Conv2D(64, (3, 3), padding="same",kernel_regularizer=l2(0.000001), activation="relu",bias_initializer='zeros',kernel_initializer='he_uniform'))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(64, (3, 3), padding="same",kernel_regularizer=l2(0.000001), activation="relu",bias_initializer='zeros',kernel_initializer='he_uniform'))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
		model.add(Dropout(0.25))

		# (CONV => RELU) * 2 => POOL
		model.add(Conv2D(128, (3, 3), padding="same",kernel_regularizer=l2(0.000001),activation="relu",bias_initializer='zeros',kernel_initializer='he_uniform'))
		model.add(BatchNormalization(axis=chanDim))
		model.add(Conv2D(128, (3, 3), padding="same",kernel_regularizer=l2(0.000001), activation="relu",bias_initializer='zeros',kernel_initializer='he_uniform'))
		model.add(BatchNormalization(axis=chanDim))
		model.add(MaxPooling2D(pool_size=(2, 2), padding="same"))
		model.add(Dropout(0.25))

		# first (and only) set of FC => RELU layers
		#model.add(Flatten())
		#model.add(Dense(1024))
		#model.add(LeakyReLU(alpha=0.05))
		model.add(GlobalAveragePooling2D())
		model.add(BatchNormalization(momentum=0.99, epsilon=0.05,beta_initializer=RandomNormal(mean=0.0, stddev=0.05), gamma_initializer=Constant(value=0.9)))
		model.add(Dropout(0.3))

		# softmax classifier
		model.add(Dense(classes,activation="softmax"))

		# return the constructed network architecture
		return model
