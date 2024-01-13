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
    conn = sqlite3.connect('db_name')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
def check_answer(quest_id, answer):
    query = '''
        SELECT question.answer FROM quiz_content, question WHERE quiz_content.id = ? 
        AND quiz_content.question_id = question.id
    '''
    open()
    cursor.execute(query, str(quest_id))
    result = cursor.fetchone()
    close()
    if result is None:
        return False
    else:
        if result[0] == answer:
            return True
        else:
            return False