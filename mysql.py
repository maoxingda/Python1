import pymysql

dbTest = pymysql.connect(host='localhost', user='root', passwd='010203', db='test')

cursor = dbTest.cursor()

cursor.execute("select * from table1;")

for row in cursor.fetchall():
    print(row)

dbTest.close()
