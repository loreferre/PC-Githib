from flask import session, render_template, redirect, request
from app_autos.modeladores.modelo_autos import Autos
from app_autos import app
from flask import flash


@app.route('/dashboard', methods=['GET'])
def mostrar_autos():
    if "id_usuario" not in session:
        return redirect('/')
    else:
        lista_autos=Autos.mostrar_todos_los_autos()
        return render_template ('/dashboard.html', lista_autos=lista_autos)


@app.route('/formulario/nuevo/auto', methods=['GET'])
def formulario_añadir_auto():
    if "id_usuario" not in session:
        return redirect('/')
    else:
        return render_template('/formulario_autos.html')

@app.route('/crear/auto', methods=['POST'])
def agregar_auto():
    print(request.form)
    data={
        **request.form,
        "id_usuario" : session['id_usuario']
    }
    if Autos.validar_formulario_autos(data) ==False:
        return redirect('/formulario/nuevo/auto')
    else:
        id_autos=Autos.agregar_auto(data)
        return redirect('/dashboard')
    
@app.route('/eliminar_auto/<int:id>', methods=['POST']) 
def eliminar_auto (id):
    data ={
        "id" : id
    }
    Autos.elimina_uno(data)
    return redirect("/dashboard")

@app.route('/info_auto/<int:id>', methods=['GET'])
def desplegar_info_auto(id):
    if "id_usuario" not in session:
        return redirect('/')
    else:
        data = {
            "id": id
        }
        auto = Autos.obtener_uno_con_usuario(data)
        return render_template('info_auto.html', auto=auto)
    
@app.route('/formulario/editar/<int:id>', methods=['GET'])
def formulario_para_editar(id):
    data={
        "id":id
    }
    if "id_usuario" not in session:
        return redirect('/')
    else:
        auto=Autos.obtener_uno(data)
        return render_template('formulario_editar.html', auto = auto)

@app.route('/editar/auto/<int:id>', methods=['POST'])
def editar_auto(id):
    data = {
        "id": id,
        **request.form,
    }
    if not Autos.validar_formulario_autos(data):
        flash('Error en el formulario', 'error')
        return redirect(f'/formulario/editar/{id}')
    else:
        Autos.editar_uno(data)
        return redirect('/dashboard')