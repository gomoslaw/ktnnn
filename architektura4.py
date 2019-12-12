from keras import backend as K
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.layers import Dense, Dropout, Flatten
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard
from keras.preprocessing.image import ImageDataGenerator
from glob import glob
import datetime



BATCH_SIZE = 128
EPOCH_COUNT = 50

MODEL_PATH = 'model.hdf5'
WEIGHTS_PATH = 'weights.hdf5'
IMAGE_DEPTH = 3
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_SHAPE = (IMAGE_DEPTH, IMAGE_HEIGHT, IMAGE_WIDTH)
NAME = "architektura-4{}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 
tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME),write_graph=True,write_images=True,histogram_freq=0)

#odpowiednie wymiarowanie obrazu wchodzącego
if K.image_data_format() == 'channels_last':
    IMAGE_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_DEPTH)

#budowa sieci
model = Sequential()

model.add(Conv2D(filters = 32, kernel_size = (3, 3), activation = 'relu', input_shape = IMAGE_SHAPE))
model.add(ZeroPadding2D(padding = (1, 1)))
model.add(Conv2D(filters = 32, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2), strides=(2, 2)))
model.add(Dropout(rate = 0.25))

model.add(ZeroPadding2D(padding = (1, 1)))
model.add(Conv2D(filters = 64, kernel_size = (3, 3), activation = 'relu'))
model.add(ZeroPadding2D(padding = (1, 1)))
model.add(Conv2D(filters = 64, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2), strides=(2, 2)))
model.add(Dropout(rate = 0.25))

model.add(ZeroPadding2D(padding = (1, 1)))
model.add(Conv2D(filters = 128, kernel_size = (3, 3), activation = 'relu'))
model.add(ZeroPadding2D(padding = (1, 1)))
model.add(Conv2D(filters = 128, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2), strides=(2, 2)))
model.add(Dropout(rate = 0.25))

model.add(ZeroPadding2D(padding = (1, 1)))
model.add(Conv2D(filters = 256, kernel_size = (3, 3), activation = 'relu'))
model.add(ZeroPadding2D(padding = (1, 1)))
model.add(Conv2D(filters = 256, kernel_size = (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2), strides=(2, 2)))
model.add(Dropout(rate = 0.25))

model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(rate = 0.2))
model.add(Dense(5, activation = 'softmax'))
model.summary()

#ustawienie optymizera na sgd
sgd=SGD(lr=0.01, decay=1e-6, momentum0.9, nesterov=True)
model.compile(optimizer = sgd, loss = 'categorical_crossentropy', metrics = ['accuracy'])

class_names = glob("dataset/train") # czytanie obrazóœ z folderu
class_names = sorted(class_names) # sortowanie
name_id_map = dict(zip(class_names, range(len(class_names))))

#augmenting 
train_datagen = ImageDataGenerator(
        rescale = 1./255,
        shear_range = 0.2,
        zoom_range = 0.2,
        horizontal_flip = True)
valid_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory(
        'dataset/train',
        target_size = (IMAGE_HEIGHT, IMAGE_WIDTH),
        batch_size = BATCH_SIZE,
        class_mode = 'categorical')




valid_set = valid_datagen.flow_from_directory(
        'dataset/test',
        target_size = (IMAGE_HEIGHT, IMAGE_WIDTH),
        batch_size = BATCH_SIZE,
        class_mode = 'categorical')

#earlystop = EarlyStopping(monitor='val_acc', min_delta=0.0001, patience=3, verbose=1, mode='auto')
checkpoint = ModelCheckpoint(WEIGHTS_PATH, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
model.fit_generator(
        training_set,
        epochs = EPOCH_COUNT,
        steps_per_epoch=valid_set.__len__(),
        validation_steps=10,
        validation_data = valid_set,
        callbacks = [checkpoint,tensorboard])
model.save(MODEL_PATH, True, True)
