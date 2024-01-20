import sqlite3

conn = sqlite3.connect("cuiz.sqlite")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS quiz")
cursor.execute("DROP TABLE IF EXISTS question")
cursor.execute("DROP TABLE IF EXISTS quiz_content")
conn.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS quiz(id INTEGER PRIMARY KEY, name VARCHAR)''')
conn.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS question(id INTEGER PRIMARY KEY, question_text VARCHAR, answer VARCHAR, wrong1 VARCHAR, wrong2 VARCHAR, wrong3 VARCHAR , wrong4 VARCHAR)''')
conn.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS quiz_content(id INTEGER PRIMARY KEY,
                quiz_id INTEGER,
                question_id INTEGER,
                FOREIGN KEY (quiz_id) REFERENCES quiz(id),
                FOREIGN KEY (question_id) REFERENCES question(id))''')
conn.commit()

questions = [
    ("Who is Einstein?", 'Physicist', 'Biologist', 'Geographer', 'Chemist', 'Astronomer'),
    ("Who is Tesla?", 'Physicist', 'Inventor', 'Engineer', 'Mathematician', 'Physician'),
    ("What is the capital of France?", 'Paris', 'Berlin', 'London', 'Rome', 'Madrid'),
    ("Which planet is known as the Red Planet?", 'Mars', 'Venus', 'Jupiter', 'Saturn', 'Neptune'),
    ("What is the powerhouse of the cell?", 'Mitochondria', 'Nucleus', 'Endoplasmic Reticulum', 'Ribosome', 'Golgi Apparatus')
    # Додайте інші питання, якщо потрібно
]

cursor.executemany('''INSERT INTO question
                   (question_text, answer, wrong1, wrong2, wrong3, wrong4)
                   VALUES(?,?,?,?,?,?)''', questions)

quizzes = [("World Knowledge",), ("General Science",)]
cursor.executemany('''INSERT INTO quiz
                   (name)
                   VALUES(?)''', quizzes)

for question_id in range(1, len(questions) + 1):
    cursor.execute('''INSERT INTO quiz_content
                   (quiz_id, question_id)
                   VALUES(?,?)''', [1, question_id])

conn.commit()

# Перевірка результатів
cursor.execute('''SELECT * FROM question, quiz_content WHERE question.id == quiz_content.question_id 
               AND quiz_content.quiz_id == ?''', [1])
conn.commit()

data = cursor.fetchall()
print(data)