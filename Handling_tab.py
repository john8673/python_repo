import time

from selenium import webdriver
import os
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.implicitly_wait(20)
chrome_driver.get("https://www.zenclass.in/login")

email = chrome_driver.find_element(By.NAME, "email")
email.send_keys("mailstoabraham@gmail.com")
passwd = os.getenv("password")
password = chrome_driver.find_element(By.NAME, "password")
password.send_keys(passwd)
login = chrome_driver.find_element(By.XPATH, "//button[text()='Login']")
login.click()

add_session = chrome_driver.find_element(By.XPATH, "//h5[text()='Additional: (08/10/2023) @ 03.00 PM']")
add_session.click()
rec_button = chrome_driver.find_element(By.XPATH, "//button[@class='join-btn']")
rec_button.click()
joining_link = chrome_driver.find_element(By.XPATH, "//div[text()='Recording Link : ']/parent::div")
joining_link.click()

tabs = chrome_driver.window_handles

for i in tabs:
    if chrome_driver.title == ("Passcode Required - Zoom"):
        chrome_driver.switch_to.window(i)
        link_passwd = chrome_driver.find_element(By.ID, "passcode")
        link_passwd.send_keys("4Er%?8wY")
        watch_rec = chrome_driver.find_element(By.ID, "passcode_btn")
        watch_rec.click()

time.sleep(10)
