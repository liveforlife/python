# 定位 UI 元素 (WebElements)

find_element_by_id
find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector

# 获取元素数据

ele.get_attribute('href')
ele.text
ele.inner
ele.get_attribute('outerHTML')
ele.get_attribute('innerHTML')

# 导入 ActionChains 类

from selenium.webdriver import ActionChains

# 鼠标移动到 ac 位置

ac = driver.find_element_by_xpath('element')
ActionChains(driver).move_to_element(ac).perform()

# 在 ac 位置单击

ac = driver.find_element_by_xpath("elementA")
ActionChains(driver).move_to_element(ac).click(ac).perform()

# 在 ac 位置双击

ac = driver.find_element_by_xpath("elementB")
ActionChains(driver).move_to_element(ac).double_click(ac).perform()

# 在 ac 位置右击

ac = driver.find_element_by_xpath("elementC")
ActionChains(driver).move_to_element(ac).context_click(ac).perform()

# 在 ac 位置左键单击 hold 住

ac = driver.find_element_by_xpath('elementF')
ActionChains(driver).move_to_element(ac).click_and_hold(ac).perform()

# 将 ac1 拖拽到 ac2 位置

ac1 = driver.find_element_by_xpath('elementD')
ac2 = driver.find_element_by_xpath('elementE')
ActionChains(driver).drag_and_drop(ac1, ac2).perform()

# 导入 Select 类

from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_name('status')
select.select_by_visible_text("审核不通过")

# 页面切换

driver.switch_to.window("window name")

# 操作页面的前进和后退

driver.forward()  
driver.back()

# 页面等待

## 隐式等待

driver.implicitly_wait(10)

## 显示等待

try: # 页面一直循环，直到 id="myElement" 出现
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myElement")))
finally:
driver.quit()
