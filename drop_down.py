#coding=utf-8
from selenium import webdriver
import os,time
driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('drop_down.html')
driver.get(file_path)
#先定位到下拉框
m = driver.find_element_by_id('ShippingMethod')
#在点击下拉框下的选项
m.find_element_by_xpath("//option[@value='10.69']").click()
time.sleep(3)
driver.quit()