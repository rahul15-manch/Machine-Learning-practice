from flask import Flask, render_template, request,redirect, url_for
#{{}} to print the code in html document
#{%...%} for confrol structures like loops and conditionals
#{#...#} for comments in jinja templates
app = Flask(__name__)
@app.route('/')
def welcome():
    return "<html> <h1> Welcome to the Flask Application! </h1></html>" 
@app.route("/success/<int:score>")
def success(score: int):
    res=""
    if score >= 50:
        res = "Congratulations! You passed the exam."
    else:
        res = "Unfortunately, you did not pass the exam. Please try again."
    return render_template("result.html", result=res) 

@app.route("/success_result/<int:score>") 
def success_result(score: int):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    exp ={"score": score, "result": res}
    return render_template("result1.html", result=exp) 
@app.route("/score_if/<int:score>")
def score_if(score: int):
    return render_template("result.html", score=score)

@app.route("/fail/<int:score>")
def fail(score: int):
    return render_template("result.html", score=score)

@app.route("/submit", methods=['POST',"GET"])
def submit():
    total_marks = 0
    if request.method == 'POST':
        science_marks = int(request.form.get('science', 0))
        math_marks = int(request.form.get('math', 0))
        datascience_marks = int(request.form.get('datascience', 0))
        
        total_marks = (science_marks + math_marks + datascience_marks)/3
        return redirect(url_for('success_result', score=total_marks))
    return render_template("getresult.html")
if __name__ == '__main__':
    app.run(debug=True)