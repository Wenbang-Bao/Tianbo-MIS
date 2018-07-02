#encoding: utf-8

from common import db, get_info_from_request, to_response, get_current_param, set_current_param

class ProductInfo(db.Model):
	proid = db.Column(db.Integer, primary_key=True)
	proname = db.Column(db.String)
	category = db.Column(db.String)
	description = db.Column(db.String)
	prototal = 0
	proname_list = []

	def __init__(self, pid, name, cate, des):
		self.proid = pid
		self.proname = name
		self.category = cate
		self.description = des


	def to_dict(self):
		return {
				'proid': self.proid,
				'proname': self.proname,
				'category': self.category,
				'description': self.description
				}

	@staticmethod
	def setup_param():
		ProductInfo.prototal = 0
		items = ProductInfo.query.all()
		for item in items:
			ProductInfo.prototal += 1
			ProductInfo.proname_list.append(item.proname)

	@staticmethod	
	def get_pro_from_request():
		origin_proid = 1000
		keys = ['proname', 'category', 'description']
		name, cate, des = get_info_from_request(keys)
		last_pro = ProductInfo.query.order_by(ProductInfo.proid.desc()).first()
		if not last_pro:
			proid = origin_proid + 1
		else:
			proid = last_pro.proid + 1
		return ProductInfo(proid, name, cate, des)

	@staticmethod	
	def add_item():
		origin_proid = 1000
		keys = ['proname', 'category', 'description']
		name, cate, des = get_info_from_request(keys)
		last_pro = ProductInfo.query.order_by(ProductInfo.proid.desc()).first()
		if not last_pro:
			proid = origin_proid + 1
		else:
			proid = last_pro.proid + 1
		item = ProductInfo(proid, name, cate, des) 
		db.session.add(item)
		db.session.commit()
		new_item = ProductInfo.query.filter_by(proid=int(item.proid)).first()
		if new_item:
			ProductInfo.setup_param()
			return to_response('SUCCESS', new_item.to_dict(), {'prototal': ProductInfo.prototal})
		else:
			return to_response('FAILED', '获取最新数据失败')

	@staticmethod
	def delete_item():
		keys = ['proid', 'proname', 'category', 'description']
		proid, name, cate, des = get_info_from_request(keys)
		pro = ProductInfo.query.filter_by(proid=int(proid)).first()
		db.session.delete(pro)
		db.session.commit()
		pro = ProductInfo.query.filter_by(proid=int(proid)).first()
		if not pro:
			ProductInfo.setup_param()
			return to_response('SUCCESS', '', {'prototal': ProductInfo.prototal})
		else:
			return to_response('FAILED', '')

	@staticmethod
	def update_item():
		keys = ['proid', 'proname', 'category', 'description']
		proid, name, cate, des = get_info_from_request(keys)
		ProductInfo.query.filter_by(proid=int(proid)).update({'proname':name, 'category': cate, 'description': des})
		db.session.commit()
		new_pro = ProductInfo.query.filter_by(proid=int(proid)).first()
		if new_pro:	
			return to_response('SUCCESS', '')
		else:
			return to_response('FAILED', '')
		


	@staticmethod
	def get_item_by_filter(offset=0, size=10):
		offset_t = int(offset)
		size_t = int(size)
		if ProductInfo.prototal == 0:
			ProductInfo.setup_param()
		res = ProductInfo.query.all()
		items = res[offset_t:offset_t+size_t]
		if res:
			return to_response('SUCCESS', [item.to_dict() for item in items], {'prototal': ProductInfo.prototal})
		else:
			return to_response('FAILED', '暂无数据')
						
