from flask import flash, session, render_template, redirect, request
from flask_bcrypt import Bcrypt
from app_revistas.modelos.modelo_revista import Revistas
from app_revistas import app

bcrypt = Bcrypt(app)

@app.route('/revista', methods=['GET'])
def mostrar_revista():
   lista_revistas = Revistas.obtener_suscripciones()
   return render_template('dashboard.html', revista=lista_revistas)

@app.route('/cuenta/usuario', methods=['GET'])
def mostrar_suscripciones():
   return render_template('cuenta.html')

@app.route('/new_revista', methods=['POST'])
def nueva_revista():
   data = {
        **request.form,
      "usuarios_id": session['usuarios_id']
   }
   if Revistas.validador_formulario_revistas(data) == False:
      return redirect('/new')
   else:
      id_revista = Revistas.agregar_uno(data)
      return redirect('/dashboard')

@app.route('/new', methods=['GET'])
def desplegar_new():
   if 'usuarios_id' not in session:
      return redirect('/')
   else:
      return render_template('revistas.html')