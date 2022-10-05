from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,EmailField,BooleanField,SubmitField,PasswordField

class frmEstudiante(FlaskForm):
    documento= IntegerField('Documentos',render_kw={'class':'form-control'})
    nombre= StringField('Nombre',render_kw={'class':'form-control'})
    genero= StringField('Sexo',render_kw={'class':'form-control'})
    ciclo= SelectField('Ciclo', choices=[('1','Python'),('2','Java'),('3','html'),('4','css')],render_kw={'class':'btn btn-outline-secondary dropdown-toggle'})
    correo= EmailField('Correo',render_kw={'class':'form-control'})
    estado = BooleanField('Estado',render_kw={'class':'form-check-input mt-0'})
    guardar= SubmitField('Guardar',render_kw={'class':'btn btn-primary'})
    eliminar = SubmitField('Eliminar',render_kw={'class':'btn btn-danger'})
    modificar = SubmitField('Modificar',render_kw={'class':'btn btn-warning'})
   
class frmloggin(FlaskForm):
    usuario = StringField('Usuario',render_kw={'class':'form-control'})
    clave = PasswordField('Clave',render_kw={'class':'form-control'})
    ingresar = SubmitField('Ingresar',render_kw={'class':'btn btn-primary'})