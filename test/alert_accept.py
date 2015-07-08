#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os,time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
#展开设置下拉选项（定位悬停元素）
setting = driver.find_element_by_link_text("设置")
#对定位到的元素执行悬停操作
ActionChains(driver).move_to_element(setting).perform()
time.sleep(3)
#点击“搜索设置”，貌似在div中的元素要逐层定位。
driver.find_element_by_xpath('//*[@id="wrapper"]/div[5]/a[1]').click()
time.sleep(2)
m = driver.find_element_by_id("nr")
m.find_element_by_xpath("//option[@value='50']").click()
driver.find_element_by_xpath("//*[@id='gxszButton']/a[1]").click()
time.sleep(2)
# 确认保存设置
driver.switch_to_alert().accept()
time.sleep(3)
#返回百度首页搜索，验证设置结果
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(10)
driver.quit()
