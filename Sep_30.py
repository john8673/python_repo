# Data driven framework
# json - javascript object notation
# import time
#
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.common.by import By
import json

import os

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

file_open1 = open("data.json")
json_dict1 = json.load(file_open1)

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.implicitly_wait(20)
chrome_driver.get("https://www.zenclass.in")
# WebDriverWait(chrome_driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, "email")))
chrome_driver.find_element(By.NAME, "email").send_keys(json_dict1.get("john_data").get("email_id"))
chrome_driver.find_element(By.NAME, "password").send_keys(json_dict1.get("john_data").get("passwd"))


# keyword driven framework


def login():
    print("I'm executing login test")


def homepage():
    print("I'm executing homepage test")


def logout():
    print("I'm executing logout test")


file_open2 = open("keyword.json")
json_dict2 = json.load(file_open2)
eval(json_dict2.get("logout_test") + "()")

# ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
action = ActionChains(driver)
button = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
action.double_click(button).perform()
action.key_down(Keys.ARROW_DOWN).perform()

drag = driver.find_element(By.ID, "draggable")
drop = driver.find_element(By.ID, "droppable")
action.drag_and_drop(drag, drop).perform()

slider = driver.find_element(By.ID, "slider")
action.click_and_hold(slider).move_by_offset(10, 0).release().perform()
resize = driver.find_element(By.XPATH, "//*[@id='resizable']/div")
action.click_and_hold(resize).move_by_offset(100, 0).release().perform()

sample = driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']")
sample.send_keys("Hello World!")
