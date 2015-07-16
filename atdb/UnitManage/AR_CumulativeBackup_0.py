from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
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
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_css_selector("div.tree_expand").click()
        driver.find_element_by_link_text(u"进入").click()
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_link_text(u"新建备份作业").click()
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_id("archivedlogRadio").click()
        driver.find_element_by_id("differenceRadio").click()
        driver.find_element_by_id("nextbtnExportBackupMethod").click()
        driver.find_element_by_id("nextbtnExportDevice").click()
        driver.find_element_by_id("ftpRadio").click()
        driver.find_element_by_css_selector("div.item.ftp > label").click()
        driver.find_element_by_id("nextbtnExportType").click()
        driver.find_element_by_id("jobName").clear()
        driver.find_element_by_id("jobName").send_keys(u"归档日志备份")
        driver.find_element_by_link_text(u"提交").click()
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

