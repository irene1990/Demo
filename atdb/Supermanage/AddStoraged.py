#-*-coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
#        self.driver.set_window_size(800, 480)
        self.base_url = "http://192.168.82.32/dbackup"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get("http://192.168.82.32/dbackup/index.php")
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_id("UserNameID").clear()
        driver.find_element_by_id("UserNameID").send_keys("dingjia")
        driver.find_element_by_id("PWID").clear()
        driver.find_element_by_id("PWID").send_keys("dingjia123")
        driver.find_element_by_id("LoginButton").click()
        time.sleep(3)
        current_handle = self.driver.current_window_handle
        driver.switch_to_frame("headerflag")
        driver.find_element_by_id("sysManagerLink").click()
        driver.switch_to_window(current_handle)
        driver.find_element_by_xpath('//*[@id="navigate"]/ul[1]/li[2]/a').click()
        driver.find_element_by_xpath("/html/body/div[4]/div[3]/div[1]/div[1]/div[1]/div/a").click()
        driver.find_element_by_id("txt_ftp_name").clear()
        driver.find_element_by_id("txt_ftp_name").send_keys("82.32")
        driver.find_element_by_id("txt_ftp_address").clear()
        driver.find_element_by_id("txt_ftp_address").send_keys("192.168.82.32")
        driver.find_element_by_id("txt_ftp_path").clear()
        driver.find_element_by_id("txt_ftp_path").send_keys("Files")
        driver.find_element_by_css_selector("input.w80.input-retention-days").clear()
        driver.find_element_by_css_selector("input.w80.input-retention-days").send_keys("2")
        time.sleep(13)
        driver.find_element_by_id("add_ftp_submit").click()
        time.sleep(3)
        self.assertEqual(u"提交成功", self.close_alert_and_get_its_text())
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

