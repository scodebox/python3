import sqlite3

conn = sqlite3.connect('student.db')
c  = conn.cursor()


def delete():
    c.execute('DELETE FROM studentData WHERE id = 99')
    conn.commit()



def updateTable(old,new):
    c.execute('SELECT * FROM studentData')
    [print(row) for row in c.fetchall()]

    c.execute('UPDATE studentData SET id = (?) where id=(?)',(new,old))
    conn.commit()

    c.execute('SELECT * FROM studentData')
    [print(row) for row in c.fetchall()]


updateTable(33,3)
# delete()