import sqlite3

conn = sqlite3.connect('student.db')
c  = conn.cursor()

def read_from_db():
    # c.execute('SELECT * FROM studentData WHERE id=3')
    # c.execute('SELECT * FROM studentData WHERE id=9 AND roll=97')
    # c.execute('SELECT * FROM studentData WHERE id>2 AND id<8')
    # c.execute('SELECT * FROM studentData WHERE id>3')
    # c.execute('SELECT name FROM studentData WHERE id=3')
    c.execute('SELECT name,roll FROM studentData WHERE id=3')

    data = c.fetchall()
    for row in data:
        print (row)



read_from_db()