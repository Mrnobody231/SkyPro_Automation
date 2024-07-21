from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable


driver = webdriver.Firefox()
action = ActionChains(driver)

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/entry_ad")

close_button = WebDriverWait(driver, 10).until(element_to_be_clickable((By.CSS_SELECTOR, ("div.modal-footer"))))
action.click(close_button).perform()
print("Close button were found ")

driver.quit()