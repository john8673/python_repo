import time

from selenium import webdriver
import os
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.implicitly_wait(20)
chrome_driver.get("https://demo.automationtesting.in/Windows.html")

chrome_driver.find_element(By.XPATH, "//button[text()='    click   ']").click()
list_of_tabs = chrome_driver.window_handles
window_frames = list_of_tabs[0]
window_selenium = list_of_tabs[1]
chrome_driver.switch_to.window(window_selenium)
print(chrome_driver.title)
time.sleep(5)
chrome_driver.switch_to.window(window_frames)
print(chrome_driver.title)

