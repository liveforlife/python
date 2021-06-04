import requests,json,time
session = requests.session()
# 推啊
# 获取 通行码
url='https://ssp.tuia.cn/account/login'
data={'email':'lcs@yoc.tech','password':'luzhen821','remember':False}
data_json = json.dumps(data) 
session.post(url, data=data_json,headers={'Content-Type':'application/json'})
html_set_cookie = requests.utils.dict_from_cookiejar(session.cookies)

## 获取 昨日收入,当数据无值的时候,还未到出数据的时间
getDate_url = 'https://ssp.tuia.cn/slotLineStatistics/getMediaExpectedIncomeData'
current_date = time.strftime('%Y-%m-%d')
getDate_data = {'startDate':current_date,'endDate':current_date}
d = requests.get(getDate_url, params=getDate_data,headers={'Cookie':'ssp_tiket='+html_set_cookie.get('ssp_tiket')})
print(d.json()['data']['yesterdayExpectedIncome'])

