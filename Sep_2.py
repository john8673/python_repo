#Selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()           #This line launches the browser
chrome_driver.get("https://www.google.com")  #This line navigates to the URl
time.sleep(3)

edge_driver = webdriver.Edge()
edge_driver.get("https://www.google.com")
time.sleep(3)

chrome_driver.find_element(By.NAME, "q").send_keys("John")
time.sleep(10)

# chrome_driver.quit()
# time.sleep(5)
# edge_driver.quit()

