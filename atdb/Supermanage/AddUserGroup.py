from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
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
        driver.find_element_by_id("UserNameID").send_keys("dingjia")
        driver.find_element_by_id("PWID").send_keys("123456")
        driver.find_element_by_id("LoginButton").click()
        time.sleep(1)
        current_handle = self.driver.current_window_handle
        driver.switch_to_frame("headerflag")
        driver.find_element_by_id("sysManagerLink").click()
        driver.switch_to_window(current_handle)
        user = driver.find_element_by_xpath('//*[@id="navigate"]/ul[1]/li[3]/a')
        ActionChains(driver).move_to_element(user).perform()
        driver.find_element_by_xpath('//*[@id="navigate"]/ul[1]/li[3]/ul/li[2]/a').click()
        driver.find_element_by_id("account-group-add").click()
        time.sleep(2)
        driver.find_element_by_id("txt_account_group_name").clear()
        driver.find_element_by_id("txt_account_group_name").send_keys("File")
# choose users
        driver.find_element_by_xpath('//*[@id="add_account_group_modal"]/div[2]/form/div[2]/div/div/button').click()
        checkboxes = driver.find_elements_by_xpath('//*[@id="add_account_group_modal"]/div[2]/form/div[2]/div/div/div/ul/li[1]/label/input')
        for checkbox in checkboxes:
            checkbox.click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="add_account_group_modal"]/div[2]/form/div[2]/div/div/button').click()
# choose source
        driver.find_element_by_xpath('//*[@id="add_account_group_modal"]/div[2]/form/div[3]/div/div/button').click()
        checkboxes = driver.find_elements_by_xpath('//*[@id="add_account_group_modal"]/div[2]/form/div[3]/div/div/div/ul/li[1]/label/input')
        for checkbox in checkboxes:
            checkbox.click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="add_account_group_modal"]/div[2]/form/div[3]/div/div/button').click()
# submit
        driver.find_element_by_id("btn_submit_account_group").click()
        time.sleep(3)
    
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

