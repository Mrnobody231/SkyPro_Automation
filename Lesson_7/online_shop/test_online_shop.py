from selenium import webdriver

from online_shop.Login import Login
from online_shop.MainPage import MainPage
from online_shop.Cart import Cart
from online_shop.PersonalInfo import PersonalInfo
from online_shop.Review import Review

def test_total_amount():
    driver = webdriver.Chrome()

    login = Login(driver)
    login.login_locators("standard_user", "secret_sauce")
    login.click_button()

    main_page = MainPage(driver)
    main_page.select_items(2)

    cart = Cart(driver)
    cart.click_cart()
    cart.click_checkout()

    personal = PersonalInfo(driver)
    personal.add_personal_data("Edgar", "Andruskevic", "123456")
    personal.click_continue()

    review = Review(driver)
    price = review.total_price()

    assert price == "Total: $58.29"

    driver.quit()