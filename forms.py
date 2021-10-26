from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import StringField, IntegerField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired,InputRequired


class Producto(FlaskForm):
    codigo = StringField('Codigo', validators=[DataRequired(message='No dejar vacío,  completar')])
    nombre = StringField('Nombre', validators = [InputRequired(message='Indique el nombre')])
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    precio = IntegerField('Precio', validators=[DataRequired()])
    enviar = SubmitField('Agregar Producto')
    
def validate_on_submit(self)->bool:
    return True

class FormInicio(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío,  completar')])
    contrasena = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar')])
    recordar = BooleanField('Recordar Usuario')
    enviar = SubmitField('Iniciar Sesión') #validate_on_submit)
 
def validate_on_submit(self)->bool:
    return True

class FormRegistro(FlaskForm):
    nombre = StringField('Nombre', validators=[InputRequired(message='No dejar vacío,  completar')])
    apellidos = StringField('Apellidos', validators=[InputRequired(message='No dejar vacío,  completar')])
    direccion = StringField('Direccion', validators=[InputRequired(message='No dejar vacío,  completar')])
    telefono = StringField('Telefono', validators=[InputRequired(message='No dejar vacío,  completar')])
    email = EmailField('Email', validators=[InputRequired(message='ingrese email valido')])
    usuario = StringField('Usuario', validators=[InputRequired(message='No dejar vacío,  completar')])
    contrasena = PasswordField('Contraseña', validators=[InputRequired(message='No dejar vacío, completar')])
    cumpleanos = StringField('Cumpleaños', validators=[InputRequired(message='No dejar vacío,  completar')])
    termsCond = BooleanField('Acepta Terminos y Condiciones?',validators=[InputRequired(message='Debe aceptar Term & Cond ')])

    enviar = SubmitField('Iniciar Sesión')


def validate_on_submit(self)->bool:
    return True

