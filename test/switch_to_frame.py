#coding=utf-8
from selenium import webdriver
import time,os
browser = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('frame.html')
browser.get(file_path)
browser.implicitly_wait(30)
#先找到ifrome1(id = f1)
browser.switch_to_frame("f1")
#再找到其下面的ifrome2(id = 2)
browser.switch_to_frame("f2")
#下面就可以正常的操作元素了
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()
#没介绍如何推出frame
