import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

# Handling Alerts
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://testautomationpractice.blogspot.com/")
alert = Alert(driver)
driver.find_element(By.XPATH, "//button[text()='Alert']").click()
# alert = driver.switch_to.alert
print(alert.text)
alert.accept()
driver.find_element(By.XPATH, "//button[text()='Confirm Box']").click()
print(alert.text)
alert.dismiss()
driver.find_element(By.XPATH, "//button[text()='Prompt']").click()
print(alert.text)
alert.send_keys("My Name is Khan!")
alert.accept()

# ActionChains
# instance.maximize_window()
# instance.get("https://testautomationpractice.blogspot.com/")
# action = ActionChains(instance)
# button = instance.find_element(By.XPATH, "//button[text()='Copy Text']")
# action.double_click(button).perform()
# time.sleep(2)
# action.key_down(Keys.ARROW_DOWN).perform()
#
# drag = instance.find_element(By.ID, "draggable")
# drop = instance.find_element(By.ID, "droppable")
# action.drag_and_drop(drag, drop).perform()
# time.sleep(3)
#
# slider = instance.find_element(By.ID, "slider")
# action.click_and_hold(slider).move_by_offset(10, 0).release().perform()
# time.sleep(3)
#
# resize = instance.find_element(By.XPATH, "//*[@id='resizable']/div")
# action.click_and_hold(resize).move_by_offset(100, 0).release().perform()
# time.sleep(3)
#
# sample = instance.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']")
# sample.send_keys("Hello World!")
# time.sleep(3)
