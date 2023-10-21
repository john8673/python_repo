import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

car_driver = webdriver.Chrome()
car_driver.maximize_window()
car_driver.implicitly_wait(20)
car_driver.get("https://jqueryui.com/")
action = ActionChains(car_driver)

# opening different tabs
draggable_tab = car_driver.find_element(By.XPATH, "//a[text()='Draggable']")
droppable_tab = car_driver.find_element(By.XPATH, "//a[text()='Droppable']")
resizeable_tab = car_driver.find_element(By.XPATH, "//a[text()='Resizable']")
selectable_tab = car_driver.find_element(By.XPATH, "//a[text()='Selectable']")
sortable_tab = car_driver.find_element(By.XPATH, "//a[text()='Sortable']")


# draggable tab
def draggable_operation():
    draggable_tab.click()
    car_driver.switch_to.frame(0)
    draggable_action = car_driver.find_element(By.ID, "draggable")
    action.click_and_hold(draggable_action).move_by_offset(200, 120).release().perform()


# droppable_tab
def droppable_operation():
    car_driver.switch_to.default_content()
    car_driver.find_element(By.XPATH, "//a[text()='Droppable']").click()
    # droppable_tab.click() - stale element exception (elements go stale when browser reloads)
    car_driver.switch_to.frame(0)
    source = car_driver.find_element(By.ID, "draggable")
    destination = car_driver.find_element(By.ID, "droppable")
    action.drag_and_drop(source, destination).perform()


# resizeable_tab
def resizable_operation():
    car_driver.switch_to.default_content()
    car_driver.find_element(By.XPATH, "//a[text()='Resizable']").click()
    car_driver.switch_to.frame(0)
    resizeable_action = car_driver.find_element(By.XPATH, "//div[@id='resizable']/div[3]")
    action.click_and_hold(resizeable_action).move_by_offset(300, 200).release().perform()


# selectable_tab
def selectable_operation():
    car_driver.switch_to.default_content()
    car_driver.find_element(By.XPATH, "//a[text()='Selectable']").click()
    car_driver.switch_to.frame(0)
    selectable_item1 = car_driver.find_element(By.XPATH, "//li[text()='Item 1']")
    selectable_item2 = car_driver.find_element(By.XPATH, "//li[text()='Item 2']")
    selectable_item3 = car_driver.find_element(By.XPATH, "//li[text()='Item 3']")
    selectable_item4 = car_driver.find_element(By.XPATH, "//li[text()='Item 4']")
    selectable_item5 = car_driver.find_element(By.XPATH, "//li[text()='Item 5']")
    selectable_item6 = car_driver.find_element(By.XPATH, "//li[text()='Item 6']")
    selectable_item7 = car_driver.find_element(By.XPATH, "//li[text()='Item 7']")
    action.key_down(Keys.CONTROL).click(selectable_item1).click(selectable_item2).click(selectable_item3).click(
        selectable_item4).click(selectable_item5).click(selectable_item6).click(selectable_item7).key_up(
        Keys.CONTROL).release().perform()


# sortable_tab
def sortable_operation():
    car_driver.switch_to.default_content()
    car_driver.find_element(By.XPATH, "//a[text()='Sortable']").click()
    car_driver.switch_to.frame(0)
    sortable_item1 = car_driver.find_element(By.XPATH, "//li[text()='Item 1']")
    sortable_item2 = car_driver.find_element(By.XPATH, "//li[text()='Item 2']")
    sortable_item3 = car_driver.find_element(By.XPATH, "//li[text()='Item 3']")
    sortable_item4 = car_driver.find_element(By.XPATH, "//li[text()='Item 4']")
    sortable_item5 = car_driver.find_element(By.XPATH, "//li[text()='Item 5']")
    sortable_item6 = car_driver.find_element(By.XPATH, "//li[text()='Item 6']")
    sortable_item7 = car_driver.find_element(By.XPATH, "//li[text()='Item 7']")
    action.click_and_hold(sortable_item1).move_by_offset(50, 250).release().perform()
    action.click_and_hold(sortable_item2).move_by_offset(50, 250).release().perform()
    action.click_and_hold(sortable_item3).move_by_offset(50, 250).release().perform()
    action.click_and_hold(sortable_item4).move_by_offset(50, 250).release().perform()
    action.click_and_hold(sortable_item5).move_by_offset(50, 250).release().perform()
    action.click_and_hold(sortable_item6).move_by_offset(50, 250).release().perform()
    action.click_and_hold(sortable_item7).move_by_offset(50, 250).release().perform()

draggable_operation()
droppable_operation()
resizable_operation()
selectable_operation()
sortable_operation()
