from main import app
from flask import render_template
from flask import Flask, request, render_template,flash, redirect, url_for

@app.route('/')
@app.route('/Kindex.html')
def Kindex(): 
  return render_template('/Kindex.html')


@app.route('/neWmenu', methods=['GET', 'POST'])
def neWmenu(): 
  return render_template('/neWmenu.html')
  
@app.route('/Knosotros')
def Knosotros(): 
  return render_template('/Knosotros.html')

@app.route('/Kcontacto', methods=['GET', 'POST'])
def Kcontacto(): 
  return render_template('/Kcontacto.html')

@app.route('/Kregistro', methods=['GET', 'POST'])
def Kregistro(): 
  return render_template('/Kregistro.html')

@app.route('/Klogin', methods=['GET', 'POST'])
def Klogin(): 
  return render_template('/Klogin.html')

