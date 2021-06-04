# 广点通
import requests,json,time
import hashlib

#获取通行证 
#   https://adnet.qq.com/user/getloginstatus
#   cookie
#   set-cookie: PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InVpblNlc3Npb25LZXkiOiI4MDUwNzAyMDkwMjQiLCJpc1N1cGVyVWluS2V5IjoiMCIsIm9wZW5JZFNlc3Npb25LZXkiOiJCQkJFNUYxQzQxNDAzNkFCMjE3QTI5NTIyRDkwODJERCJ9LCJuYmYiOjE2MDAyMjY4MDYsImlhdCI6MTYwMDIyNjgwNn0.rO_rH39qV0M11ll_DIS_4FfzLLjoYGK0pUpHzorF4sI; SameSite=Lax; Path=/; HTTPOnly
# set-cookie: adnet_uin=805070209024; Max-Age=143593; Expires=Thu, 17 Sep 2020 19:19:59 GMT; Path=/; Domain=qq.com
# set-cookie: adnet_uname=%E6%88%90%E9%83%BD%E4%BC%98%E9%80%89%E4%BB%93%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8; Max-Age=143593; Expires=Thu, 17 Sep 2020 19:19:59 GMT; Path=/; Domain=qq.com
# set-cookie: adnet_openId=BBBE5F1C414036AB217A29522D9082DD; Max-Age=143593; Expires=Thu, 17 Sep 2020 19:19:59 GMT; Path=/; Domain=qq.com; HTTPOnly
# set-cookie: adnet_li=$1$b4Bf66T8$adC9xQtNHUUHfZ5AYsE6w.; Max-Age=143593; Expires=Thu, 17 Sep 2020 19:19:59 GMT; Path=/; Domain=qq.com

#获取数据

# getDate_url = 'https://adnet.qq.com/eros/report/revenue'
# getDate_data = {}
# d = requests.get(getDate_url, params=getDate_data,headers={'cookie':'ptui_loginuin=597748089@qq.com; adnet_sso=TGT-09936-C7ONfRisd9D_XpOF0oFzS7ThQjYG4ozKIzZuK586F8511RPoGZb7fmvZGKVc3RSX;'})
# # print(d.text)
# print(d.json()['data']['revenue_data']['yesterday_revenue'])

s='Aa15884451330'
m= hashlib.md5(s.encode())
print(m.hexdigest())
