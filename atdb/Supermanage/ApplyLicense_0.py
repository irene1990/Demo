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
        driver.get("http://192.168.82.32/dbackup/")
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_id("UserNameID").clear()
        driver.find_element_by_id("UserNameID").send_keys("dingjia")
        driver.find_element_by_id("PWID").clear()
        driver.find_element_by_id("PWID").send_keys("dingjia123")
        driver.find_element_by_id("LoginButton").click()
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_id("sysManagerLink").click()
        driver.find_element_by_link_text(u"许可证").click()
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_id("licenses_request").click()
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_name("type").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_css_selector("i.icon-remove").click()
        Select(driver.find_element_by_name("os")).select_by_visible_text("Linux-x86")
        driver.find_element_by_css_selector("button.ms-choice").click()
        driver.find_element_by_name("selectItemtypes.features").click()
        driver.find_element_by_xpath("//table[@id='modulesTable']/tbody/tr/td/div/div/ul/li[2]/label").click()
        driver.find_element_by_xpath("(//input[@name='selectItemtypes.features'])[3]").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1437718341153']/ul/li[4]/label").click()
        driver.find_element_by_xpath("(//input[@name='selectItemtypes.features'])[4]").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1437718341153']/ul/li[5]/label").click()
        driver.find_element_by_xpath("(//input[@name='selectItemtypes.features'])[5]").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1437718341153']/ul/li[6]/label").click()
        driver.find_element_by_xpath("(//input[@name='selectItemtypes.features'])[6]").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1437718341153']/ul/li[7]/label").click()
        driver.find_element_by_xpath("(//input[@name='selectItemtypes.features'])[14]").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1437718341153']/ul/li[15]/label").click()
        driver.find_element_by_id("page_3").click()
        Select(driver.find_element_by_name("os")).select_by_visible_text("AIX")
        driver.find_element_by_css_selector("button.ms-choice").click()
        driver.find_element_by_name("selectItemtypes.features").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1437718341153']/ul/li[2]/label").click()
        driver.find_element_by_xpath("(//input[@name='selectItemtypes.features'])[2]").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1437718341153']/ul/li[3]/label").click()
        driver.find_element_by_xpath("(//input[@name='selectItemtypes.features'])[3]").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1437718341153']/ul/li[4]/label").click()
        driver.find_element_by_css_selector("div.wizard-buttons-container").click()
        Select(driver.find_element_by_name("os")).select_by_visible_text("Windows")
        driver.find_element_by_css_selector("button.ms-choice").click()
        driver.find_element_by_xpath("(//input[@name='selectItemtypes.features'])[16]").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1437718341153']/ul/li[17]/label").click()
        driver.find_element_by_css_selector("div.wizard-buttons-container").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        self.assertEqual(u"您确认要提交吗？", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text(u"退出").click()
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

