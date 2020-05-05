import sqlite3
import time

conn = sqlite3.connect('student.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS studentData(id INTEGER, name TEXT, roll INTEGER, stream TEXT)")

def data_entry(id):
    name = input('Enter name : ')
    roll = int(input('Enter roll : '))
    stream = input('Enter stream : ')

    c.execute("INSERT INTO studentData (id, name, roll, stream) VALUES (?,?,?,?)",(id, name, roll, stream))
    conn.commit()


create_table()
i = 1
for i in range(10):
    data_entry(i)
    i+=1
    time.sleep(1)

c.close()
conn.close()
