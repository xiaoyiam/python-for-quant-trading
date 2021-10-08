
from jqdatasdk import *
auth('18263989896','KU&yu*1015') #ID是申请时所填写的手机号；Password为聚宽官网登录密码，新申请用户默认为手机号后6位

#获取平安银行按1分钟为周期以“2015-01-30 14:00:00”为基础前4个时间单位的数据
#df = get_price('000001.XSHE', end_date='2021-10-08',count=100, frequency='daily', fields=['open','close','high','low','volume','money'])
#print(df)
#print(len(df))


#获取所有A股的标的信息
stocks = list(get_all_securities(['stock']).index)
print(stocks)
print(len(stocks))

#df = get_price(stocks, end_date='2021-10-08',count=100, frequency='daily', fields=['open','close','high','low','volume','money'])
#print(df)
