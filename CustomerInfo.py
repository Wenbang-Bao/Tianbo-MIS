#encoding: utf-8

from common import db, get_info_from_request, to_response

class CustomerInfo(db.Model):
	custid = db.Column(db.Integer, primary_key=True)
	custname = db.Column(db.String)
	contacter = db.Column(db.String)
	position = db.Column(db.String)
	telephone = db.Column(db.String)
	cellphone = db.Column(db.String)
	postcode = db.Column(db.String)
	address = db.Column(db.String)
	comment = db.Column(db.String)	
	custtotal = 0
	custname_list = []	

	def __init__(self, custid, custname, 
				 contacter, position, telephone, cellphone,\
				 postcode, address, comment):
		self.custid = custid
		self.custname = custname
		self.contacter = contacter
		self.position = position
		self.telephone = telephone
		self.cellphone = cellphone
		self.postcode = postcode
		self.address = address
		self.comment = comment

	def to_dict(self):
		return {
				'custname': self.custname,
				'contacter': self.contacter,
				'position': self.position,
				'telephone': self.telephone,
				'cellphone': self.cellphone,
				'postcode': self.postcode,
				'address': self.address,
				'comment': self.comment
				}	

	@staticmethod
	def setup_param():
		CustomerInfo.custtotal = 0
		items = CustomerInfo.query.all()
		for item in items:	
			CustomerInfo.custtotal += 1
			CustomerInfo.custname_list.append(item.custname)

	@staticmethod	
	def get_cust_from_request():
		keys = ['custname', 
				'contacter', 'position', 'telephone', 'cellphone',
				'postcode', 'address', 'comment']
		custname, contacter, position, telephone, cellphone, postcode, address, comment= get_info_from_request(keys)
		return CustomerInfo(custname, contacter, position, telephone, cellphone, postcode, address, comment)

	@staticmethod	
	def add_item():
		origin_custid = 2000
		keys = ['custname', 
				'contacter', 'position', 'telephone', 'cellphone',
				'postcode', 'address', 'comment']
		custname, contacter, position, telephone, cellphone, postcode, address, comment= get_info_from_request(keys)
		last_cust = CustomerInfo.query.order_by(CustomerInfo.custid.desc()).first()
		if not last_cust:
			custid = origin_custid + 1
		else:
			custid = last_cust.custid + 1
		item = CustomerInfo(custid, custname, contacter, position, telephone, cellphone, postcode, address, comment)
		db.session.add(item)
		db.session.commit()
		new_item = CustomerInfo.query.filter_by(custid=int(item.custid)).first()
		if new_item:
			CustomerInfo.setup_param()	
			return to_response('SUCCESS', item.to_dict(), {'custtotal': CustomerInfo.custtotal})
		else:
			return to_response('FAILED', '')


	@staticmethod
	def delete_item():
		keys = ['custid', 'custname', 
				'contacter', 'position', 'telephone', 'cellphone',
				'postcode', 'address', 'comment']

		custid, custname, contacter, position, telephone, cellphone, postcode, address, comment= get_info_from_request(keys)
		print custid
		cust = CustomerInfo.query.filter_by(custid=int(custid)).first()
		db.session.delete(cust)
		db.session.commit()
		print custid
		new_cust = CustomerInfo.query.filter_by(custid=int(custid)).first()
		if not new_cust:
			return to_response('SUCCESS', '')
		else:
			return to_response('FAILED', '')
			

	@staticmethod
	def get_item_by_filter(offset=0, size=10):
		offset_t = int(offset)
		size_t = int(size)
		if CustomerInfo.custtotal == 0:
			CustomerInfo.setup_param()
		res = CustomerInfo.query.all()
		items = res[offset_t:offset_t+size_t]
		if res:
			return to_response('SUCCESS', [item.to_dict() for item in items], {'custtotal': CustomerInfo.custtotal})
		else:
			return to_response('FAILED', '暂无数据')
