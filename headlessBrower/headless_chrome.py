from time import sleep

from selenium.webdriver import Chrome
from selenium import webdriver
import json

options = webdriver.ChromeOptions()
options.add_argument("--auto-open-devtools-for-tabs")
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = Chrome(chrome_options=options)
test_url = 'http://192.168.0.81:9018/#/processEight2020113001?channelCode=7VCs'
formal_url = 'https://topic.ttshengbei.com/#/processEight2020113001?channelCode=7VCs'
driver.get(formal_url)

# driver.execute_script('Object.defineProperty(navigator,"webdriver",{get:() => false,});')
ele = driver.find_element_by_xpath("//input[@placeholder ='请输入手机号']")

ele.send_keys('13541781424')

driver.find_element_by_xpath("//div[@class='header-form-button']//img").click()
# find_element_by_id('')
# 获取网站cookie
diccookie = driver.get_cookies()
fw= open('cookie.txt','w')
json.dump(diccookie,fw)
fw.close()
try:
  driver.get_element_by_id('test')
except NoSuchElementException:
  print('NoSuchElementException')

# 截图
driver.get_screenshot_as_file('img/chrome.png')

sleep(3)