from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    def __init__(self,driver):
        self.chrome = driver
        self.chrome.get("https://www.saucedemo.com/inventory.html") 
        self.chrome.maximize_window()

    
    def select_items(self, wait_time):
        WebDriverWait(self.chrome, wait_time).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        self.chrome.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.chrome.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()