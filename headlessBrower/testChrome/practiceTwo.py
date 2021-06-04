from selenium import webdriver
import json

driver = webdriver.Chrome()
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

ele = driver.find_element_by_id('forecastID')

# print(ele.text)

dls = ele.find_elements_by_tag_name('dl')

citys =[]
for city in dls:
  # print(city.text)
  name  = city.find_element_by_tag_name('dt').text
  ltemp = city.find_element_by_tag_name('b').text
  # ltemp = min([ int(one) for one in ltemp.split('/')])
  ltemp = int(ltemp.replace('℃',''))
  # print(ltemp)
  citys.append([name ,ltemp])

print(citys)

lowest = None
lowCity = []
for city in citys :
  curiName = city[0]
  ltemp = city[1]
  if lowest == None or  ltemp <lowest:
    lowest = ltemp
    lowCity = [curiName]
  elif lowest == ltemp:
    lowCity.append(curiName)
print('温度最低为 %s ℃,城市有%s' % (lowest,' '.join(lowCity)))
driver.quit()