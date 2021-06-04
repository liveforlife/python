from selenium import webdriver
import json

from bs4 import BeautifulSoup
driver = webdriver.Chrome()
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

ele = driver.find_element_by_id('forecastID')

resultStr = ele.get_attribute('innerHTML')


html_json = BeautifulSoup(resultStr,"html5lib")


dls = html_json.find_all('dl')

# print(dls)

citys=[]
for dl in dls:
  name =dl.find('dt').text.replace('\n','')
  lemp = dl.find('b').text
  lemp = int(lemp.replace('℃',''))
  citys.append([name,lemp])

lower = None
cityName = []
for city in citys:
  currName = city[0]
  lemp = city[1]
  if lower ==None or lemp < lower:
    lower = lemp
    cityName = [currName]
  elif lower == lemp :
    cityName.append(currName)

print('最冷的温度 %s ℃ 最冷的城市：%s' % (lower,' '.join(cityName)))
driver.quit()