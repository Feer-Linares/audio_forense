# -*- coding: utf-8 -*-
"""
Created on Wen Dic  05 10:10:43 2018
@author: Feer
Este archivo genera las tripletas necesarias para ofrecerle datos a la Red Neuronal
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
listaA=[]
combinaciones =[]
aleatorio=0
aleatorio1=0

import sys
def combinar(lista,num):
                for elemento in combinations_with_replacement(lista, 3):
                        if(len(combinaciones)<num):
                                lista1=list(elemento) #Convierte en una lista las combinaciones que hace la linea anterior
                                p=lista1[0][0]
                                p2=lista1[1][0]
                                p3=lista1[2][0]
                                if(p==p2 and p2!=p3):
                                        combinaciones.append(lista1)
                        elif (len(combinaciones)>num):
                                return combinaciones
                return combinaciones


def genParts(id,num):
	importlib.reload(sys)
	if (f.exists()):
		file=open(f,'rb')
		lista=pickle.load(file)
		res=combinar(lista,num)
	else:	
                for roots, dirs, files in os.walk(spath,topdown=True):
                        for file in files:
                                if file.endswith("LEC.wav"):  #Si el archivo es de lectura (LEC) y .wav continua el proceso
                                        y,sr=librosa.load(file)
                                        lista=[]
                                        #Si el archivo es tipo mono de de 16000 Hz continua el proceso
                                        if (sr!=16000 and librosa.util.valid_audio(y)):
                                                y,sr =librosa.load(file,16000)
                                                espect=librosa.feature.melspectrogram(y=y, sr=sr)
                                                #Genera trozos del mismo tamaño del arreglo
                                                hlen,slen=espect.shape
                                                print(slen,hlen)
                                                ini=randint(0,slen-30)#Punto inicial: Desde 0 hasta 
                                                part=espect[:,ini:ini+30]
                                                slice = part
                                                a=(file.split("_"))
                                                clave=a[0] #Toma como clave el nombre del archivo antes del "_"	
                                                diccionario[clave]=slice # guarda las partes en el diccionario
                                                for indice in diccionario.keys(): #Recorre el diccionario
                                                        tupla =indice,diccionario[indice]
                                                        lista.append(tupla)
                                                pickle.dump( lista, open("lista.p", "wb" ))
	res=combinar(lista,num)
	return res
def listaraarch(spath):
        for roots,dirs, files in os.walk(spath,topdown=True):
                for file in files:
                        if file.endswith('LEC.wav'):
                                listaA.append(file)
        return listaA

#genParts('CDMN1E2SF001_LEC.wav',256)
							
						 

				



