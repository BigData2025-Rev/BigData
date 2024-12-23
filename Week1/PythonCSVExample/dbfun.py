"""
This module demonstrates how to use sqllite

"""
import sqlite3

conn = sqlite3.connect('students.db')

c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS students""")
c.execute("""CREATE TABLE students (name TEXT, age INTEGER)""")
c.execute("""INSERT INTO STUDENTS VALUES ('Mark', 18)""")

c.execute("""SELECT * FROM STUDENTS""")

rows = c.fetchall()
for row in rows:
    print(row)

conn.commit()

conn.close()
