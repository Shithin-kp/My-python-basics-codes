from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.implicitly_wait(5)
select_date= "20-Aug-2025"
dates = select_date.split("-")
calender = driver.find_element(By.XPATH, "//div[@class='dateInputWrapper___f4c22e']")
calender.click()
time.sleep(2)

td= driver.find_elements(By.XPATH, "//div[@id='rb-calendar_onward_cal']//td")
for date in td:
    if date.text == dates[0]:
        date.click()
        break