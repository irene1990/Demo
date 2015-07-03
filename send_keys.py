#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #需要引入keys包
import os,time
driver = webdriver.Firefox()
driver.get("http://www.tuicool.com/login")
time.sleep(3)
driver.maximize_window()
driver.find_element_by_id('xlEmail').clear()
driver.find_element_by_id('xlEmail').send_keys('fnngj')
#tab的定位相当于清除密码框的默认提示信息，等同上面的clear()
driver.find_element_by_id('xlEmail').send_keys(Keys.TAB)
time.sleep(3)
driver.find_element_by_id('xlPassword').send_keys('123456')
time.sleep(3)
#通过定位密码框，enter（回车）来代替登录按钮
driver.find_element_by_id('xlPassword').send_keys(Keys.ENTER)
time.sleep(3)
#也可以定位登录按钮，通过enter（回车）代替click()
driver.find_element_by_xpath('/html/body/div[3]/div/form/fieldset/div/div[4]/button').send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()
