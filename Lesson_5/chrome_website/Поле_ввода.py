from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")

write_number = driver.find_element(By.CSS_SELECTOR, ("input[type='number']")).send_keys("1000")
reset_number = driver.find_element(By.CSS_SELECTOR, ("input[type='number']")).clear()
new_number = driver.find_element(By.CSS_SELECTOR, ("input[type='number']")).send_keys("999")

driver.quit()