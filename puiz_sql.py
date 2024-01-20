import sqlite3

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
                wrong3 VARCHAR)'''
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
        ('Скільки місяців на рік мають 28 днів?', 'Всі', 'Один', 'Ні одного', 'Два'),
        ('Яким стане зелена скеля, якщо впаде в Червоне море?', 'Мокрою?', 'Червоною', 'Не зміниться', 'Фіолетовою'),
        ('Якою рукою краще розмішувати чай?', 'Ложкою', 'Правою', 'Лівою', 'Будь-якою'),
        ('Що не має довжини, глибини, ширини, висоти, а чи можна виміряти?', 'Час', 'Безглуздість', 'Море', 'Повітря'),
        ('Коли мережею можна витягти воду?', 'Коли вода замерзла', 'Коли немає риби', 'Коли спливла золота рибка', 'Коли мережа порвалася'),
        ('Що більше за слона і нічого не важить?', 'Тінь слона', 'Повітряна куля', 'Парашут', 'Хмара'),
        ('Що таке в кишені?', 'Кільце', 'Кулак', 'Дірка', 'Бублик')
    ]
    open_db()
    cursor.executemany('''INSERT INTO question (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)''', questions)
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
    answer = input("Додати зв'язок (y / n)?")
    while answer != 'n':
        quiz_id = int(input("id вікторини: "))
        question_id = int(input("id питання: "))
        cursor.execute(query, [quiz_id, question_id])
        conn.commit()
        answer = input("Додати зв'язок (y / n)?")
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