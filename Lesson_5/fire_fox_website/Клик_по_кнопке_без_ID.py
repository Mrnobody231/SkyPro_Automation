from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

driver.maximize_window()
driver.get(" http://uitestingplayground.com/dynamicid")

for x in range(1, 4):
    click_button = driver.find_element(By.CSS_SELECTOR, ("button[class='btn btn-primary']")).send_keys(Keys.RETURN)
print(x)


driver.quit()