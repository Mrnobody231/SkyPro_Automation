from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


upload_pictures = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#award"))).get_attribute("src")
print(f'The value of src is : {upload_pictures}')

driver.quit()