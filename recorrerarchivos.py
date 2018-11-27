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
#print (os.getcwd())
spath= r"C:\Users\rosam\Desktop\Speakers\todos"

os.chdir( spath ) #Cambia a la ruta especificada
#print(os.listdir(spath))
for roots, dirs, files in os.walk(spath,topdown=True):
	for file in files:
		if file.endswith("LEC.wav"):
			y,sr=librosa.load(file)
			if (sr!=16000 and librosa.util.valid_audio(y)):
				y,sr =librosa.load(file,16000)
				#Genera trozos del mismo tamaño del arreglo y
				parts = np.array_split(y,20)
				a=(file.split("_"))
				clave=a[0]
				diccionario= {clave : parts}
				#print (diccionario)
				print("*****************************************************************")
				a=0
				for x in combinations_with_replacement(parts, 2):
					a=a+1
					print("Iteración :" ,a)
					x=array(x)
					if(np.all(x[0]==x[1])):
						x=np.append(x,[1])
					elif((np.all(x[0]!=x[1]))):
						x=np.append(x,[0])
					print(x)

	#for dir in dirs:
		#print("")