import sqlite3


def get_question(quiz_id, question_id):
    conn = sqlite3.connect("quiz.splite")
    cursor = conn.cursor()

    cursor.execute('''SELECT question.question FROM  question , quiz_content
                   WHERE quiz_content.question_id == question.id == question.id
                   AND question.id = ?
                   AND quiz_content.quiz_id == ?''', [question_id,quiz_id])
    data = cursor.fetchall()
    return data
def get_quises():
    query = 'SELECT * FROM quiz ORDER BY id'
    conn = sqlite3.connect(main_2)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    return result