
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:17:43 2018

@author: Feer
"""
from flask import Flask, render_template, request, redirect,flash,url_for
from flask_pymongo import PyMongo
import os
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'audios'
app.config["MONGO_URI"] = 'mongodb://Feer:sistemas123@ds125953.mlab.com:25953/audios'
mongo = PyMongo(app)
new = mongo.db.archaudio

@app.route('/')
def index():
      title = "Audio Forense"
      return render_template('index.html',title=title)

@app.route('/insert')
def insert():
      return render_template('agregar.html')
      
@app.route('/upload', methods=['POST'])
def upload():
      file=request.files['file']
      new.insert({'name' : file.filename, 'data' : file.read()}) 
      return redirect(url_for('insert'))

@app.route('/lista')
def lista():
      title="Lista de audios"
      res = new.find()
      return render_template('lista.html',title=title,res = res)

@app.route('/obs')
def obs():
      title = "Observar Espectrograma"
      return render_template('espectro.html',title=title)

@app.route('/borrar',methods=['GET'])
def borrar ():
      select = new.find
      #res = new.delete_one({'name': })
      return redirect(url_for(lista))
      
if __name__ == '__main__':
      #db.create_all() #Cuando se ejecuta, se crea la bd
      app.run(port = 8000,debug=True)