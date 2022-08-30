from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math import *

def calc(x):
    return log(abs(12 * sin(x)))


try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    button = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button2 = browser.find_element(By.ID, "book")
    button2.click()
    
    
    x = int(browser.find_element(By.ID, "input_value").text)
    y = calc(x)
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)
    button3 = browser.find_element(By.ID, 'solve')
    button3.click()
    alert = browser.switch_to.alert
    alert_text = alert.text.split("quiz: ")[1]
    print(alert_text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(100)
    # закрываем браузер после всех манипуляций
    browser.quit()