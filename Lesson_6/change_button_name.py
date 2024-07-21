from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

write_text = driver.find_element(By.CSS_SELECTOR, "input[placeholder='MyButton']").send_keys("SkyPro")
click_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
get_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(f"New buttons name is: {get_text}") 

driver.quit()