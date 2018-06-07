#encoding: utf-8

import json
from users import Users
from flask import Flask, render_template, redirect, url_for, request, make_response
from common import db, app


@app.route('/')
def index():
	return redirect(url_for('login'))

@app.route('/login/', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		user_name = request.form.get('name')
		if user_name:
			some_body = Users.query.filter_by(name=user_name).first()
			if some_body:
				user_pwd = request.form.get('password')
				if user_pwd and user_pwd == some_body.password:
					return u'登录成功！'
				else:
					return u'密码错误！'
			else:
				return u'无此用户！'		
		else:
			return u'登录失败！'
	return render_template('index.html')
	

if __name__ == '__main__':
	app.run(host='192.168.1.108', port=8000, debug=True)
