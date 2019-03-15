import mysql.connector


conn = mysql.connector.connect(
	host='127.0.0.1',
	user='root',
	passwd='',
	db='news',
	port='3306'
)


cursor = conn.cursor()
cursor.execute('SELECT * FROM news')
rest = cursor.fetchone()
print(rest)

conn.close()
