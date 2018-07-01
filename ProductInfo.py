#encoding: utf-8

from common import db, get_info_from_request, to_response, get_current_param, set_current_param

class ProductInfo(db.Model):
	proid = db.Column(db.Integer, primary_key=True)
	proname = db.Column(db.String)
	category = db.Column(db.String)
	description = db.Column(db.String)

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
	def get_pro_from_request():
		origin_proid = '1000'
		keys = ['proname', 'category', 'description']
		name, cate, des = get_info_from_request(keys)
		last_pro = ProductInfo.query.order_by(ProductInfo.proid.desc()).first()
		last_proid = last_pro.proid
		if not last_proid:
			proid = str(int(origin_proid) + 1) 
		else:
			proid = str(int(last_proid) + 1)
		return ProductInfo(proid, name, cate, des)

	@staticmethod	
	def add_item(item):
		db.session.add(item)
		db.session.commit()
		new_item = ProductInfo.query.filter_by(proid=item.proid).first()
		if new_item:
			set_current_param('proname_list', new_item.proname)
			last_pro_total = get_current_param('pro_total')
			if not last_pro_total:
				pro_total = '1'
			else:
				pro_total = str(int(last_pro_total) + 1)
			set_current_param('pro_total', pro_total, True)
			return to_response('SUCCESS', new_item.to_dict(), pro_total)
		else:
			return to_response('FAILED', '获取最新数据失败')

	@staticmethod
	def delete_item(item):
		pro = ProductInfo.query.filter_by(proid=item.proid).first()
		db.session.delete(pro)
		db.session.commit()
		return to_response('SUCCESS', '')

	@staticmethod
	def update_item(item):
		product = ProductInfo.query.filter_by(proid=item.proid).first()
		#product.proname = 'hello'
		print item.proid
		db.session.commit()


	@staticmethod
	def get_item_by_filter(offset=0, size=10):
		offset_t = int(offset)
		size_t = int(size)
		res = ProductInfo.query.all()
		items = res[offset_t:offset_t+size_t]
		if res:
			return to_response('SUCCESS', [item.to_dict() for item in items])
		else:
			return to_response('FAILED', '暂无数据')
					
				  
	@staticmethod
	def get_product_list():
		total = 0
		product_list = []
		items = ProductInfo.query.all()
		for item in items:
			total += 1
			product_list.append(item.proname)
		return to_response('SUCCESS', {'total': total, 'prolist': product_list})
