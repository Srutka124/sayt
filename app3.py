from flask import Flask, render_template , session , request,redirect ,url_for
from random import shuffle
from puiz_sql import get_question_after ,get_quises,check_answer
import main_2
def index():


    if request.method == 'GET':

        quizz = get_quises()
        return render_template("index.html", quizz=quizz ,title = "121212121211")
    else:
        session["quiz_id"] = request.form.get('quiz')
        session["question_id"] = 0
        session['total'] = 0
        session['answer'] = 0
        return redirect(url_for("test"))

def test():
    if 'quiz_id' not in session :
        return redirect(url_for('index'))
    
    if request.method == "POST":
        answer = request.form.get('quiz')
        quest_id  =request.form.get('q_id')

        session["question_id"]  = quest_id
        session['total'] += 1

        if check_answer(quest_id , answer):
            session['answer'] += 1
    print(session["question_id"],session["quiz_id"])


    question = get_question_after(session["question_id"],session["quiz_id"])
    print(question)
    if question is None :
        return redirect(url_for('result'))
    
    answers  = [question[2] ,question[3] ,question[4] ,question[5]]
    shuffle(answers)
    return render_template('test.html' , question = question[1], answers = answers , question_id = question[0])
    
app = Flask(__name__, template_folder = '', static_folder= '')



def result():
    return render_template("result.html",
                            right=session['answer'], 
                           total=session['total'])
    
app = Flask(__name__, template_folder='', static_folder='')
app.config["SECRET_KEY"] = 'secret'
app.add_url_rule("/", "index", index)
app.add_url_rule("/index", "index", index, methods=["POST", "GET"])

app.add_url_rule("/test", "test", test, methods=["POST", "GET"])
app.add_url_rule("/result", "result", result)

app.run(debug=True)