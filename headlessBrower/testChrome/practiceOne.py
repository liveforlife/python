from selenium import webdriver
import json

driver = webdriver.Chrome()
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

ele = driver.find_element_by_id('forecastID')
# print(ele.text)

cityWeather = ele.text.split('℃\n')


lowest = None
lowestList = []
for one in cityWeather:
  one = one.replace('℃','')
  print(one)
  parts = one.split('\n')
  print(parts)
  curcity = parts[0]
  lowweather = min([int(one) for one in parts[1].split('/')])
  if lowest == None or lowweather<lowest:
    lowest = lowweather
    lowestList = [curcity]
  elif lowest == lowweather:
    lowestList.append(curcity)


print('温度最低为%s℃, 城市有%s' % (lowest, ' '.join(lowestList)))

driver.quit()