from msilib.schema import Error
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from formulario import frmEstudiante, frmloggin
import os
from sqlite3.dbapi2 import Error


app = Flask(__name__)

app.secret_key = os.urandom(24)

@app.route('/')

def index():
    form = frmEstudiante()
    return render_template('formulario.html', form=form)

@app.route('/estudianteguardar/', methods=['POST', 'GET'])
def estudianteguardar():
    form = frmEstudiante()
    if request.method == "POST":
        documento = request.form['documento']
        nombre = request.form['nombre']
        genero = request.form['genero']
        ciclo = request.form['ciclo']
        correo = request.form['correo']
        estado = request.form['estado']
        print("hola")
        try:
            with sqlite3.connect('colegio.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO Estudiante (Documentos, Nombre, Sexo, Ciclo, Correo, Estado) VALUES (?,?,?,?,?,?)', (documento, nombre, genero, ciclo, correo, estado))
                conn.commit()
                flash('Estudiante registrado correctamente')
                return "hola"

        except Error:
            print(Error)
    flash('Estudiante registrado correctamente')
    return "error"

@app.route('/ver/', methods=['POST', 'GET'])
def ver():
    form=frmloggin()
    return render_template('loggin.html', form=form)

@app.route('/loggin/', methods=['POST', 'GET'])
def loggin():
    form = frmEstudiante()
    usuario=request.form['usuario']
    clave=request.form['clave']
    with sqlite3.connect('colegio.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuarios = '"+ usuario +"' AND clave = '"+clave+"'")
        conn.commit()
        if cursor.fetchone() is not None:
            return render_template("formulario.html", form=form)
    return "error"


            

         




app.run(debug=True)