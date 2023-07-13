from app_autos.config.mysqlconecction import connectToMySQL
from app_autos.modeladores.modelo_user import Usuario
from app_autos import BASE_DATOS
from flask import flash

class Autos:
    def __init__(self, data):
        self.id = data['id']
        self.precio = data['precio']
        self.modelo = data['modelo']
        self.marca = data['marca']
        self.año = data['año']
        self.id_usuario = data['id_usuario']
        self.descripcion = data['descripcion']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
        self.usuario = None

    @classmethod
    def agregar_auto(cls, data):
        query = """
            INSERT INTO autos (precio, modelo, marca, año, descripcion, id_usuario)
            VALUES (%(precio)s, %(modelo)s, %(marca)s, %(año)s, %(descripcion)s, %(id_usuario)s)
        """
        id_autos = connectToMySQL(BASE_DATOS).query_db(query, data)
        return id_autos

    @classmethod
    def mostrar_todos_los_autos(cls):
        query = """
            SELECT *
            FROM autos JOIN usuarios u
            ON autos.id_usuario = u.id;
        """
        resultado = connectToMySQL(BASE_DATOS).query_db(query)
        lista_autos = []
        if resultado:
            for renglon in resultado:
                autos = Autos(renglon)
                data_usuario = {
                    "id": renglon['u.id'],
                    "nombre": renglon['nombre'],
                    "apellido": renglon['apellido'],
                    "email": renglon['email'],
                    "password": renglon['password'],
                    "fecha_creacion": renglon['u.fecha_creacion'],
                    "fecha_actualizacion": renglon['u.fecha_actualizacion'],
                }
                usuario = Usuario(data_usuario)
                autos.usuario = usuario
                lista_autos.append(autos)
        return lista_autos

    @classmethod
    def elimina_uno(cls, data):
        query = """
            DELETE FROM autos
            WHERE id = %(id)s;
        """
        return connectToMySQL(BASE_DATOS).query_db(query, data)

    @classmethod
    def obtener_uno_con_usuario(cls, data):
        query = """
            SELECT *
            FROM autos a JOIN usuarios u
            ON a.id_usuario = u.id
            WHERE a.id = %(id)s
        """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, data)
        if resultado:
            renglon = resultado[0]
            autos = Autos(renglon)
            data_usuario = {
                "id": renglon['u.id'],
                "nombre": renglon['nombre'],
                "apellido": renglon['apellido'],
                "email": renglon['email'],
                "password": renglon['password'],
                "fecha_creacion": renglon['u.fecha_creacion'],
                "fecha_actualizacion": renglon['u.fecha_actualizacion'],
            }
            usuario = Usuario(data_usuario)
            autos.usuario = usuario
            return autos
        else:
            return None

    @classmethod
    def obtener_uno(cls, data):
        query = """
            SELECT *
            FROM autos
            WHERE id = %(id)s;
        """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, data)
        autos = Autos(resultado[0])
        return autos

    @classmethod
    def editar_uno(cls, data):
        query = """
            UPDATE autos
            SET precio = %(precio)s, modelo = %(modelo)s, marca = %(marca)s, año = %(año)s, descripcion = %(descripcion)s, id_usuario = %(id_usuario)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(BASE_DATOS).query_db(query, data)

    @staticmethod
    def validar_formulario_autos(data):
        es_valido = True
        if not data['precio'].isdigit() or int(data['precio']) < 0:
            es_valido = False
            flash("Debes escribir un monto superior a 0", "error_precio")
        if len(data['modelo']) < 2:
            es_valido = False
            flash("Debes escribir el campo modelo", "error_modelo")
        if len(data['marca']) < 2:
            es_valido = False
            flash("Debes escribir el campo marca", "error_marca")
        if data['año'] == "":
            es_valido = False
            flash("Debes seleccionar el fecha año de fabricacion", "error_año")
        if len(data['descripcion']) < 10:
            es_valido = False
            flash("Debes escribir el campo descripcion", "error_descripcion")
        return es_valido