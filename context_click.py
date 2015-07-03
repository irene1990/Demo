#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os,time
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
qqq = driver.find_element_by_xpath('//*[@id="1"]/h3/a')
#qqq = driver.find_element_by_xpath('//*[@id="1"]/div[1]/div[2]/p[1]/em[1]')
ActionChains(driver).context_click(qqq).perform()
#ActionChains(driver).double_click(qqq).perform()
time.sleep(3)
driver.close()