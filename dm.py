import requests,json
url='https://www.doumob.com/end/app/login'
data={'email':'zz@yoc.tech','password':'luzhen821'}
data_json = json.dumps(data) 
r = requests.post(url, data)
print(r.json())
print(r.json()['token'])

token = r.json()['token']
getDate_url = 'https://www.doumob.com/end/app/reduceMoney'
getDate_data = {'token':token}
d = requests.get(getDate_url, params=getDate_data)
print(d.json()['map']['reduceMoney'])
