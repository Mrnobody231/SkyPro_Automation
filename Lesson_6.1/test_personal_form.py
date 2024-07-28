from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_fill_form():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='first-name']").send_keys("Иван")
    chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='last-name']").send_keys("Петров")
    chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='address']").send_keys("Ленина, 55-3")
    chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='zip-code']").send_keys("")
    chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='e-mail']").send_keys("test@skypro.com")
    chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='phone']").send_keys("+7985899998787")
    chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='city']").send_keys("Москва")
    chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='country']").send_keys("Россия")
    chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='job-position']").send_keys("QA")
    chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='company']").send_keys("SkyPro")

    chrome.find_element(By.CSS_SELECTOR, ("button[type='submit']")).click()

    locators = [
        ".alert.alert-success#first-name", 
        ".alert.alert-success#last-name",
        ".alert.alert-success#address",
        ".alert.alert-success#email",
        ".alert.alert-success#phone",
        ".alert.alert-success#city",
        ".alert.alert-success#country",
        ".alert.alert-success#job-position",
        ".alert.alert-success#company"
        ]
    
    for locator in locators:
        color = WebDriverWait(chrome, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator))).value_of_css_property("background-color")
        assert color == "rgba(209, 231, 221, 1)"
    
    zip_code_color = WebDriverWait(chrome, 4).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.py-2.alert-danger#zip-code"))).value_of_css_property("background-color")
    assert zip_code_color == "rgba(248, 215, 218, 1)"


    chrome.quit()
