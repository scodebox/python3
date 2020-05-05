import pymysql

db = pymysql.connect("localhost","root","","hack" )
cursor = db.cursor()

sql = "SELECT * FROM phone"
cursor.execute(sql)
results = cursor.fetchall()
print (results)
db.close()