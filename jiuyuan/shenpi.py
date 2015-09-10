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
        driver.find_element_by_id("username").send_keys("safeadmin")
        driver.find_element_by_id("password").send_keys("1234")
        driver.find_element_by_id("user_login").click()
        driver.find_element_by_id("job").click()
        now_handle1 = driver.current_window_handle
        print now_handle1
        kk = driver.find_elements_by_xpath("//*[@id='pageinfo']/tbody/tr")
        print len(kk)
        i = 1
        while i < len(kk):
            path = "//*[@id='pageinfo']/tbody/tr["+str(i)+"]/td[6]/button"
            nums = len(driver.find_elements_by_xpath(path))
            status = driver.find_element_by_xpath(path+"["+str(1)+"]").text
            print status
            i += 1
        now_handle2 = driver.current_window_handle
        print now_handle2
        driver.refresh()
        now_handle3 = driver.current_window_handle
        print now_handle3
        i = 1
        while i < len(kk):
            path = "//*[@id='pageinfo']/tbody/tr["+str(i)+"]/td[6]/button"
            nums = len(driver.find_elements_by_xpath(path))
            status = driver.find_element_by_xpath(path+"["+str(1)+"]").text
            print status
            i += 1
if __name__ == "__main__":
    unittest.main()