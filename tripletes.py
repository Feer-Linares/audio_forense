# -*- coding: utf-8 -*-
"""
Created on Wen Dic  05 10:10:43 2018
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
from unipath import Path
f = Path('lista.p')
spath= r"C:\Users\feerz\Desktop\todos"
os.chdir( spath ) #Cambia a la ruta especificada
diccionario={}
diccionario1={}
lista=[]
lista1=[]
tupla=()
p =""
p2 = ""
p3=""
combinaciones =[]
aleatorio=0
aleatorio1=0
def genParts(id,num):
	for roots, dirs, files in os.walk(spath,topdown=True):
		for file in files:
			if file.endswith("LEC.wav"): #Si el archivo es de lectura (LEC) y .wav continua el proceso
				y,sr=librosa.load(file)
				#Si el archivo es tipo mono de de 16000 Hz continua el proceso
				if (sr!=16000 and librosa.util.valid_audio(y)): 
					y,sr =librosa.load(file,16000)
					espect=librosa.feature.melspectrogram(y=y, sr=sr)
					#espect.reshape(128,1330)
					#tam= np.shape(espect)
					# print ("El tamaño de ", file ,"es: ",tam, " y es: ",type(espect))
					#Genera trozos del mismo tamaño del arreglo y
					parts = np.array_split(espect,20)
					a=(file.split("_"))
					clave=a[0] #Toma como clave el nombre del archivo antes del "_"
					aleatorio=randint(4,19)
					aleatorio1=randint(0,3)	
					if id == file: #Si el archivo que entra en el método es igual al que se procesa continua
						diccionario[clave]=parts # guarda las partes en el diccionario
						for indice in diccionario.keys(): #Recorre el diccionario 
							tupla =indice,diccionario[indice][aleatorio1]
							tupla1=indice,diccionario[indice][aleatorio]
							lista.append(tupla)
							lista.append(tupla1)
					#print lista
					else:
						diccionario1[clave]=parts
						tupla=()
						for indice in diccionario1.keys():
							tupla =indice,diccionario1[indice][aleatorio1]
							lista.append(tupla)
					pickle.dump( lista, open( "lista.p", "wb" ) )
					#print ("Resultado: ",lista)
	i=0
	if(i<num):
		i=i+1
		for elemento in combinations_with_replacement(lista, 3):
			lista1=list(elemento) #Convierte en una lista las combinaciones que hace la linea anterior
			print ("Tipo de indice 0",type(lista1[0]), "su contenido es: ",lista1[0])
			p=str(lista1[0])
			p2=str(lista1[1])
			p3=str(lista1[2])
			p=p.split(",")
			p=p[0]
			p2=p2.split(",")
			p2=p2[0]
			p3=p3.split(",")
			p3=p3[0]
			if(p==p2 and p2!=p3):
				combinaciones.append(lista1)
		print(combinaciones)
		print (len(combinaciones))
	pickle.dump( combinaciones, open( "combinaciones.p", "wb" ) )
genParts("CDMN1E2SF001_LEC.wav",256)


			