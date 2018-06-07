#-*- coding=utf-8 -*-
import json
from common import app, db
from CustomerInfo import CustomerInfo
from ProductInfo import ProductInfo
from flask import Flask, render_template, request, jsonify

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/product-page/', methods=['POST', 'GET'])
def product_management():
	if request.method == 'POST':
		cmd = request.form.get('command')
		if cmd == 'SAVE_PRODUCT_INFO':
			product = ProductInfo.get_pro_from_request()
			if product:
				ProductInfo.add_item(product)
				item = ProductInfo.get_newest_item()
				return jsonify(item)
		elif cmd == 'GET_PRODUCT_INFO':
			print 'hllooooooo\n'
			offset = request.form.get('filter[offset]')
			size = request.form.get('filter[size]')
			items = ProductInfo.get_item_by_filter(offset, size)
			print items
			return jsonify(items)
			
	return render_template('index.html')



@app.route('/cust-page/', methods=['POST', 'GET'])
def customer_management():
	if request.method == 'POST':
		print "data is coming!"
		cmd = request.form.get('command')
		if cmd == 'SAVE_CUSTOMER_INFO':
			name = request.form.get('message[name]')
			contacter1 = request.form.get('message[contacter1]')
			position1 = request.form.get('message[position1]')
			email1 = request.form.get('message[email1]')
			telephone1 = request.form.get('message[telephone1]')
			cellphone1 = request.form.get('message[cellphone1]')
			contacter2 = request.form.get('message[contacter2]')
			position2 = request.form.get('message[position2]')
			email2 = request.form.get('message[email2]')
			telephone2 = request.form.get('message[telephone2]')
			cellphone2 = request.form.get('message[cellphone2]')
			classes = request.form.get('message[classes]')
			level = request.form.get('message[level]')
			credit = request.form.get('message[credit]')
			postcode = request.form.get('message[postcode]')
			address = request.form.get('message[address]')
			comment = request.form.get('message[comment]')
			customer = CustomerInfo(name, 
									contacter1, position1, email1, telephone1, cellphone1,\
									contacter2, position2, email2, telephone2, cellphone2,\
									classes, level, credit, postcode, address, comment)
			db.session.add(customer)
			db.session.commit()
			item = CustomerInfo.query.filter_by(id=customer.id).first()
			if item:
				return jsonify(item.to_dict())			
			else:
				return 'FAIL'
		elif cmd == 'GET_CUSTOMER_INFO':
			print 'send data'	
			size = request.form.get('filter[size]')
			offset = request.form.get('filter[offset]')
			print size
			print offset
			end = offset + size
			infos = CustomerInfo.query.filter('id>:id').params(id=offset).limit(size)
			return jsonify([item.to_dict() for item in infos])
			
	return render_template('index.html')


if __name__ == '__main__':
	app.run(host='150.236.226.92', port=8080, debug=True)
