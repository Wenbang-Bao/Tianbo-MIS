#encoding: utf-8
from flask import Flask, request
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
import xlwt

app = Flask(__name__, static_folder = './dist/static', template_folder = './dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/TB_MIS_DEV'
db = SQLAlchemy(app)

current_param_file = './.current_param.config'
current_param_dict = {
						'pro_total': '',
						'proname_list': [],
						'cust_total': '',
						'custname_list': []
					 }

def get_info_from_request(keys=[]):
	values = []
	for key in keys:
		values.append(request.form.get('message['+key+']'))
	return values


def generate_execel(header=[], infos=[]):
	workbook = xlwt.Workbook(encoding = 'utf-8')
	worksheet = workbook.add_sheet('My WorkSheet')
	border = xlwt.Borders()
	border.left = 1
	border.right = 1
	border.top = 1
	border.bottom = 1
	style = xlwt.XFStyle()
	style.borders = border
	header_len = len(header)
	for i,unit in enumerate(header):
		worksheet.write(0,i, label = unit, style=style)
	for x,item in enumerate(infos):
		for y,unit in enumerate(item):
			worksheet.write(x+1, y, label=unit, style=style)
	workbook.save('xlwt_excel.xls')

def to_response(code='FAILED', msg='', cfg=''):
		return {'answercode': code, 'answermsg': msg, 'answercfg': cfg}


def get_current_param(key):
	res = current_param_dict.get(key)
	if res:
		return res
	else:
		load_current_param(current_param_file)
		return current_param_dict.get(key)

def set_current_param(key, value, is_store=False):
	global current_param_dict
	if current_param_dict.has_key(key):
		if type(current_param_dict[key]).__name__ == 'list':
			current_param_dict[key].append(value)
		else:
			current_param_dict[key] = value
	else:
		return False
	if is_store:
		store_current_param(current_param_file)
	
def store_current_param(filename):
	with open(filename, 'w') as f:
		for item in current_param_dict.items():
			if type(item[1]).__name__ == 'list':
				f.write('='.join([item[0], '|'.join(item[1]).encode('utf8')])+'\n')
			else:
				f.write('='.join(item)+'\n')

def load_current_param(filename):
	global current_param_dict
	with open(filename, 'r+') as f:
		for line in f:
			if not line:
				key = line.split('=')[0]
				value = line.split('=')[1]	
				if current_param_dict.has_key(key):
					current_param_dict[key] = value
			
if __name__ == '__main__':
	set_current_param('proid', '20180070101')
	set_current_param('proname_list', '镀铝袋')
	set_current_param('proname_list', '枸杞蜜')
	set_current_param('pro_total', '1', True)
	for key, value in current_param_dict.items():
		print key, value
