import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    #TC_01
    def test_success_login_01(self):
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

         # validasi
        response_data = driver.find_element(By.CLASS_NAME,"oxd-topbar-header-breadcrumb").text
        self.assertIn('Dashboard', response_data)

    #TC_02
    def test_failed_login_02(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin1234") # isi password
        time.sleep(1) 
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

         # validasi
        response_data = driver.find_element(By.CLASS_NAME,"orangehrm-login-error").text
        self.assertIn('Invalid credentials', response_data)

    #TC_03
    def test_failed_login_03(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Adminraka") # username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # isi password
        time.sleep(1) 
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

         # validasi
        response_data = driver.find_element(By.CLASS_NAME,"orangehrm-login-error").text
        self.assertIn('Invalid credentials', response_data)

    #TC_04
    def test_failed_login_04(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("") # username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") # isi password
        time.sleep(1) 
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

         # validasi
        response_data = driver.find_element(By.CLASS_NAME,"oxd-input-field-error-message").text
        self.assertIn('Required', response_data)

    #TC_05
    def test_failed_login_05(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("Admin") # username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("") # isi password
        time.sleep(1) 
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

          # validasi
        response_data = driver.find_element(By.CLASS_NAME,"oxd-input-field-error-message").text
        self.assertIn('Required', response_data)

    #TC_06
    def test_failed_login_06(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys("") # username
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("") # isi password
        time.sleep(1) 
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

         # validasi
        response_data = driver.find_element(By.CLASS_NAME,"oxd-input-field-error-message").text
        self.assertIn('Required', response_data)

def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()