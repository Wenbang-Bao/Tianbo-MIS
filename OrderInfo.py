#encoding: utf-8

from common import db, get_info_from_request


class OrderInfo(db.Model):
	orderid = db.Column(db.String, primary_key=True)
	starttime = db.Column(db.String)
	endtime = db.Column(db.String)
	proname = db.Column(db.String)
	prosize = db.Column(db.String)
	price = db.Column(db.String)
	amount = db.Column(db.String)
	prosum = db.Column(db.String)
	othercose = db.Column(db.String)
	cosetype = db.Column(db.String)
	ordersum = db.Column(db.String)
	waittime = db.Column(db.String)
	waitmoney = db.Column(db.String)
	orderstatus = db.Column(db.String)
	postlist = db.Column(db.String)
	billlist = db.Column(db.String)
	comment = db.Column(db.String)
	orderdate = db.Column(db.String)
	custname = db.Column(db.String)

	def __init__(self, orderid, starttime, endtime,\
				 proname, prosize, price, amount, prosum,\
				 othercose, cosetype, ordersum, waittime,\
				 waitmoney, orderstatus, postlist, billlist,\
				 comment, orderdate, custname):
		self.orderid = orderid
		self.starttime = starttime
		self.endtime = endtime
		self.proname = proname
		self.prosize = prosize
		self.price = price
		self.amount = amount
		self.prosum = prosum
		self.othercose = othercose
		self.cosetype = cosetype
		self.ordersum = ordersum
		self.waittime = waittime
		self.waitmoney = waitmoney
		self.orderstatus = orderstatus
		self.postlist = postlist
		self.billlist = billlist
		self.comment = comment
		self.orderdate = orderdate
		self.custname = custname

	@staticmethod
	def get_order_from_request():
		keys = ['custname', 'starttime', 'endtime', 'proname', 'prosize', 'price',
			   'amount', 'prosum', 'othercose', 'cosetype', 'ordersum', 'waittime',
			   'waitmoney', 'orderstatus', 'postlist', 'billlist', 'comment', 'orderdate']
		custname, starttime, endtime, proname, prosize, price, amount, prosum, othercose, cosetype, ordersum, waittime, waitmoney, orderstatus, postlist, billlist,comment, orderdate = get_info_from_request(keys)
		orderid = '2018053003'	
		starttime = '2018-10-11'
		endtime = '2018-10-11'
		orderdate = '2018-10-11'
		return OrderInfo(orderid, starttime, endtime, proname, prosize, price, amount, prosum,othercose, cosetype, ordersum, waittime,waitmoney, orderstatus, postlist, billlist,comment, orderdate, custname)

	@staticmethod 
	def add_item(item):
		db.session.add(item)
		db.session.commit()
