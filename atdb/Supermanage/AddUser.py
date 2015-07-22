#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.82.33/dbackup"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get("http://192.168.82.33/dbackup/index.php")
        driver.find_element_by_id("UserNameID").send_keys("admin")
        driver.find_element_by_id("PWID").send_keys("admin")
        driver.find_element_by_id("LoginButton").click()
        time.sleep(2)
        user = driver.find_element_by_xpath('//*[@id="navigate"]/ul[1]/li[3]/a')
        ActionChains(driver).move_to_element(user).perform()
        driver.find_element_by_xpath('//*[@id="navigate"]/ul[1]/li[3]/ul/li[1]/a').click()
        time.sleep(2)
        driver.find_element_by_id("account-add").click()
        driver.find_element_by_id("txt_username").send_keys("dingjia")
        driver.find_element_by_id("txt_password").send_keys("dingjia123")
        driver.find_element_by_id("txt_re_password").send_keys("dingjia123")
        driver.find_element_by_id("txt_email").send_keys("dingjia1@scutech.com")
        driver.find_element_by_id("txt_phone").send_keys("1234567890")
        driver.find_element_by_id("cb_role_admin").click()
        driver.find_element_by_id("cb_role_monitor").click()
        driver.find_element_by_id("btn_submit_user").click()
        time.sleep(10)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

