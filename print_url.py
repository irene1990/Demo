#coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
url='http://www.baidu.com'
print "now access %s" %(url)
browser.get(url)
time.sleep(2)
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()
