#encoding: utf-8

from common import db, get_info_from_request

class ProductInfo(db.Model):
	proid = db.Column(db.String, primary_key=True)
	proname = db.Column(db.String)
	category = db.Column(db.String)
	description = db.Column(db.String)



	def __init__(self, proid, name, category, description):
		self.proid = proid
		self.proname = name
		self.category = category
		self.description = description


	def to_dict(self):
		return {
				'id': self.proid,
				'name': self.proname,
				'category': self.category,
				'description': self.description
				}

	@staticmethod	
	def get_pro_from_request():
		keys = ['id', 'name', 'category', 'description']
		proid, proname, category, description = get_info_from_request(keys)
		return ProductInfo(proid, proname, category, description)

	@staticmethod	
	def add_item(item):
		db.session.add(item)
		db.session.commit()

	@staticmethod	
	def get_newest_item():
		item = ProductInfo.query.filter_by(proid=self.proid).first()
		return item.to_dict()

	@staticmethod
	def get_item_by_filter(offset=1, size=10):
		items = ProductInfo.query.filter('seq>:seq').params(seq=offset).limit(size)
		if items:
			print 'no....\n'
			print items
			return [item.to_dict() for item in items]
		else:
			return {'result': 'failed',
					'message': '无数据!'
				   }
