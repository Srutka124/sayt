from flask import Flask , session
from random import randint
from puiz_sql import get_question
import main_2
def start_quiz():
    session['quiz'] = quiz_id
    session['last_question'] = 0
def index():
    session['counter'] = randint(0,1)
    session['counter2'] = randint(0,1)
    return '<a href="/test" >start Test</a>'

def test():
    data = get_question( session['counter'],session['counter'])
    return f"<h1>{session['counter']}</h1>"
def result ():
    return''
app = Flask(__name__)

app.config["SECRET_KEY"] = 'qweqwe123'
app.add_url_rule('/' , "home", index)
app.add_url_rule('/test' , "test" , test)
app.add_url_rule('/result' , "result" , result)
if __name__ == '__main__':

    app.run()