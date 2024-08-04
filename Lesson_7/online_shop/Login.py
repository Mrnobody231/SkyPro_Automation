from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.chrome = driver
        self.chrome.get("https://www.saucedemo.com/") 
        self.chrome.maximize_window()


    def login_locators(self, user_name, password):
        self.chrome.find_element(By.ID, "user-name").send_keys(user_name)
        self.chrome.find_element(By.ID, "password").send_keys(password)


    def click_button(self):
        self.chrome.find_element(By.ID, "login-button").click()