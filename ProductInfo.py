#encoding: utf-8

from common import db, get_info_from_request

class ProductInfo(db.Model):
	id = db.Column(db.String, primary_key=True)
	name = db.Column(db.String)
	category = db.Column(db.String)
	description = db.Column(db.String)



	def __init__(self, id, name, category, description):
		self.id = id
		self.name = name
		self.category = category
		self.description = description


	def to_dict(self):
		return {
				'id': self.id,
				'name': self.name,
				'category': self.category,
				'description': self.description
				}
	
	def get_pro_from_request():
		keys = ['id', 'name', 'category', 'description']
		id, name, category, description = get_info_from_request(keys)
		return ProductInfo(id, name, category, description)
