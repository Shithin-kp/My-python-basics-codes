from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()
driver.implicitly_wait(5)
first_alert = driver.find_element(By.ID, "OKTab")
time.sleep(2)
first_alert.click()
time.sleep(2)
driver.switch_to.alert.accept()
second_alert_page = driver.find_element(By.XPATH, "//a[normalize-space()='Alert with OK & Cancel']")
second_alert_page.click()
second_alert= driver.find_element(By.ID, "CancelTab")
second_alert.click()
time.sleep(2)
driver.switch_to.alert.dismiss()
third_alert_page = driver.find_element(By.XPATH, "//a[normalize-space()='Alert with Textbox']")
third_alert_page.click()
third_alert = driver.find_element(By.ID, "Textbox")
third_alert.click()
time.sleep(2)
txt = driver.switch_to.alert.text
print(txt)
driver.switch_to.alert.send_keys("Hello World")
time.sleep(2)
driver.switch_to.alert.accept()

