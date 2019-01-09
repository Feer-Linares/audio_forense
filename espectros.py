# -*- coding: utf-8 -*-
"""
Created on Fri Dic  07 12:18:33 2018
@author: Feer
"""
import os
import librosa
import numpy as np
from numpy import array
import librosa.display
import matplotlib.pyplot as plt
spath= r"C:\Users\feerz\Desktop\todos"

os.chdir( spath ) #Cambia a la ruta especificada
file="CDMN1E2SF001_LEC.wav"
if file.endswith("LEC.wav"):
	y,sr=librosa.load(file)
	if (sr!=16000 and librosa.util.valid_audio(y)):
		y,sr =librosa.load(file,16000)
		espect=librosa.feature.melspectrogram(y=y, sr=sr)
		plt.plot(espect)
		plt.ylabel("Mel")
		plt.xlabel("Time")
		plt.title("Melspectrogram from file "+ file)
		plt.show()
