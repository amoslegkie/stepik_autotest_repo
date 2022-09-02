import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import math
import time

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():
    message = ""
    link_list = ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1", "236903/step/1", "236904/step/1", "236905/step/1"]
    @pytest.mark.parametrize('links', link_list)
    def test_sites(self, browser, links):
        link = f"https://stepik.org/lesson/{links}/"
        browser.get(link)
        browser.implicitly_wait(20)
        input1 = browser.find_element(By.TAG_NAME, "textarea")
        input1.send_keys(str(math.log(int(time.time()))))
        button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
            )
        button.click()
        browser.implicitly_wait(10)
        text1 = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        #WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locator).text)
        if text1 != "Correct!":
            self.message += text1
            print(self.message)
        assert text1 == "Correct!"
        
if __name__ == "__main__":
    unittest.main()
        
    
    
