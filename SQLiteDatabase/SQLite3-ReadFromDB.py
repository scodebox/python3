import sqlite3

conn = sqlite3.connect('student.db')
c  = conn.cursor()

def read_from_db():
    c.execute('SELECT * FROM studentData')

    ### DISPLAY APP DATA.
    # data = c.fetchall()
    # print (data)

    ### DISPLAY ONE ROW.
    # data = c.fetchone()
    # print (data)

    ### DISPLAY ROW WISE.
    data = c.fetchall()
    for row in data:
        print (row)



read_from_db()