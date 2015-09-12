#coding=utf-8
from selenium import webdriver
import time
class test_shenpi():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.82.32"
    def login(self,username,password):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("user_login").click()
        driver.find_element_by_id("job").click()
    def approval(self,approvalor):
            driver = self.driver
            rnum = driver.find_elements_by_xpath("//*[@id='pageinfo']/tbody/tr") #table row numbers
            i = 1
            while i < len(rnum)+1:
                path = "//*[@id='pageinfo']/tbody/tr["+str(i)+"]/td[6]/button"
                nums = len(driver.find_elements_by_xpath(path))  # numbers of button
                btext = driver.find_element_by_xpath(path+"["+str(1)+"]").text.encode('utf-8')  # button's text
                tmpapprovalor = driver.find_element_by_xpath("//*[@id='pageinfo']/tbody/tr["+str(i)+"]/td[5]").text.encode('utf-8')
                print btext			
                if tmpapprovalor == approvalor:
                    if btext == '通过':
                        print 'pass'
                        #driver.find_element_by_xpath(path+"["+str(j)+"]").click()
						try:
						    alter = switch_to_alert()
							alter.accept()
						except:
						    print 'next'
                        time.sleep(2)
                i +=1
                #driver.refresh()
                #time.sleep(5)
	def logout(self):
	    driver = self.driver()