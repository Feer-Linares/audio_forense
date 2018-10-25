
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
      title="Add Audio"
      return render_template('agregar.html',title=title)
      
@app.route('/upload', methods=['POST'])
def upload():
      new.insert({'usuario' : request.form['user'],'tipo_audio' : request.form['opcion'], 'area_geo' : request.form['lugar'],'name_arch' : request.form['file']}) 
      return redirect(url_for('insert'))

@app.route('/lista')
def lista():
      title="Audio list"
      res = new.find()
      return render_template('lista.html',title=title,res = res)

@app.route('/acerca')
def acerca():
      title="About"
      return render_template('acerca.html',title=title)

@app.route('/obs')
def obs():
      title = "Observar Espectrograma"
      return render_template('espectrograma.html',title=title)

@app.route('/rep/<dato>')
def enc (dato):
      title="Reproductor"
      song = dato 
      return render_template('music.html',title=title, song = song)
@app.route('/borrar/<dato>')
def borrar(dato):
      res = new.delete_one({'name_arch':dato})
      return redirect(url_for('lista'))
#@app.route('/editar/<dato>')     
#def editar(dato):
      #res = 
if __name__ == '__main__':
      #db.create_all() #Cuando se ejecuta, se crea la bd
      app.run(port = 8000,debug=True)