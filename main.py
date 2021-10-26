import os
from types import MethodDescriptorType

from flask import Flask, request, render_template,flash, redirect, url_for
#from wtforms.validators import DataRequired, validate_on_submit

from database import sql_select_productos, sql_insert_producto, sql_edit_producto,  sql_buscar_cliente, sql_delete_producto, sql_insert_cliente
from forms import Producto, FormInicio, FormRegistro
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = os.urandom(24)

''' if __name__=='__main__':
    app.run(debug=True,port=5000) '''

app.config['SECRET_KEY']="LA_CLAVE"

import rutas

@app.route('/Abatidos')
def Abatidos(): 
      #productos = sql_select_productos()
  return render_template('/Abatidos.html')
  # productos = productos

@app.route('/Productos')
def Productos():
    productos = sql_select_productos()
    return render_template('/Productos.html', productos = productos)
    
@app.route('/pide_login', methods=["GET","POST"])
def pide_login():
    form = FormInicio()
    if (form.validate_on_submit()):    # es por POST si pasa este validate
        usuario=request.form["usuario"]
        contrasena=request.form["contrasena"]
        revisapwd= sql_buscar_cliente(usuario)
        # if  check_password_hash(revisapwd,contrasena):
        return redirect('/neWmenu') 
        #  else:
        #  return render_template('/pide_login.html')
    return render_template('/pide_login.html', form=form) 

@app.route('/Kregistro', methods=['GET', 'POST'])
def registra_nuevo():
   if  request.method == "GET": #Si la ruta es accedida a través del método GET entonces
	    #form = FormRegistro() #Crea un nuevo formulario de tipo producto
	    return render_template('/Kregistro.html')
        #, form=form) #redirecciona vista nuevo.html enviando la variable form
   if  request.method == "POST": #Si la ruta es accedida a través del método POST entonces
      nomb = request.form["nombre"] #asigna variable npmb con valor enviado desde formulario  en la vista html
      apell = request.form["apellidos"] #asigna variable apell con valor enviado desde formulario en la vista html
      direcc = request.form["direccion"] #asigna vble direcc con valor enviado desde formulario en la vista html
      telef = request.form["telefono"] #asigna vble telef con valor enviado desde formulario en la vista html
      correo = request.form["email"] #asigna vble correo con valor enviado desde formulario en la vista html
      usuar= request.form["usuario"]#asigna vble correo con valor enviado desde formulario en la vista html
      contrase = request.form["contrasena"] #asigna vble cant con valor enviado desde formulario en la vista html
      cumplea = request.form["cumpleanos"] #asigna vble cant con valor enviado desde formulario en la vista html
      sql_insert_cliente(nomb, apell, direcc, telef, correo, usuar, contrase, cumplea) #llamado de la función para insertar el nuevo usuario
      return render_template('/gracias.html')

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')

@app.route('/nuevoProd', methods=['GET', 'POST'])
def nuevoProd():
  if  request.method == "GET": #Si la ruta es accedida a través del método GET entonces#
	    form = Producto() #Crea un nuevo formulario de tipo producto
	    return render_template('/nuevoProd.html', form=form) #redirecciona vista nuevo.html enviando la variable form
  
  if  request.method == "POST": #Si la ruta es accedida a través del método POST entonces
      cod = request.form["codigo"] #asigna variable cod con valor enviado desde formulario  en la vista html
      nom = request.form["nombre"] #asigna variable nom con valor enviado desde formulario en la vista html
      cant = request.form["cantidad"] #asigna vble cant con valor enviado desde formulario en la vista html
      precio = request.form["precio"] #asigna vble cant con valor enviado desde formulario en la vista html
      sql_insert_producto(cod, nom, cant, precio) #llamado de la función para insertar el nuevo producto
      return 'OK'

@app.route('/edit', methods=['GET'])
def editar_producto():
    codigo = request.args.get('codigo') #captura de la vble código enviada a través de la URL
    nombre = request.args.get('nombre') #captura de la vble nombre enviada a través de la URL
    cantidad = request.args.get('cantidad') #captura de la vble cantidad enviada a través de la URL
    precio = request.args.get('precio') #captura de la variable id enviada a través de la URL
    sql_edit_producto(codigo, nombre, cantidad, precio) #llamado de la función de edición de la base de datos
    return "OK"

@app.route('/delete', methods=['GET'])
def borrar_producto():
    codigo = request.args.get('codigo') #captura de la variable id enviada a través de la URL
    sql_delete_producto(codigo) #llamado a la función de borrado de la base de datos
    return "OK"

@app.route('/pide_registrar', methods =["POST", "GET"])
def pide_registrar():
          #return f'Formulario GET nombre: {nombre}  apellidos : {apellidos} direccion : {direccion} telefono :  {telefono} email : {email}  constrasena: {contrasena} cumpleaños:  {cumpleaños}'
        form = FormRegistro()
        if form.validate_on_submit():    # formato es POST entonces
            nombre= request.form['nombre']
            apellidos= request.form['apellidos']
            direccion=request.form['direccion']   
            telefono=request.form['telefono']
            email=request.form['email']
            usuario=request.form['usuario']
            contrasena= generate_password_hash(request.form['contrasena'])
            cumpleanos=request.form['cumpleanos']
            termsCond=request.form['termsCond']
            #usuario_activo==true
            #print(request.json)
            if termsCond :
                sql_insert_cliente(nombre, apellidos, direccion, telefono, email, usuario, contrasena,cumpleanos)#,usuario_activo)
            return redirect('/pide_login')
        return render_template('/pide_registrar.html', form=form)
            
  