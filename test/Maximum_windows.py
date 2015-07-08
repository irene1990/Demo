#coding=utf-8
from selenium import webdriver
import time
browser=webdriver.Firefox()
browser.get('http://www.baidu.com')
print '浏览器最大化'
browser.maximize_window()
time.sleep(2)
browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').click()
time.sleep(3)
browser.quit()
