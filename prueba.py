# -*- coding: utf-8 -*-
"""
Created on Wen Dic  05 10:10:43 2018
@author: Feer
"""
import os
import sys
import importlib
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
spath= r"/home/feer/tensorflow/todos"
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
def combinar(lista,num):
		for elemento in combinations_with_replacement(lista, 3):
			if(len(combinaciones)<num):
				lista1=list(elemento) #Convierte en una lista las combinaciones que hace la linea anterior
				#print ("Tipo de indice 0",type(lista1[0]), "su contenido es: ",lista1[0])
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
					print(" y num es: ",num)
					pickle.dump( combinaciones, open( "combinaciones.p", "wb" ) )
			elif (len(combinaciones)>num):
				break


def genParts(id,num):
	importlib.reload(sys)
	if (f.exists()):
		file=open(f,'rb')
		lista=pickle.load(file)
		print ("lista creada")
		combinar(lista,num)
	else:
		print("Creando lista")	
		for roots, dirs, files in os.walk(spath,topdown=True):
			for file in files:
				if file.endswith("LEC.wav"):  #Si el archivo es de lectura (LEC) y .wav continua el proceso
					y,sr=librosa.load(file)
					lista=[]
					#Si el archivo es tipo mono de de 16000 Hz continua el proceso
					if (sr!=16000 and librosa.util.valid_audio(y)):
						y,sr =librosa.load(file,16000)
						espect=librosa.feature.melspectrogram(y=y, sr=sr)
						#espect.reshape(128,1330)
						#tam= np.shape(espect)
						# print ("El tamaño de ", file ,"es: ",tam, " y es: ",type(espect))
						#Genera trozos del mismo tamaño del arreglo y
						#print("Tipo de espect", type(espect))
						parts = np.array_split(espect,20)
						#print("Tipo de parts", type(parts))
						parts=np.asarray(parts)
						slice = np.array_split(parts,10)
						#print("Resultado parts: ",parts)
						#print("Resultado slice: ",slice)
						a=(file.split("_"))
						clave=a[0] #Toma como clave el nombre del archivo antes del "_"
						aleatorio=randint(4,9)
						aleatorio1=randint(0,3)	
						if id == file: #Si el archivo que entra en el método es igual al que se procesa continua
							diccionario[clave]=slice # guarda las partes en el diccionario
							#lista=[]
							for indice in diccionario.keys(): #Recorre el diccionario 
								tupla =indice,diccionario[indice][aleatorio1]
								tupla1=indice,diccionario[indice][aleatorio]
								lista.append(tupla)
								lista.append(tupla1)
						else:
							diccionario1[clave]=slice
							tupla=()
							for indice in diccionario1.keys():
								tupla =indice,diccionario1[indice][aleatorio1]
								lista.append(tupla)
								combinar(lista,num)
						#nombre = "lista" + a + ".p"
						#print(nombre)
						pickle.dump( lista, open("lista.p", "wb" ))
genParts("CDMN2E1SF002_LEC.wav",256)



							
						 

				



