import mysql.connector

class MysqlSearch(object):

	def __init__(self):
		self.get_conn()

	def get_conn(self):
		# get connection
			self.conn = mysql.connector.connect(
				host='127.0.0.1',
				user='root',
				passwd='',
				db='news',
				port='3306'
			)

	def close_conn(self):
			if self.conn:
				#close connection
				self.conn.close()


	def get_one(self):
		# SQL
		sql = "SELECT * FROM news"
		cursor = self.conn.cursor()
		cursor.execute(sql)
		# get outcome
		rest = cursor.fetchone()

		print(rest)
		# close cursor and conneciton
		cursor.close()
		self.close_conn()

	def add_one(self):
		# SQL
		sql = (
			"INSERT INTO news (title, image, content, types) VASLUE"
			"('标题1'， '','新闻内容1','推荐');"
			)
		# get connection and cursor
		cursor = self.conn.cursor()
		cursor.execute()
		# add data to database
		# close cursor and conneciton


def main():
	obj = MysqlSearch()
	obj.get_one()


if __name__ == '__main__':
	main()