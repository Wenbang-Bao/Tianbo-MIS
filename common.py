
#encoding: utf-8
from flask import Flask, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder = './dist/static', template_folder = './dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/TB_MIS_DEV'
db = SQLAlchemy(app)

def get_info_from_request(keys=[]):
	values = []
	for key in keys:
		values.append(request.form.get('message['+key+']'))
	return values
	
