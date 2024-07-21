from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()


driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for x in range(1, 6):
    click_on_button = driver.find_element(By.CSS_SELECTOR, ("[onclick='addElement()']")).click()
    count_delete_button = driver.find_elements(By.XPATH, "//button[@onclick='deleteElement()']")
print(len(count_delete_button))


driver.quit()