from selenium import webdriver
import time

from selenium.webdriver.common.by import By

import os

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.implicitly_wait(20)
chrome_driver.get("https://www.zenclass.in")
# WebDriverWait(chrome_driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "email")))
# time.sleep(3)
chrome_driver.find_element(By.NAME, "email").send_keys("mailstoabraham@gmail.com")
password = os.getenv("password")
chrome_driver.find_element(By.NAME, "password").send_keys(password)
login = chrome_driver.find_element(By.XPATH, "//button[text()='Login']")
login.click()
# time.sleep(10)
session_25 = chrome_driver.find_element(By.XPATH, "//h6[text()='25']")
session_25.click()
# time.sleep(5)
join_button = chrome_driver.find_element(By.XPATH, "//button[@class='join-btn']")
join_button.click()
# time.sleep(5)
class_link = chrome_driver.find_element(By.XPATH, "//div[text()='Class Link : ']")
class_link.click()
# time.sleep(5)
