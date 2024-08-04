from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class MainCalculator:

    def __init__(self, driver):
        self.chrome = driver
        self.chrome.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html") 
        self.chrome.maximize_window()
        self.actions = ActionChains(self.chrome)


    def set_timer(self, time):
        self.chrome.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.actions.send_keys_to_element(self.chrome.find_element(By.CSS_SELECTOR, "#delay"), time)
        self.actions.perform()
        

    def insert_integers(self):
        self.actions.click(self.chrome.find_element(By.XPATH, "//span[@class='btn btn-outline-primary'and text()='7']"))
        self.actions.click(self.chrome.find_element(By.XPATH, "//span[@class='operator btn btn-outline-success'and text()='+']"))
        self.actions.click(self.chrome.find_element(By.XPATH, "//span[@class='btn btn-outline-primary'and text()='8']"))
        self.actions.click(self.chrome.find_element(By.XPATH, "//span[@class='btn btn-outline-warning'and text()='=']"))
        self.actions.perform()


    def get_result(self, wait_time, result):
        WebDriverWait(self.chrome, wait_time).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), result))
        text = self.chrome.find_element(By.CSS_SELECTOR, ".screen").text
        return text