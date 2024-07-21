from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")

for x in range (1, 4):
    try:
        click_button = driver.find_element(By.CSS_SELECTOR, ("button.btn.btn-primary")).click()
        alert = driver.switch_to.alert
        alert.accept()
        print(f"{x}")
    except NoSuchElementException:
        print(f"{x}")


driver.quit()