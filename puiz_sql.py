import sqlite3
from random import randint
db_name = 'quiz.sqlite'
conn = None
cursor = None


def open_db():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close_db():
    cursor.close()
    conn.close()


def execute_query(query):
    cursor.execute(query)
    conn.commit()


def clear_db():
    open_db()
    execute_query('''DROP TABLE IF EXISTS quiz_content''')
    execute_query('''DROP TABLE IF EXISTS question''')
    execute_query('''DROP TABLE IF EXISTS quiz''')
    close_db()


def create_tables():
    open_db()
    cursor.execute('''PRAGMA foreign_keys=on''')

    execute_query('''CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY, 
            name VARCHAR)'''
    )

    execute_query('''CREATE TABLE IF NOT EXISTS question (
                id INTEGER PRIMARY KEY, 
                question VARCHAR, 
                answer VARCHAR, 
                wrong1 VARCHAR, 
                wrong2 VARCHAR, 
                wrong3 VARCHAR,
                wrong4 VARCHAR)
                  '''
    )

    execute_query('''CREATE TABLE IF NOT EXISTS quiz_content (
                id INTEGER PRIMARY KEY,
                quiz_id INTEGER,
                question_id INTEGER,
                FOREIGN KEY (quiz_id) REFERENCES quiz (id),
                FOREIGN KEY (question_id) REFERENCES question (id) )'''
    )
    close_db()


def show_table(table):
    query = 'SELECT * FROM ' + table
    open_db()
    cursor.execute(query)
    print(cursor.fetchall())
    close_db()


def show_tables():
    show_table('question')
    show_table('quiz')
    show_table('quiz_content')


def add_questions():
    questions = [
    ("Who is Einstein?", 'Physicist', 'Biologist', 'Geographer', 'Chemist', 'Astronomer'),
    ("Who is Tesla?", 'Physicist', 'Inventor', 'Engineer', 'Mathematician', 'Physician'),
    ("What is the capital of France?", 'Paris', 'Berlin', 'London', 'Rome', 'Madrid'),
    ("Which planet is known as the Red Planet?", 'Mars', 'Venus', 'Jupiter', 'Saturn', 'Neptune'),
    ("What is the powerhouse of the cell?", 'Mitochondria', 'Nucleus', 'Endoplasmic Reticulum', 'Ribosome', 'Golgi Apparatus')
    ]
    open_db()
    cursor.executemany('''INSERT INTO question (question, answer, wrong1, wrong2, wrong3, wrong4) VALUES (?,?,?,?,?,?)''', questions)
    conn.commit()
    close_db()


def add_quiz():
    quizzes = [
        ('Вікторина 1',),
        ('Вікторина 2',),
        ('Вікторина-незаплавна',)
    ]
    open_db()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizzes)
    conn.commit()
    close_db()


def add_links():
    open_db()
    cursor.execute('''PRAGMA foreign_keys=on''')
    query = "INSERT INTO quiz_content (quiz_id, question_id) VALUES (?,?)"
    
    links=[[1,1], [1,2], [1,3], [1,4], [1,5]]

    for i in links:
        cursor.execute(query, [i[0], i[1]])
        conn.commit()
        
    close_db()


def get_question_after(last_id=0, vict_id=1):
    open_db()
    query = '''
    SELECT quiz_content.id, question.question, question.answer, question.wrong1, question.wrong2, question.wrong3
    FROM question, quiz_content 
    WHERE quiz_content.question_id == question.id
    AND quiz_content.id > ? AND quiz_content.quiz_id == ? 
    ORDER BY quiz_content.id '''
    cursor.execute(query, [last_id, vict_id])

    result = cursor.fetchone()
    close_db()
    return result


def get_quises():
    query = 'SELECT * FROM quiz ORDER BY id'
    open_db()
    cursor.execute(query)
    result = cursor.fetchall()
    close_db()
    return result


def get_quiz_count():
    query = 'SELECT MAX(quiz_id) FROM quiz_content'
    open_db()
    cursor.execute(query)
    result = cursor.fetchone()
    close_db()
    return result


def get_random_quiz_id():
    query = 'SELECT quiz_id FROM quiz_content'
    open_db()
    cursor.execute(query)
    ids = cursor.fetchall()
    rand_num = randint(0, len(ids) - 1)
    rand_id = ids[rand_num][0]
    close_db()
    return rand_id
def check_answer(quest_id, answer):
    query = '''
        SELECT question.answer FROM quiz_content, question WHERE quiz_content.id = ? 
        AND quiz_content.question_id = question.id
    '''
    open()
    cursor.execute(query, str(quest_id))
    result = cursor.fetchone()
    close_db()
    if result is None:
        return False
    else:
        if result[0] == answer:
            return True
        else:
            return False
        

def main():
    clear_db()
    create_tables()
    add_questions()
    add_quiz()
    show_tables()
    add_links()
    show_tables()


def get_question(quiz_id, question_id):
    open_db()
    cursor.execute('''SELECT question.question FROM  question , quiz_content
                   WHERE quiz_content.question_id == question.id
                   AND question.id = ?
                   AND quiz_content.quiz_id == ?''', [question_id, quiz_id])
    data = cursor.fetchall()
    close_db()
    return data


if __name__ == "__main__":
    main()