from flask import Flask, render_template , session , request,redirect ,url_for
from puiz_sql import get_question ,get_quises
def index():
    if request.method == 'GET':

        quizz = get_question()
        return render_template("index.html", quizz=quizz ,title = "121212121211")
    else:
        print(request.form.get('quiz'))
        session["question_id"] = 1
        return redirect(url_for('test'))

def test():
    if request.method == 'POST':
        session["question_id"] += 1
    question = get_question(session["question_id"],session["quiz_id"])
    answers  = ["ede","asasas","esdsfd","dvge"]
    return render_template('test.html' , question = question, answers = answers)
app = Flask(__name__, template_folder = '', static_folder= '')

app.add_url_rule('/','home', index )
app.add_url_rule('/index','index', index , methods=['GET', 'POST'])
app.add_url_rule('/test','test', test , methods=['GET', 'POST)
app.run()