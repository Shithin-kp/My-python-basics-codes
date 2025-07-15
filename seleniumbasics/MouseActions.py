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
driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()
driver.implicitly_wait(5)
#Action chains
woman= driver.find_element(By.XPATH, "//a[@id='ui-id-4']")
actions = ActionChains(driver)
actions.move_to_element(woman).perform()
top = driver.find_element(By.XPATH, "//a[@id='ui-id-9']")
actions.move_to_element(top).perform()
jackets = driver.find_element(By.XPATH, "//a[@id='ui-id-11']")
actions.click(jackets).perform()
time.sleep(2)
search = driver.find_element(By.XPATH, "//input[@id='search']")
actions.key_down(Keys.SHIFT).send_keys("shithin").key_up(Keys.SHIFT).perform()
time.sleep(2)