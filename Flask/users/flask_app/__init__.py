from flask import Flask

app = Flask(__name__)
app.secret_key = "shhhhhh"

from flask_app.controllers import users