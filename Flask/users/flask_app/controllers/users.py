from flask import render_template, request, url_for, redirect
from flask_app import app
from flask_app.models.users import Users

@app.route("/")
def home():
    return redirect(url_for('user'))

@app.route("/users/new", methods=['GET', 'POST'])
def new_users_form():
    if request.method == 'POST':
        data = {
            "fname": request.form["fname"],
            "lname": request.form["lname"],
            "email": request.form["email"]
        }
        Users.save(data)
        return redirect(url_for('user'))
    return render_template("index.html")

@app.route("/users")
def user():
    return render_template("users.html", users=Users.get_all())

@app.route("/users/edit/<int:id>", methods=['GET', 'POST'])
def update_user(id):
    if request.method == 'POST':
        new_data = {
            "id": id,
            "first_name": request.form.get('first_name'),
            "last_name": request.form.get('last_name'),
            "email": request.form.get('email')
        }
        Users.update(id, new_data)
        return redirect(url_for('show_user', id=id))
    else:
        user = Users.get_by_id(id)
        return render_template("edit_user.html", user=user)

@app.route("/users/show/<int:id>", methods=['GET'])
def show_user(id):
    user = Users.get_by_id(id)
    return render_template("show_user.html", user=user)


