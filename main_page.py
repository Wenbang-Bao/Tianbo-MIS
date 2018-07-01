#-*- coding=utf-8 -*-
import json
from common import app, db, generate_execel
from CustomerInfo import CustomerInfo
from ProductInfo import ProductInfo
from OrderInfo import OrderInfo
from flask import Flask, render_template, request, jsonify, make_response, send_file

header = ['客户名称', '联系人姓名', '联系人职位', '联系电话', '客户类别', '客户级别', '信用级别']
db = [['百度', '张三', '经理', '12345678', '正式客户', 'VIP客户', '5'],
	  ['腾讯', '李四', '经理', '12345678', '正式客户', '大客户', '4'],
	  ['青海康普', '王五', '经理', '12345678', '正式客户', '大客户', '3'],]




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
				item = ProductInfo.add_item(product)
				return jsonify(item)
		elif cmd == 'DELETE_PRODUCT_INFO':
			product = ProductInfo.get_pro_from_request()
			if product:
				res = ProductInfo.delete_item(product)
				return jsonify(res)
		elif cmd == 'EDIT_PRODUCT_INFO':
			product = ProductInfo.get_pro_from_request()
			if product:
				ProductInfo.update_item(product)
				item = product.get_newest_item()
				return jsonify(item)
		elif cmd == 'GET_PRODUCT_LIST':
			items = ProductInfo.get_product_list()
			return jsonify(items)
		elif cmd == 'GET_PRODUCT_INFO':
			offset = request.form.get('filter[offset]')
			size = request.form.get('filter[size]')
			print offset
			print size
			items = ProductInfo.get_item_by_filter(offset, size)
			return jsonify(items)
			
	return render_template('index.html')



@app.route('/cust-page/', methods=['POST', 'GET'])
def customer_management():
	if request.method == 'POST':
		cmd = request.form.get('command')
		if cmd == 'SAVE_CUSTOMER_INFO':
			cust = CustomerInfo.get_cust_from_request()
			if cust:
				CustomerInfo.add_item(cust)
				item = cust.get_newest_item()
				return jsonify(item)
		elif cmd == 'DELETE_CUST_INFO':
			cust = CustomerInfo.get_cust_from_request()
			if cust:
				res = CustomerInfo.delete_item(cust)
				return jsonify(res)
		elif cmd == 'GET_CUSTOMER_INFO':	
			size = request.form.get('filter[size]')
			offset = request.form.get('filter[offset]')
			print size
			print offset
			items = CustomerInfo.get_item_by_filter(offset, size)
			return jsonify(items)
		elif cmd == 'GET_CUSTOMER_LIST':
			item = CustomerInfo.get_cust_list()
			return jsonify(item)	
		
	return render_template('index.html')



@app.route('/order-page/', methods=['POST', 'GET'])
def order_management():
	if request.method == 'POST':
		cmd = request.form.get('command')
		if cmd == 'SAVE_ORDER_INFO':
			print "data is coming.."
			order = OrderInfo.get_order_from_request()
			if order:
				OrderInfo.add_item(order)	
			return 'SUCCESS'
		elif cmd == 'GET_PRODUCT_INFO':
			items = ProductInfo.get_item_by_filter(offset, size)
			print items
			return jsonify(items)	
		elif cmd == 'GET_CUST_PRO_INFO':
			return 'SUCCESS'
		elif cmd == 'DOWNLOAD_BILL_EXCEL':
			print 'get message'
			#generate_execel(header, db)
			response = make_response(send_file("xlwt_excel.xls"))
			#response.headers['Content-Type'] = 'application/octet-stream'
			response.headers['Content-Disposition'] = 'attachment;filename=xlwt_excel.xls'
			return response

	return render_template('index.html')



if __name__ == '__main__':
	app.run(host='192.168.254.177', port=8080, debug=True)
