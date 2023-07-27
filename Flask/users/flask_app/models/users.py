from flask_app.config.mysqlconnection import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        resultados = connectToMySQL('users').query_db(query)
        users = []
        for user in resultados:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
        return connectToMySQL('users').query_db(query, data)
    
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id": id}
        result = connectToMySQL('users').query_db(query, data)
        
        if len(result) < 1:
            return False
        else:
            return cls(result[0])
    
    @classmethod
    def edit(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id": id}
        result = connectToMySQL('users').query_db(query, data)
        
        if len(result) >0 :
            return False
        else:
            return cls(result[0])
        
    @classmethod
    def delete_by_id(cls, id):
        query = "DELETE * FROM users WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL('users').query_db(query, data)
    

    @classmethod
    def update(cls, id, new_data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('users').query_db(query, new_data)           
