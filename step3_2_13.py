import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistration(unittest.TestCase):
    def test_registration_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)    
        input1 = browser.find_element(By.CLASS_NAME, "form-control.first[required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "form-control.second[required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "form-control.third[required]")
        input3.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        phrase = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", phrase, "Should be correct required registration data")
        #time.sleep(500)
        
    def test_registration_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser1 = webdriver.Chrome()
        browser1.get(link)    
        input1 = browser1.find_element(By.CLASS_NAME, "form-control.first[required]")
        input1.send_keys("Ivan")
        input2 = browser1.find_element(By.CLASS_NAME, "form-control.second[required]")
        input2.send_keys("Petrov")
        input3 = browser1.find_element(By.CLASS_NAME, "form-control.third[required]")
        input3.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser1.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        phrase = browser1.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", phrase, "Should be correct required registration data")
        #time.sleep(500)
        
if __name__ == "__main__":
    unittest.main()