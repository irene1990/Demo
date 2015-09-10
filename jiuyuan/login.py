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
        driver.find_element_by_id("username").send_keys("sysadmin")
        driver.find_element_by_id("password").send_keys("1234")
        driver.find_element_by_id("user_login").click()
        now_handle = driver.current_window_handle
        print "now_handle is ========="+now_handle
        driver.find_element_by_id("create").click()
        time.sleep(20)
        #now_handle1 = driver.current_window_handle
        #print "now_handle1 is ========="+now_handle1
        all_handles = driver.window_handles
        print len(all_handles)
        for handle in all_handles:
            if handle != '':
                print "all_handles is =========="+handle
        driver.find_element_by_id("name").send_keys("dingjia3")
        driver.find_element_by_id("identitycn").send_keys("111111111111111111")
        driver.find_element_by_id("passwd").send_keys("@Dingjia123")
        driver.find_element_by_id("passwdcommit").send_keys("@Dingjia123")
        driver.find_element_by_id("telphone").send_keys("13822548786")
        driver.find_element_by_id("email").send_keys("wangshuixian@scutech.com")
        driver.find_element_by_id("singlecheck").click()
        driver.find_element_by_id("bt_role").click()
        driver.find_element_by_xpath("//*[@id='roleselect']/li[3]/a").click()
        driver.find_element_by_id("singlecheck").click()
		
if __name__ == "__main__":
    unittest.main()