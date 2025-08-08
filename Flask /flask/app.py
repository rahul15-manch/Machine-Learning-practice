from flask import Flask
'''This code initializes a Flask application.'''
app= Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask Application!"
@app.route("/index")
def index():
    return "This is the index page of the Flask Application!"







if __name__ == '__main__':
    app.run(debug=True)