import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



class TestAddOrganizationLocation(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def tc_success_add_organization_location(self):
        #steps
        #1.buka web browser
        driver = self.browser 
        
        #2.buka situs
        driver.get("https://opensource-demo.orangehrmlive.com") 
        time.sleep(4)

        #3.isi email
        driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin") 
        time.sleep(2)
        #4.isi password
        driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
        time.sleep(2)
        #5.Login
        driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
        time.sleep(2)


        #6.Pilih Menu Admin
        driver.find_element(By.XPATH,"//a[.='Admin']").click()
        time.sleep(2)

        #7.Klik organization
        driver.find_element(By.XPATH,"//span[normalize-space()='Organization']//i[@class='oxd-icon bi-chevron-down']").click() 
        time.sleep(2)

       #8.Klik organization- location
        driver.find_element(By.XPATH,"//li[@class='--active oxd-topbar-body-nav-tab --parent']//li[2]").click() 
        time.sleep(2)


      

    def tc_failed_add_organization_location(self):
        #steps
        #1.buka web browser
        driver = self.browser 
        #2.buka situs
        driver.get("https://opensource-demo.orangehrmlive.com") 
        time.sleep(1)

        #3.isi email
        driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin") 
        time.sleep(1)
        #4.isi password
        driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
        time.sleep(1)

        #5. Klik Login
        driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
        time.sleep(1)

        
        #6.Pilih Menu Admin
        driver.find_element(By.XPATH,"//a[.='Admin']").click()
        time.sleep(2)

        #7.Klik organization
        driver.find_element(By.XPATH,"//span[normalize-space()='Organization']//i[@class='oxd-icon bi-chevron-down']").click() 
        time.sleep(2)

       #8.Klik organization- location
        driver.find_element(By.XPATH,"//li[@class='--active oxd-topbar-body-nav-tab --parent']//li[2]").click() 
        time.sleep(2)


    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()



