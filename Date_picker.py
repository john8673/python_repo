import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.implicitly_wait(20)
chrome_driver.get("https://testautomationpractice.blogspot.com/")
actions = ActionChains(chrome_driver)
actions.scroll_by_amount(0, 1200).perform()

# chrome_driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# chrome_driver.execute_script("window.scrollTo(0, 1000);")
time.sleep(5)
chrome_driver.switch_to.frame(0)
date = chrome_driver.find_element(By.ID, "RESULT_TextField-2")
date.send_keys("01/01/2000")
