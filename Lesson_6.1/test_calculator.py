from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_sum_calculator():

    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    actions= ActionChains(chrome)

    chrome.find_element(By.CSS_SELECTOR, "#delay").clear()

    actions.send_keys_to_element(chrome.find_element(By.CSS_SELECTOR, "#delay"), "45")
    actions.click(chrome.find_element(By.XPATH, "//span[@class='btn btn-outline-primary'and text()='7']"))
    actions.click(chrome.find_element(By.XPATH, "//span[@class='operator btn btn-outline-success'and text()='+']"))
    actions.click(chrome.find_element(By.XPATH, "//span[@class='btn btn-outline-primary'and text()='8']"))
    actions.click(chrome.find_element(By.XPATH, "//span[@class='btn btn-outline-warning'and text()='=']"))
    actions.perform()
    
    WebDriverWait(chrome, 50).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
    text = chrome.find_element(By.CSS_SELECTOR, ".screen").text
    assert text == "15"
    
    chrome.quit()


