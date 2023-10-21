# Alerts
# AutoIT - third party tool for windows pop-up

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

# Handling Alerts
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://testautomationpractice.blogspot.com/")
# alert = driver.switch_to.alert

# refer Sep_17 file for remaining code

# Locating elements inside frames - <iframe>

driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='frame-one796456169']"))
# driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0]) another way to find a frame
driver.find_element(By.XPATH, "//select[@class='drop_down']").click()

# driver.get("https://demo.automationtesting.in/Frames.html/")
# driver.find_element(By.XPATH, "//a[@href='#Multiple']").click()
# driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']"))
# driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']"))
# driver.find_element(By.TAG_NAME, 'input').send_keys('Hello from inside')
# driver.switch_to.parent_frame()
# driver.switch_to.default_content()
