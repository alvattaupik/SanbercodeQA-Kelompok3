import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class TestAddEmployee(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_Success_addemployee(self):
        #steps
        #buka web browser
        driver = self.browser 
        #buka situs
        driver.get("https://opensource-demo.orangehrmlive.com") 
        time.sleep(1)
        #isi email
        driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin") 
        time.sleep(1)
        #isi password
        driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
        time.sleep(1)
        #Login
        driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
        time.sleep(1)
        #PIM
        driver.find_element(By.XPATH,"//a[.='PIM']").click()
        time.sleep(1)
        #Add employee
        driver.find_element(By.XPATH,"//li[@class='oxd-topbar-body-nav-tab']").click() 
        time.sleep(1)
        #Firstname
        driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys('Dani') 
        time.sleep(1)
        #Middlename
        driver.find_element(By.XPATH,"//input[@name='middleName']").send_keys('Adam')
        time.sleep(1)
        #Lastname
        driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys('Jackson')
        time.sleep(1)
        #Save
        driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click()
        time.sleep(1)

    def test_b_Failed_addemployee_Blankempoyeefullname(self):
        #steps
        #buka web browser
        driver = self.browser 
        #buka situs
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") 
        time.sleep(1)
        #isi email
        driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin") 
        time.sleep(1)
        #isi password
        driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
        time.sleep(1)
        #Login
        driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
        time.sleep(1)
        #PIM
        driver.find_element(By.XPATH,"//a[.='PIM']").click()
        time.sleep(1)
        #Add employee
        driver.find_element(By.XPATH,"//li[@class='oxd-topbar-body-nav-tab']").click() 
        time.sleep(1)
        #Save
        driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click()
        time.sleep(1)
          
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()



