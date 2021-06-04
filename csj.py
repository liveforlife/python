# 穿山甲
import requests,json,time
# 登录
# https://partner.oceanengine.com/passport/web/user/login/?account_sdk_source=web
# 发送  cookie: s_v_web_id=kf4t16mp_XppkjzDn_yUi6_4vBO_AEo5_YkhToQIfcV2L; passport_csrf_token=392b70d06b29703439268a50431fe075
# 参数 ：
# account: 72727f34457c6a662b7160666d
# password: 7f7d343736313033
# captcha: 
# fp: kf4t16mp_XppkjzDn_yUi6_4vBO_AEo5_YkhToQIfcV2L
# aid: 1407
# language: zh
# mix_mode: 1
# 获得 set-cookie: sessionid=127e566732950eb51ea0dd5df018b1f9; Path=/; Domain=oceanengine.com; Max-Age=5184000; HttpOnly 
# passport_csrf_token s_v_web_id


# 数据接口
# cookie  x-csrftoken: ImRlNWZmN2NhMWMyMjEwNjUwNGFmZGUxOWQ2ZGMzMDNiZDE1NmU5ZDQi.X2F-aw.XGEyyOUlZO8Ae-jXPfFssIIgjIs

# Request URL: https://partner.oceanengine.com/union/media/api/overview   ['data']['YesterdayIncome']

getDate_url = 'https://partner.oceanengine.com/union/media/api/overview'
getDate_data = {}
d = requests.get(getDate_url, params=getDate_data,headers={'cookie':'sessionid=127e566732950eb51ea0dd5df018b1f9'})
# print(d.text)
print(d.json()['data']['YesterdayIncome'])