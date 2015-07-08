# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path ='file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)
#选择页面上的所有input，然后从中过滤出所有的checkbox并勾选之
inputs = driver.find_elements_by_tag_name('input')
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
time.sleep(2)
driver.quit()
