import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Page_Objects_Oct_14_15.Login_Page import Login_Page

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.implicitly_wait(30)
chrome_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

lp_object = Login_Page(chrome_driver)
lp_object.enter_username("Admin")
lp_object.enter_password("admin123")
lp_object.login_button_click()
time.sleep(10)
