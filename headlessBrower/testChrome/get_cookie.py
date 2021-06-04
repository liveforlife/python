from selenium import webdriver
import json
import time

url='https://www.jianshu.com/sign_in'

driver = webdriver.Chrome()

driver.get(url)
time.sleep(6)
el = driver.find_element_by_xpath('//input[@type="text"]')
el.send_keys('962383345@qq.com')

el = driver.find_element_by_xpath('//input[@type="password"]')
el.send_keys('123456')

driver.find_element_by_id('sign-in-form-submit-btn').click()

time.sleep(20)

diccookie = driver.get_cookies()
print(diccookie)
fw = open('cookie.txt','w')
json.dump(diccookie,fw)
fw.close()
time.sleep(2)

driver.get_screenshot_as_file('img/ogin.png')

# driver.quit()
