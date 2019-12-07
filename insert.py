import sqlite3

conn = sqlite3.connect('image.db')
cursor=conn.curson()

name='filename'

with open ('file', 'rb') as f:
    data=f.read()

cursor.execute("""
        INSERT INTO my_table (name, data) VALUES (?,?)""" (name,data))
        """)


conn.commit()
cursor.close()
conn.close()
