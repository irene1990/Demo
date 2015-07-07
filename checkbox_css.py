#coding = utf-8
from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path ='file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)
#选择页面上的所有checkbox并全部勾上
checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
time.sleep(2)
#打印当前页面有多少个checkbox
print (len(driver.find_elements_by_css_selector('input[type=checkbox]')))
time.sleep(2)
driver.quit()
