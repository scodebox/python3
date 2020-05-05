import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS userData(id REAL, name TEXT, roll REAL, stream TEXT)")

def data_entry():
    c.execute("INSERT INTO userData VALUES(1, 'Suvam Basak', 102, 'CSE')")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
print ('done')