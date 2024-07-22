from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get(" http://uitestingplayground.com/ajax")

click_blue_button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

find_text = WebDriverWait(driver, 16).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#content"), "Data loaded with AJAX get request."))
print (f"Able to read the text: {find_text}")

driver.quit()