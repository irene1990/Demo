#coding=utf-8
from selenium import webdriver
import time,CONFIG
class test_shenpi():
    def __init__(self):
        self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(5)
        self.base_url = CONFIG.IP
    def login(self,username,password):
        driver = self.driver
        print 'login'
        driver.get("192.168.82.52")
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("user_login").click()
        driver.find_element_by_id("job").click()
        try:
            alter = switch_to_alert()
            alter.accept()
        except:
            print '------login-----'
    def approval(self,approvalor):
        driver = self.driver
        rnum = driver.find_elements_by_xpath("//*[@id='pageinfo']/tbody/tr") #table row numbers
        i = 1
        while i < len(rnum)+1:
            path = "//*[@id='pageinfo']/tbody/tr["+str(i)+"]/td[6]/button"
            nums = len(driver.find_elements_by_xpath(path))  # numbers of button
            btext = driver.find_element_by_xpath(path+"["+str(1)+"]").text.encode('utf-8')  # button's text
            tmpapprovalor = driver.find_element_by_xpath("//*[@id='pageinfo']/tbody/tr["+str(i)+"]/td[5]").text.encode('utf-8')		
            if tmpapprovalor == approvalor:
                if btext == '通过':
                    print approvalor + ' pass'
                    #driver.find_element_by_xpath(path+"["+str(1)+"]").click()
                    try:
                        alter = switch_to_alert()
                        alter.accept()
                        try:
                            alter1 = switch_to_alert()
                            alter1.accept()
                        except:
                            print '-----------'
                    except:
                        print '-----------'
                    time.sleep(2)
            i +=1
        driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/ul/li[4]/a').click()
