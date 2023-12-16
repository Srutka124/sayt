import sqlite3

conn = sqlite3.connect("cuiz.splite")

cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS quizz")
cursor.execute("DROP TABLE IF EXISTS question")
cursor.execute("DROP TABLE IF EXISTS quizz_conntent")
conn.commit()
cursor.execute('''
CREATE TABLE IF NOT EXISTS puizz(id INTREGER PRIMARY KEY , quizz VARCHAR)''')
conn.commit()
cursor.execute(''' CREATE TABLE IF NOT EXISTS question(id INTEREGER PRIMARI KEY , question VARCHAR , answer VARCHAR, worg1 VARCHAR,worg2 VARCHAR,worg3 VARCHAR )''')
conn.commit()
cursor.execute('''
CREATE TABLE IF NOT EXISTS quiz_content(id INTREGER PRIMARY KEY ,
                quiz_id  INTEGER,
               question_id INTEGER,
               FOREIGN KEY (quizz_id) REFERENCES quizz(id),
               FOREIGN KEY (question_id) REFERENCES question(id))''')

questions = [("first","хто такий енштейн" , 'фізик' ,'біолог' , 'географ' , ),
            ("two","хто такий Tesla" , 'фізик' ,'біолог' , 'географ' ,)]

cursor.executemany('''INSERT INTO question
                   (question, answer, worg1, worg2, worg3)
                   VALUES(?,?,?,?,?)''', questions)

quiziz = [("я у світі",),("hhjjj",)]
cursor.executemany('''INSERT INTO puizz
                   (name)
                   VALUES(?)''',quiziz )

cursor.execute('''INSERT INTO quiz_content
               (quiz_id , question_id)
               VALUES(?,?)''', [1,2])
conn.commit()

cursor.execute('''SELECT * FROM puestoin , quiz_content WHERE question.id == puiz_conntent.puestion_id 
               AND quiz_content.quiz_id == ?''' , [1])
conn.commit()




data = cursor.fetchall()
print(data)