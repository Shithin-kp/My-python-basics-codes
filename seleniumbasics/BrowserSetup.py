from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
driver.implicitly_wait(5)
first_name = driver.find_element(By.CSS_SELECTOR, "input[placeholder='First Name']")
first_name.send_keys("John")
last_name = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Last Name']")
last_name.send_keys("Doe")
address = driver.find_element(By.CSS_SELECTOR, ".form-control.ng-pristine.ng-untouched.ng-valid[rows='3']")
address.send_keys("123 Main St, Springfield")
email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
email.send_keys("johndoe@gmail.com")
phone = driver.find_element(By.CSS_SELECTOR, "input[type='tel']")
phone.send_keys("1234567890")
radio = driver.find_element(By.XPATH, "//input[@value='Male']")
radio.click()
li = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for ele in li:
    val= ele.get_attribute("value")
    print(val)
    if val == "Cricket":
        ele.click()
Skills = driver.find_element(By.ID, "Skills")
select = Select(Skills)
#elect.select_by_visible_text("Java")
#select.select_by_index(1)
select.select_by_value("Design")
print(driver.current_url)