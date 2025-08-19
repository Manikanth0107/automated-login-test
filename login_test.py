import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import config

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run without opening browser window
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get(config.BASE_URL)
        self.driver.find_element(By.ID, "username").send_keys(config.USERNAME)
        self.driver.find_element(By.ID, "password").send_keys(config.PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)
        success_message = self.driver.find_element(By.ID, "flash").text
        self.assertIn("You logged into a secure area!", success_message)

    def test_invalid_login(self):
        self.driver.get(config.BASE_URL)
        self.driver.find_element(By.ID, "username").send_keys(config.USERNAME)
        self.driver.find_element(By.ID, "password").send_keys(config.INVALID_PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)
        error_message = self.driver.find_element(By.ID, "flash").text
        self.assertIn("Your password is invalid!", error_message)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()