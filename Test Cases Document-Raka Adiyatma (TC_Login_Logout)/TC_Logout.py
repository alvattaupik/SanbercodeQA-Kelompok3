import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

        #testing1
    def test_success_logout(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # isi password
        time.sleep(1) 
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click() # klik dropdown
        
        menus = driver.find_elements(By.XPATH, "//ul[@class='oxd-dropdown-menu']")
        count = 0
        for menu in menus : 
            if count == 3 :
                menu.click()
            count += 1
        time.sleep(1)

def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()