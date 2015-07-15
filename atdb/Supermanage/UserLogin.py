#-*-coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.82.32/dbackup"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled(self):
        driver = self.driver
        driver.get("http://192.168.82.32/dbackup/")
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_id("UserNameID").clear()
        driver.find_element_by_id("UserNameID").send_keys("admin")
        driver.find_element_by_id("PWID").clear()
        driver.find_element_by_id("PWID").send_keys("admin")
        driver.find_element_by_id("LoginButton").click()
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.find_element_by_link_text(u"客户端管理").click()
        self.assertEqual(u"鼎甲迪备备份服务器", driver.title)
        driver.close()

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
#    unittest.main()
    i = 0
    while i < 30:
        suite = unittest.TestSuite()
        ttime = time.strftime("%H:%M:%S",time.localtime(time.time()))
        suite.addTest(Untitled("test_untitled"))
        f = open("result.txt",'a')
        f.write("\n")
        f.write("****************************************************************************"+'\n')
        f.write(ttime+'\n')
        f.close()
        runner = unittest.TextTestRunner(open("./result.txt","a"))
        runner.run(suite)
        i += 1
#        time.sleep(120)
