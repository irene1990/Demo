#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest,time,re
class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.82.32"
        self.verificationErrors = []
        self.accept_next_alert = True
    def test_untitled(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("username").send_keys("g2safe")
        driver.find_element_by_id("password").send_keys("Dingjia123!")
        driver.find_element_by_id("user_login").click()
        driver.find_element_by_id("job").click()
        kk = driver.find_elements_by_xpath("//*[@id='pageinfo']/tbody/tr")
        print len(kk)
        while True:
            i = 1
            while i < len(kk)+1:
                path = "//*[@id='pageinfo']/tbody/tr["+str(i)+"]/td[6]/button"
                nums = len(driver.find_elements_by_xpath(path))
                status = driver.find_element_by_xpath(path+"["+str(1)+"]").text.encode('utf-8')
                #print status
                if status == '通过':
                    print 'pass'
                    driver.find_element_by_xpath(path+"["+str(1)+"]").click()
                    time.sleep(2)
                i += 1
            driver.refresh()
            time.sleep(5)
        #i = 1
        #while i < len(kk):
        #    path = "//*[@id='pageinfo']/tbody/tr["+str(i)+"]/td[6]/button"
        #    nums = len(driver.find_elements_by_xpath(path))
        #    status = driver.find_element_by_xpath(path+"["+str(1)+"]").text
        #    print status
        #    i += 1
if __name__ == "__main__":
    unittest.main()