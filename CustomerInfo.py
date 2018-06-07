#encoding: utf-8

from common import db

class CustomerInfo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	contacter1 = db.Column(db.String)
	position1 = db.Column(db.String)
	email1 = db.Column(db.String)
	telephone1 = db.Column(db.String)
	cellphone1 = db.Column(db.String)
	contacter2 = db.Column(db.String)
	position2 = db.Column(db.String)
	email2 = db.Column(db.String)
	telephone2 = db.Column(db.String)
	cellphone2 = db.Column(db.String)
	classes = db.Column(db.String)
	level = db.Column(db.String)
	credit = db.Column(db.String)
	postcode = db.Column(db.String)
	address = db.Column(db.String)
	comment = db.Column(db.String)
	
	



	def __init__(self, name, 
				 contacter1, position1, email1, telephone1, cellphone1,\
				 contacter2, position2, email2, telephone2, cellphone2,\
				 classes, level, credit, postcode, address, comment):
		self.name = name
		self.contacter1 = contacter1
		self.position1 = position1
		self.email = email1
		self.telephone1 = telephone1
		self.cellphone1 = cellphone1
		self.contacter2 = contacter2
		self.position2 = position2
		self.emai2 = email2
		self.telephone2 = telephone2
		self.cellphone2 = cellphone2
		self.classes = classes
		self.level = level
		self.credit = credit
		self.postcode = postcode
		self.address = address
		self.comment = comment

	def to_dict(self):
		return {
				'id': self.id,
				'name': self.name,
				'contacter1': self.contacter1,
				'position1': self.position1,
				'email1': self.email1,
				'telephone1': self.telephone1,
				'cellphone1': self.cellphone1,
				'contacter2': self.contacter2,
				'position2': self.position2,
				'email2': self.email2,
				'telephone2': self.telephone2,
				'cellphone2': self.cellphone2,
				'classes': self.classes,
				'level': self.level,
				'credit': self.credit,
				'postcode': self.postcode,
				'address': self.address,
				'comment': self.comment
				}	
