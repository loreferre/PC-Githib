from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    session["checkout"] = {
        "raspberry": request.form["raspberry"],
        "apple": request.form["apple"],
        "blackberry": request.form["blackberry"],
        "strawberry": request.form["strawberry"],
        "First_Name": request.form["First_Name"],
        "Last_Name": request.form["Last_Name"],
        "Your_Student": request.form["Your_Student"]
    }
    return redirect("/show_checkout")   
        
@app.route('/show_checkout', methods=['GET'])
def show_checkout():
    if "checkout" not in session:
        return redirect("/")
    else:
        return render_template("checkout.html", checkout=session["checkout"], session=session)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)