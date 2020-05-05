import sqlite3

conn = sqlite3.connect('student.db')
c = conn.cursor()

def read_data(column,name,value):
    c.execute("SELECT " +column+" FROM studentData WHERE "+name+"=?",(value,))

    data = c.fetchall()
    for row in data:
        return row



data = read_data('id','roll','63')
print (data)