import time
from time import sleep

from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import visibility_of, visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
wait = WebDriverWait(driver, 25)

driver.get("https://vynoteka.lt/")
butinu_mygtukai = driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div[3]/div/div[1]/button")
butinu_mygtukai.click()

slapukai = driver.find_element(By.CLASS_NAME, 'c-button--blue-inversed')
slapukai.click()

wait.until(expected_conditions.element_to_be_clickable((By.ID, "omnisend-form-63ff1f31b40d6530aba59a6d-form-close-icon"))).click()
print('praejo')

search = (driver.find_element(By.CLASS_NAME, 'form-control'))
search.click()
search.send_keys("alus")

# driver.find_element(By.CLASS_NAME, 'form-control').send_keys(Keys.ENTER)
wait.until(visibility_of_element_located((By.CLASS_NAME, "search-results__aside")))

# time.sleep(10)
driver.find_element(By.CLASS_NAME, 'form-control').send_keys(Keys.ENTER)

# search1 = (driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div[2]/div/div/div[3]/div/div/div/form/div[1]/button'))
# search1.click()
# driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/header/div[2]/div/div/div[3]/div/div/div/form/div[1]/div/input').send_keys(Keys.Enter)

time.sleep(30)

# keyword = driver.find_element(By.ID,"searchKeyword")
# keyword.send_keys("kadagys")
# driver.find_element(By.ID,"searchKeyword").send_keys(Keys.ENTER)
# time.sleep(3)