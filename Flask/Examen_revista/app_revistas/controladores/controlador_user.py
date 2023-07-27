from flask import session, render_template, redirect, request  
from flask import flash
from flask_bcrypt import Bcrypt
from app_revistas import app
from app_revistas.modelos.modelo_user import Usuario

bcrypt = Bcrypt(app)

@app.route("/", methods = ['GET'] )
def desplegar_login_registro():
    return render_template("registro.html")

@app.route('/crear/usuario', methods = ['POST'])  
def nuevo_usuario():
    data={
        **request.form
    }
    usuario_existe=Usuario.obtener_uno_con_email(data)
    if Usuario.validar_registro(data, usuario_existe) == False:
        return redirect('/')
    else:
        password_encriptado = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        data['password'] = password_encriptado
        id_usuario = Usuario.crear_uno(data)
        session['nombre'] = data['nombre']
        session['apellido'] = data['apellido']
        session['id_usuario'] = id_usuario

        return redirect ('/dashboard')

@app.route ('/mi_dashboard', methods = ['GET'])
def desplegar_dashboard():
    if 'nombre' not in session:
        return redirect("/")
    else:
        return render_template('dashboard.html')

@app.route('/login', methods = ['POST'])
def procesa_login():
    data={
        "email": request.form['email_login']
    }
    usuario= Usuario.obtener_uno_con_mail(data)

    if usuario == None:
        flash("Email invalido", "error_email_login")
        return redirect('/')
    else:
        if not bcrypt.check_password_hash(usuario.password, request.form['error_login_password']):
            flash ("Contraseña incorrecta","error_login_password" )
        else:
            session['nombre'] = usuario.nombre
            session['apellido'] = usuario.apellido
            session['id_usuario'] = usuario.id
            
            return redirect('dashboard')

@app.route('/logout', methods=['POST'])
def procesa_logout():
    session.clear()
    return redirect("/") 