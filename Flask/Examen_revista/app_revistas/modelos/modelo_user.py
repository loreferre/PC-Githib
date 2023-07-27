from app_revistas.config.mysqlconnection import connectToMySQL
from app_revistas import BASE_DATOS, EMAIL_REGEX, NOMBRE_REGEX
from flask import flash 

class Usuario:
        def __init__(self, data):
                self.id = data['id']
                self.nombre = data['nombre']
                self.apellido = data['apellido']
                self.email = data['email']
                self.password = data['password']
                self.fecha_creacion = data['fecha_creacion']
                self.fecha_actualizacion = data ['fecha_actualizacion']

        @classmethod
        def crear_uno(cls, data):
                query = """INSERT INTO registro (nombre, apellido, email, password) 
                        VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s)"""
                resultado = connectToMySQL(BASE_DATOS).query_db(query, data)
                return resultado 

        @classmethod
        def obtener_uno_con_mail(cls, data):
                query = """SELECT * 
                        FROM registro 
                        WHERE email = %(email)s"""

                resultado = connectToMySQL(BASE_DATOS).query_db(query, data)
                
                if len(resultado) == 0:
                        return None
                else:
                        return Usuario(resultado[0])

        @staticmethod
        def validar_registro(data, usuario_existe):
                se_valida = True
                if len(data['nombre']) < 3:
                        se_valida = False
                        flash("Tu nombre debe contener al menos 3 caracteres", "error_nombre")

                if not NOMBRE_REGEX.match(data['nombre']):
                        se_valida = False
                        flash("El formato del campo Nombre no es válido.", "error_nombre")

                if not NOMBRE_REGEX.match(data['apellido']):
                        se_valida = False
                        flash("El formato del campo apellido no es válido.", "error_apellido")
                if len(data['apellido']) < 2:
                        se_valida = False
                        flash("Tu nombre debe contener al menos 2 caracteres", "error_apellido")
                
                if not EMAIL_REGEX.match(data['email']):
                        se_valida = False
                        flash("El formato del email no es válido.", "error_email")

                if len(data['password']) < 8:
                        se_valida = False
                        flash("La contraseña debe tener por lo menos ocho caracteres", "error_password")

                if data['password'] != data['confirmar_password']:
                        se_valida = False
                        flash("Tus contraseñas no coinciden.", "error_password")
                if usuario_existe != None:
                        se_valida = False
                        flash('Este correo ya esta registrado', "error_email")

                return se_valida