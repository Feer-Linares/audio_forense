# -*- coding: utf-8 -*-
"""
Created on Wen Nov  14 13:17:43 2018

@author: Feer
"""
import os
import librosa
import numpy as np
import librosa.display
import matplotlib.pyplot as plt
from scipy.fftpack import dct
spath= r"C:\Users\rosam\Desktop\audio_forense\static\music"
os.chdir( spath ) #Cambia a la ruta especificada
#print(os.listdir(spath))
for roots, dirs, files in os.walk(spath):
	for file in files:
		if file.endswith("LEC.wav"):
			y,sr=librosa.load(file)
			if (sr!=16000 and librosa.util.valid_audio(y)):
				y,sr =librosa.load(file,48000,duration=5)
				a=(file.split("_"))
				clave=a[0]
				diccionario= {clave : [y]}
				print (diccionario)
	for dir in dirs:
		print("")