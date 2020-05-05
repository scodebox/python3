import pymysql

db = pymysql.connect("localhost","root","","hack" )
cursor = db.cursor()

sql = "SELECT name,password FROM phone WHERE adher_id='%d'"%(102)
cursor.execute(sql)
results = cursor.fetchall()
print (results)
db.close()