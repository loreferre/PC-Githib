from app_revistas.config.mysqlconnection import connectToMySQL
from app_revistas.modelos.modelo_user import Usuario
from app_revistas import BASE_DATOS, EMAIL_REGEX, NOMBRE_REGEX
from flask import flash


class Revistas:
    def __init__(self, data):
        self.id = data['id']
        self.titulo = data['titulo']
        self.descripcion = data['descripcion']
        self.fecha_creacion = data['fecha_creacion']
        self.fecha_actualizacion = data['fecha_actualizacion']
        self.usuarios_id = data['usuarios_id']
        self.usuario = None

    @classmethod
    def agregar_uno(cls, data):
        query = """INSERT INTO revistas (titulo, descripcion, Usuarios_id) 
                VALUES (%(titulo)s, %(descripcion)s, %(Usuarios_id)s)"""
        id_revista = connectToMySQL(BASE_DATOS).query_db(query, data)
        return id_revista

    @classmethod
    def obtener_suscripciones(cls):
        query = """SELECT *
                FROM revistas r JOIN usuario u
                ON r.id = u.id 
                """
        resultados = connectToMySQL(BASE_DATOS).query_db(query)
        lista_revistas = []
        for renglon in resultados:
            revista = Revistas(renglon)
            data_usuario = {
                'id': renglon['u.id'],
                'nombre': renglon['u.nombre'],
                'apellido': renglon['u.apellido'],
                'email': renglon['email'],
                'password': renglon['password'],
                'fecha_creacion': renglon['fecha_creacion'],
                'fecha_actualizacion': renglon['u.fecha_actualizacion']
            }
            usuario = Usuario(data_usuario)
            revista.usuario = usuario
            lista_revistas.append(revista)

        return lista_revistas

    @staticmethod
    def validador_formulario_revistas(data):
        se_valida = True
        if len(data['titulo']) < 2:
            se_valida = False
            flash("El nombre debe tener al menos tres caracteres", "error_titulo")
        if len(data['descripcion']) < 10:
            se_valida = False
            flash("Debes completar la descripcion de la revista", "error_descripcion")
        return se_valida