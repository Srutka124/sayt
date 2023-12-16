
def get_question(quiz_id, question_id):
    connn = sqlite3.connect("quiz.splite")
    cursor = conn.cursor

    cursor.execute('''SELECT question.qestion, FROM question , quiz_content
                   WHERE quiz_content.question_id == question.id == question.id
                   AND question.id = ?
                   AND quiz_content.quiz_id == ?'''[question_id,quiz_id])
    data = cursor.fetchall()
    return data