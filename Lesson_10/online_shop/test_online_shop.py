from selenium import webdriver
import allure


from .Login import Login
from .MainPage import MainPage
from .Cart import Cart
from .PersonalInfo import PersonalInfo
from .Review import Review

@allure.severity("Critical")
@allure.title("Shopping clothes")
@allure.description("Select 3 clothes to the cart and check for total amount")
@allure.feature("Get")
def test_total_amount():
    with allure.step("Initialize Chrome driver"):
        driver = webdriver.Chrome()
    with allure.step("Create Login's class object"):
        login = Login(driver)
    login.login_locators("standard_user", "secret_sauce")
    login.click_button()
    with allure.step("Create MainPage's class object"):
        main_page = MainPage(driver)
    main_page.select_items(2)
    with allure.step("Create Cart's class object"):
        cart = Cart(driver)
    cart.click_cart()
    cart.click_checkout()
    with allure.step("Create PersonalInfo's class object"):
        personal = PersonalInfo(driver)
    personal.add_personal_data("Edgar", "Andruskevic", "123456")
    personal.click_continue()
    with allure.step("Create Review's class object"):
        review = Review(driver)
    price = review.total_price()
    with allure.step("Check if price is $58.29"):
        assert price == "Total: $58.29"

    driver.quit()