from flask import Flask,render_template,request 
'''This code initializes a Flask application.'''
app= Flask(__name__)

@app.route('/')
def welcome():
    return "<html> <h1> Welcome to the Flask Application! </h1></html> ``"
@app.route("/index")
def index():
    return render_template("index.html",method=["GET"])
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"<h1>Hello, {name}!</h1>"
    return render_template("form.html")
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    return f"<h1>Form submitted successfully! Hello, {name}!</h1>"







if __name__ == '__main__':
    app.run(debug=True)