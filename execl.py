#encoding: utf-8

import xlwt

header = ['客户名称', '联系人姓名', '联系人职位', '联系电话', '客户类别', '客户级别', '信用级别']
db = [['百度', '张三', '经理', '12345678', '正式客户', 'VIP客户', '5'],
	  ['腾讯', '李四', '经理', '12345678', '正式客户', '大客户', '4'],
	  ['青海康普', '王五', '经理', '12345678', '正式客户', '大客户', '3'],]


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


generate_execel(header, db)
