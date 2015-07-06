#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os,time
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('level_locate.html')
driver.get(file_path)
#点击Link1链接（弹出下拉列表）
driver.find_element_by_link_text('Link1').click()
#找到id为dropdown1的父元素
WebDriverWait(driver,10).until(lambda the_driver:the_driver.find_element_by_id('dropdown1')is_displayed())
menu = driver.find_element_by_id('dropdown1').find_element_by_link_text('Action')
#鼠标定位到子元素上
webdriver.ActionChains(driver).move_to_element(menu).perform()
time.sleep(2)
driver.quit()