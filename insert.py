import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor=conn.curson()

filename='test.wav'

with open ('file', 'rb') as f:
    data=f.read()

cursor.execute(
INSERT INTO my_table (absolute_path, filename) VALUES (?,?)""" (filename))
)


conn.commit()
cursor.close()
conn.close()
