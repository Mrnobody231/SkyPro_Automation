from selenium.webdriver.common.by import By

class Cart:

    def __init__(self,driver):
        self.chrome = driver
        self.chrome.get("https://www.saucedemo.com/cart.html")
        self.chrome.maximize_window()

    def click_cart(self):
        self.chrome.find_element(By.CSS_SELECTOR,".shopping_cart_link").click()

    def click_checkout(self):
        self.chrome.find_element(By.ID, "checkout").click()