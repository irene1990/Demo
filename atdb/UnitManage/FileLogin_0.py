from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.82.34/dbackup"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get("http://192.168.82.34/dbackup/index.php")
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_id("UserNameID").clear()
        driver.find_element_by_id("UserNameID").send_keys("dingjia")
        driver.find_element_by_id("PWID").clear()
        driver.find_element_by_id("PWID").send_keys("dingjia123")
        driver.find_element_by_id("LoginButton").click()
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_css_selector("div.tree_expand").click()
        driver.find_element_by_css_selector("a.logon.op_btn").click()
        driver.find_element_by_id("txt_db_user").clear()
        driver.find_element_by_id("txt_db_user").send_keys("root")
        driver.find_element_by_id("txt_db_password").clear()
        driver.find_element_by_id("txt_db_password").send_keys("dingjia")
        driver.find_element_by_id("btn_db_login").click()
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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

