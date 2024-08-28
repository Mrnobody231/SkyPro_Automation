from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


@allure.epic("Fill the form")
class MainPage:
    def __init__(self, driver):
        self.chrome = driver
        self.chrome.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.chrome.maximize_window()

    @allure.step("Insert all fields with data")
    def fill_form_with_data(self, data: dict):
        (self.chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='first-name']").send_keys
         (data['first-name']))
        (self.chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='last-name']").send_keys
         (data['last-name']))
        (self.chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='address']").send_keys
         (data['address']))
        (self.chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='zip-code']").send_keys
         (data['zip-code']))
        self.chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='e-mail']").send_keys(data['e-mail'])
        self.chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='phone']").send_keys(data['phone'])
        self.chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='city']").send_keys(data['city'])
        self.chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='country']").send_keys(data['country'])
        (self.chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='job-position']").send_keys
         (data['job-position']))
        self.chrome.find_element(By.CSS_SELECTOR, "[class='form-control'][name='company']").send_keys(data['company'])

    @allure.step("Create dictionary with data")
    def form_data(self):
         return {
        "first-name" : "Иван", 
        "last-name" : "Петров",
        "address" : "Ленина, 55-3",
        "zip-code" : "",
        "e-mail" : "test@skypro.com",
        "phone" : "+7985899998787",
        "city" : "Москва",
        "country" : "Россия",
        "job-position" : "QA",
        "company" : "SkyPro"
        }

    @allure.step("Click button Submit")
    def click_button(self):
        self.chrome.find_element(By.CSS_SELECTOR, ("button[type='submit']")).click()

    @allure.step("Return color by selected css_attribute when field is not empty")
    def field_is_not_empty(self, time: int, css_attribute: str):
        try:
            locators = [
            "#first-name", 
            "#last-name",
            "#address",
            "#email",
            "#phone",
            "#city",
            "#country",
            "#job-position",
            "#company"
            ]
            for locator in locators:
                color = WebDriverWait(self.chrome, time).until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, locator))).value_of_css_property(css_attribute)
        except TimeoutException:
             return color

    @allure.step("Return color by selected css_attribute when field is empty")
    def field_is_empty(self, time: int, css_attribute: str ):
      color =  WebDriverWait(self.chrome, time).until(EC.visibility_of_element_located(
          (By.CSS_SELECTOR, ".alert.py-2.alert-danger#zip-code"))).value_of_css_property(css_attribute)
      return color