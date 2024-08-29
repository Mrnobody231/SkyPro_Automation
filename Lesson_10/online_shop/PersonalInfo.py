from selenium.webdriver.common.by import By
import allure


class PersonalInfo:
    def __init__(self, driver):
        self.chrome = driver
        self.chrome.get("https://www.saucedemo.com/checkout-step-one.html")
        self.chrome.maximize_window()

    @allure.step("Write first name, last name, zip code")
    def add_personal_data(self, first_name: str, last_name: str, zip_code: str):
        self.chrome.find_element(By.ID, "first-name").send_keys(first_name)
        self.chrome.find_element(By.ID, "last-name").send_keys(last_name)
        self.chrome.find_element(By.ID, "postal-code").send_keys(zip_code)

    @allure.step("Click on button 'continue'")
    def click_continue(self):
        self.chrome.find_element(By.ID, "continue").click()