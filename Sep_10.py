
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)
# from a particular node to parent node
# /parent::* (star or parent tag name)
parent_child_sibling = chrome_driver.find_element(By.XPATH, "//label[text()='Email:']/parent::div/child::label[text()='Email:']/preceding-sibling::input")
# getting all the book names
book_name_elements = chrome_driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/td[1]")

for element in book_name_elements:
    print(element.text)

# next topic 1.CSS selector, 2.Implicit and Explicit wait
