from flask import Flask , session
from random import randint
from puiz_sql import get_question

def index():
    session['counter'] = 0
    session['counter'] = randint(1,2)
    return '<a href="/test" >start Test</a>'

def test():
    data = get_question(session['counter'] , session['counter'])
    session['counter']
    return f"<h1>{session['counter']}</h1>"
def result ():
    return''
app = Flask(__name__)

app.config["SECRET_KEY"] = 'qweqwe123'
app.add_url_rule('/' , "home", index)
app.add_url_rule('/test' , "test" , test)
app.add_url_rule('/result' , "result" , result)

app.run()