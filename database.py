import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('PlanetS.db')
        return con
    except Error as err:
        print (err)

def sql_insert_producto(codigo, nombre, cantidad, precio):
    try:
        sql = f'insert into producto(Codigo,Nombre,Cantidad,Precio) values ("{codigo}","{nombre}",{cantidad},{precio})'
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        con.commit()
        con.close()
    except Error as err:
        print(err)

def sql_select_productos():
    try:
        strsql = "select * from producto;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        productos = cursorObj.fetchall()
        return productos
    except Error as err:
        print(err)

def sql_edit_producto(codigo, nombre, cantidad, precio):
    try:
        strsql = "update producto set nombre = '"+nombre+"', cantidad = "+cantidad+",precio = '"+precio+"' where codigo = "+codigo+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)


def sql_delete_producto(codigo):
    try:
        strsql = "delete from producto where codigo = "+codigo+";"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        con.commit()
        con.close()
    except Error as err:
        print(err)

def sql_insert_cliente(nombre, apellidos, direccion, telefono, email, usuario,contrasena, cumpleanos):
    try:
        sql = f'insert into cliente(nombre,apellidos, direccion, telefono, email, usuario, contrasena, cumpleanos) values ("{nombre}","{apellidos}","{direccion}","{telefono}", "{email}", "{usuario}", "{contrasena}", "{cumpleanos}")'
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        con.commit()
        con.close()
    except Error as err:
        print(err)

def sql_select_cliente():
    try:
        strsql = "select * from cliente;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(strsql)
        clientes = cursorObj.fetchall()
        return clientes
    except Error as err:
        print(err)

def sql_buscar_cliente(usuario):
    try:
        strsql = "select contrasena from cliente where usuario = "+usuario+" "
        con2 = sql_connection()
        cursorObj = con2.cursor()
        cursorObj.execute(strsql)
        clientes = cursorObj.fetchone()
        return clientes
    except Error as err:
        print(err)
