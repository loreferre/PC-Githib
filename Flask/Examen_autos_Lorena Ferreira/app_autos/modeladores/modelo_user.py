from app_autos.config.mysqlconecction import connectToMySQL
from app_autos import BASE_DATOS, EMAIL_REGEX, NOMBRE_REGEX 
from flask import flash

class Usuario: # controlador de usuario
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido= data['apellido']
        self.email=data['email']
        self.password=data['password']
        self.fecha_creacion=data['fecha_creacion']
        self.fecha_actualizacion=data['fecha_actualizacion']

    @classmethod #Registro
    def crear_uno (cls, data):
        query=""" 
                INSERT INTO usuarios (nombre, apellido, email, password)
                VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s)"""
        resultado = connectToMySQL(BASE_DATOS).query_db(query,data)
        return resultado
    
    @classmethod #login
    def obtener_uno_con_email(cls, data): #se conecta en el controlado
        query= """
                SELECT *
                FROM usuarios
                WHERE email = %(email)s"""
        resultado = connectToMySQL (BASE_DATOS).query_db(query, data)

        if len (resultado) == 0:
            return None
        else:
            return Usuario(resultado[0])



    @staticmethod #validacion de registro
    def validar_registro(data):
        es_valido=True
        if len(data['nombre']) < 3:
            es_valido = False
            flash("Tu nombre debe contener al menos 2 caracteres", "error_nombre")

        if not NOMBRE_REGEX.match(data['nombre']):
            es_valido =False
            flash ("Por favor proporciona un nobmre valido (Solo letas)", "error_nombre")

        if not NOMBRE_REGEX.match(data['apellido']):
            es_valido = False
            flash("El formato del campo apellido no es válido.", "error_apellido")      
        if len(data['apellido']) < 3:
            es_valido = False
            flash("Tu apellido debe contener al menos 2 caracteres", "error_apellido")


        if not EMAIL_REGEX.match(data['email']):
                es_valido = False
                flash("El formato del email no es válido.", "error_email")

        if len(data['password']) < 8:
                es_valido = False
                flash("La contraseña debe tener por lo menos ocho caracteres", "error_password")

        if data['password'] != data['confirmar_password']:
                es_valido = False
                flash("Tus contraseñas no coinciden.", "error_password")

        return es_valido





