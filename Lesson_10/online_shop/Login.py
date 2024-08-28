from selenium.webdriver.common.by import By
import allure


from SkyPro_Automation.Lesson_5.chrome_website.Форма_авторизации import username

@allure.epic("LogIn")
class Login:
    def __init__(self, driver):
        self.chrome = driver
        self.chrome.get("https://www.saucedemo.com/") 
        self.chrome.maximize_window()

    @allure.step("Write username and password")
    def login_locators(self, user_name: str, password: str):
        self.chrome.find_element(By.ID, "user-name").send_keys(user_name)
        self.chrome.find_element(By.ID, "password").send_keys(password)

    @allure.step("Click button Login")
    def click_button(self):
        self.chrome.find_element(By.ID, "login-button").click()