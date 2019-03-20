import mysql.connector

# get connection
try:
	conn = mysql.connector.connect(
		host='127.0.0.1',
		user='root',
		passwd='',
		db='news',
		port='3306'
	)

# get data
cursor = conn.cursor()
cursor.execute('SELECT * FROM news')
rest = cursor.fetchone()
print(rest)

#close coonection
conn.close()

# exception
except mysql.connector.Error as e:
	print("Error: %s" % e)