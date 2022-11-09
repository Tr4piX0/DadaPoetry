import sqlite3

connection = sqlite3.connect('dada.db')


with open('dadabase.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO dada (filename, content) VALUES (?, ?)",
            ('filename', 'content of filename')
            )

connection.commit()
connection.close()
