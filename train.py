import keras
import numpy as np
from keras.datasets import cifar10
from keras.callbacks import ModelCheckpoint
from model import TripletNet
from triplets import TripletGenerator

#Reemplazar por valores del espectrograma
input_size = (32, 32, 3)
embedding_dimensions = 128
batch_size = 256
train_stream = TripletStream()

t = TripletNet(shape=input_size, dimensions=embedding_dimensions)
t.summary()

t.model.load_weights('model128big_batch.weights.best.hdf5', by_name=False)
checkpointer = ModelCheckpoint(
    filepath='model128big_batch2.weights.best.hdf5',
    verbose=1, save_best_only=True
)

t.model.fit_generator(
    train_stream, 2500, epochs=30, verbose=1,
    callbacks=[checkpointer],validation_steps=20
)
# t.model.fit(x_train, y_train, batch_size=64, epochs=50)
