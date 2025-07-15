from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Index.html")
driver.maximize_window()
driver.implicitly_wait(5)

#wait sleep
time.sleep(2)  # Wait for 5 seconds

#Implicit Wait
driver.implicitly_wait(5)  # Wait for elements to be available for 5 seconds

#Explicit Wait
wait = WebDriverWait(driver, 5)# Wait for up to 5 seconds
wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("<EMAIL>")