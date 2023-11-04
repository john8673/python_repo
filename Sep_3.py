from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver = webdriver.Chrome()
chrome_driver.get("https://www.w3schools.com")
time.sleep(3)
id_locator_string = "radio_darkcode"
id_locator_element = chrome_driver.find_elements(By.ID, id_locator_string)
print(f'The number of elements in webpage with ID as {id_locator_string} are: {len(id_locator_element)}')
name_locator_string = "viewport"
name_locator_element = chrome_driver.find_elements(By.NAME, name_locator_string)
print(f"The number of elements in webpage with Name as viewport are: {len(name_locator_element)}")
class_locator_element = chrome_driver.find_element(By.CLASS_NAME, "w3-bar")
print(class_locator_element)
link_text_element = chrome_driver.find_element(By.LINK_TEXT, "UPGRADE")
link_text_element.click()
time.sleep(3)
