
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
# chrome_driver.implicitly_wait(30)
chrome_driver.get("https://www.google.com/")
WebDriverWait(chrome_driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "q")))
chrome_driver.find_element(By.XPATH,"//textarea[@name='q']").send_keys("John")
# time.sleep(3)
# from a particular node to parent node
# /parent::* (star or parent tag name)
# parent_child_sibling = chrome_driver.find_element(By.XPATH, "//label[text()='Email:']/parent::div/child::label[text()='Email:']/preceding-sibling::input")
# # getting all the book names
# book_name_elements = chrome_driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/td[1]")
#
# for element in book_name_elements:
#     print(element.text)

