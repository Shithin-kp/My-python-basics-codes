from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.implicitly_wait(5)

#Parent window
parent_window = driver.current_window_handle
print("Parent Window Handle:", parent_window)
click_link = driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']//button[@class='btn btn-info'][normalize-space()='click']")
click_link.click()

#All windows
all_windows = driver.window_handles

#switch to child window
for window in all_windows:
    print("Window Handle:", window)
    if window != parent_window:
        driver.switch_to.window(window)
        time.sleep(2)
        print("Switched to Child Window:", window)
        break
download = driver.find_element(By.XPATH, "//span[normalize-space()='Downloads']")
download.click()
driver.close()
driver.switch_to.window(parent_window)
time.sleep(2)

