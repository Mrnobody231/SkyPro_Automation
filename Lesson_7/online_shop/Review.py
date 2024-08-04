from selenium.webdriver.common.by import By

class Review:

    def __init__(self,driver):
        self.chrome = driver
        self.chrome.get("https://www.saucedemo.com/checkout-step-two.html")
        self.chrome.maximize_window()

    def total_price(self):
        self.chrome.find_element(By.CSS_SELECTOR, ".summary_total_label")
        total_amount = self.chrome.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        return total_amount