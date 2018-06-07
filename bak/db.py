#encoding: utf-8
import MySQLdb


def get_conn():
	host = '127.0.0.1'
	port = 3306
	db = 'TB_MIS_DEV'
	user = 'root'
	password = '123456'
	conn = MySQLdb.connect(host=host, user=user, passwd=password, db=db, port=port, charset='utf8')
	return conn





