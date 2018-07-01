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
	

	def __init__(self, custname, 
				 contacter, position, telephone, cellphone,\
				 postcode, address, comment):
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
	def get_cust_from_request():
		keys = ['custname', 
				'contacter', 'position', 'telephone', 'cellphone',
				'postcode', 'address', 'comment']
		custname, contacter, position, telephone, cellphone, postcode, address, comment= get_info_from_request(keys)
		return CustomerInfo(custname, contacter, position, telephone, cellphone, postcode, address, comment)

	@staticmethod	
	def add_item(item):
		db.session.add(item)
		db.session.commit()

	@staticmethod
	def delete_item(item):
		cust = CustomerInfo.query.filter_by(custname=item.custname).first()
		db.session.delete(cust)
		db.session.commit()
		return to_response('SUCCESS', '')

	def get_newest_item(self):
		item = ''
		item = CustomerInfo.query.filter_by(custname=self.custname).first()
		if item:
			return to_response('SUCCESS', item.to_dict())
		else: 
			return to_response('FAILED', '')

	@staticmethod
	def get_item_by_filter(offset=0, size=10):
		offset_t = int(offset)
		size_t = int(size)
		res = CustomerInfo.query.all()
		items = res[offset_t:offset_t+size_t]
		if res:
			return to_response('SUCCESS', [item.to_dict() for item in items])
		else:
			return to_response('FAILED', '暂无数据')

	# should optimize there code
	@staticmethod
	def get_cust_list():
		total = 0
		cust_list = []
		items = CustomerInfo.query.all()
		for item in items:
			total += 1
			cust_list.append(item.custname)
		return to_response('SUCCESS', {'total': total, 'custlist': cust_list})



