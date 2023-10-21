from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Headless browser
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")
my_options.add_argument("--start-maximized")
chrome_driver = webdriver.Chrome(options=my_options)
chrome_driver.maximize_window()
chrome_driver.implicitly_wait(20)
# chrome_driver.get("https://demo.automationtesting.in/Frames.html")
chrome_driver.get("https://testautomationpractice.blogspot.com/")
actions = ActionChains(chrome_driver)

# register = chrome_driver.find_element(By.LINK_TEXT, "Register")
# chrome_driver.execute_script("arguments[0].click();", register)
#
# # scrolling using JS executor
# chrome_driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# chrome_driver.execute_script("window.scrollTo(0, 1000);")
#
# # scrolling using ActionChains
# actions.scroll_by_amount(0, 1200).perform()

returned_value = chrome_driver.execute_script("return document.getElementById('field1').value;")
print(returned_value)
