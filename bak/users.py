#encoding: utf-8

from common import db

class Users(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)
	password = db.Column(db.String)

	def __init__(self, id, name, pwd):
		self.id = id
		self.name = name
		self.password = pwd

	def store(self):
		conn = get_conn()
		cursor = conn.cursor()
		sql = 'insert into UserInfo (name, password) VALUES (%s, %s)'
		cursor.execute(sql, (self.name, self.password))
		conn.commit()
		cursor.close()
		conn.close()
		
		
