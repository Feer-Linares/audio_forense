#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Data handling to create triplets."""
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from prueba import *
os.chdir(spath)
listaArchivos=listaraarch(spath)
class TripletStream:
    def __init__(self, streams, batch_size):
        self.classes = [c for c in streams]
        self.streams = streams
        self.batch_size = batch_size
        self.buffers = {c: [] for c in streams}

        self.random_deltas = np.arange(1, len(streams))

    def pop(self, c):
        if not self.buffers[c]:
            batch_data, batch_labels = next(self.streams[c])
            self.buffers[c] = [
                x for x in batch_data
            ]

        return self.buffers[c].pop()

    def __iter__(self):
        return self

    def __next__(self):
        file = (np.random.choice(listaArchivos))
        combinaciones=genParts(file,self.batch_size)
        samples = {
            'x':np.array([c[0][1] for c in combinaciones]),
            'x1':np.array([c[1][1] for c in combinaciones]),
            'x2': np.array([c[2][1] for c in combinaciones])
        }
        labels = np.ones(self.batch_size)
        return samples, labels


class TripletGenerator:
    def __init__(self):
        self.gen = ImageDataGenerator(
            preprocessing_function=lambda x:
                x.astype('float32') / 255
        )

    def flow(self, x, y, indices=None, batch_size=64):
        if not indices:
            classes = np.unique(y)
            indices = {c: np.where(y == c)[0] for c in classes}

        streams = {
            c: self.gen.flow(
                x[matching_indices, :],
                y[matching_indices, :],
                batch_size=batch_size
            ) for c, matching_indices in indices.items()
        }

        return TripletStream(streams, batch_size)
