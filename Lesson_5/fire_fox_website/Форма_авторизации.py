from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.CSS_SELECTOR, ("#username")).send_keys("tomsmith")
password = driver.find_element(By.CSS_SELECTOR, ("#password")).send_keys("SuperSecretPassword")
login_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.quit()