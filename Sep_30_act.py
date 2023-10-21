import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
my_action = ActionChains(driver)
source1 = driver.find_element(By.XPATH, "//div[text()='Oslo' and @id='box1']")
target1 = driver.find_element(By.XPATH, "//div[text()='Norway']")

source2 = driver.find_element(By.XPATH, "//div[text()='Stockholm' and @id='box2']")
target2 = driver.find_element(By.XPATH, "//div[text()='Sweden']")

my_action.drag_and_drop(source1, target1).drag_and_drop(source2, target2)

driver.get("https://jqueryui.com/selectable/")
my_action = ActionChains(driver)
driver.switch_to.frame(0)
item1 = driver.find_element(By.XPATH, "//li[text()='Item 1']")
item2 = driver.find_element(By.XPATH, "//li[text()='Item 2']")
my_action.key_down(Keys.CONTROL).click(item1).click(item2).perform()

# to perform right click - actionchains.context_click