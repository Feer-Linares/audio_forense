# -*- coding: utf-8 -*-
"""
Created on Wen Nov  14 13:17:43 2018
@author: Feer
"""
import os
import librosa
import numpy as np
from numpy import array
import librosa.display
import matplotlib.pyplot as plt
from scipy.fftpack import dct
from itertools import *
from random import *
import pickle
#print (os.getcwd())
spath= r"C:\Users\feerz\Desktop\todos"

os.chdir( spath ) #Cambia a la ruta especificada
#print(os.listdir(spath))
diccionario={}
for roots, dirs, files in os.walk(spath,topdown=True):
	for file in files:
		if file.endswith("LEC.wav"):
			y,sr=librosa.load(file)
			if (sr!=16000 and librosa.util.valid_audio(y)):
				y,sr =librosa.load(file,16000)
				espect=librosa.feature.melspectrogram(y=y, sr=sr)
				#Genera trozos del mismo tamaño del arreglo y
				parts = np.array_split(espect,20)
				a=(file.split("_"))
				clave=a[0]			
				diccionario[clave]=parts 
				D=librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
lista=[]
lista1=[]
tupla=()
p =""
p2 = ""
aleatorio=randint(1,19)
i=0
for indice in diccionario.keys():
	tupla =indice,diccionario[indice][0]
	tupla1=indice,diccionario[indice][aleatorio]
	lista.append(tupla)
	lista.append(tupla1)
for elemento in combinations_with_replacement(lista, 2):
	i=i+1
	lista1=list(elemento)
	for item in lista1:
		uno=tuple(item[0].split(','))
		uno=str(uno)
		uno=uno.replace(")","")
	p=str(lista1[0])
	p2=str(lista1[1])
	print "Iterac ",i
	if (p.startswith(uno)):
		lista1.extend([1])
	else:
		lista1.extend([0])
	print "\n",lista1, "\n"
pickle.dump( lista1, open( "lista1.p", "wb" ) )