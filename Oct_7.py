import time

import os
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")

my_dropdown = Select(driver.find_element(By.ID, "RESULT_RadioButton-9"))
result = my_dropdown.options
my_dropdown.select_by_index(3)
time.sleep(2)
driver.get_screenshot_as_file(os.getcwd()+"\SS\Evening_SS.png")
# driver.get_screenshot_as_png()
my_dropdown.select_by_value("Radio-1")
time.sleep(2)
driver.get_screenshot_as_file(os.getcwd()+"\SS\Afternoon_SS.png")
my_dropdown.select_by_visible_text("Morning")
time.sleep(2)
driver.get_screenshot_as_file(os.getcwd()+"\SS\Morning_SS.png")  # getting directory path using os.getcwd
# driver.get_screenshot_as_file("C:\Automation testing\AT18\Eshwar's sessions\SS\Morning_SS.png") - giving full file path

# for x in result:
#     print(x.text)
