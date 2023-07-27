from flask import Flask, render_template
# importar la clase de friend.py
from friends import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends=friends)
            
if __name__ == "__main__":
    app.run(debug=True)