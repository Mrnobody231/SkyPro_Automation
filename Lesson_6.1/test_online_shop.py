from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.test_shop_buying
def test_shop():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get("https://www.saucedemo.com/")
    
    chrome.find_element(By.ID, "user-name").send_keys("standard_user")
    chrome.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome.find_element(By.ID, "login-button").click()
    
    WebDriverWait(chrome, 3).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    chrome.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    chrome.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    chrome.find_element(By.CSS_SELECTOR,".shopping_cart_link").click()
    chrome.find_element(By.ID, "checkout").click()

    chrome.find_element(By.ID, "first-name").send_keys("Edgar")
    chrome.find_element(By.ID, "last-name").send_keys("Andruskevic")
    chrome.find_element(By.ID, "postal-code").send_keys("412541")
    chrome.find_element(By.ID, "continue").click()

    chrome.find_element(By.CSS_SELECTOR, ".summary_total_label")
    total_amount = chrome.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    assert total_amount == "Total: $58.29"
    
    
