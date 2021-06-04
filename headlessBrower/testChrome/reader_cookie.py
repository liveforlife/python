from selenium import webdriver
import json
import time

url='https://www.jianshu.com/sign_in'

driver = webdriver.Chrome()

driver.get(url)

fr = open('cookie.txt','r')
cookieList = json.load(fr)
fr.close()
for cookie in cookieList:
  driver.add_cookie(cookie)

time.sleep(10)

driver.quit()
