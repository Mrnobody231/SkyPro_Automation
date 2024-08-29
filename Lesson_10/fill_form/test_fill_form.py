from selenium import webdriver
import allure

from .MainPage import MainPage

@allure.epic("Fill the form")
@allure.severity("Critical")
@allure.title("Get color by css_attribute")
@allure.description("Check fields color when they are empty and not")
@allure.feature("Get")
def test_personal_form():
    with allure.step("Initialize Chrome driver"):
        driver = webdriver.Chrome()
    with allure.step("Create MainPage's class object"):
        main_page = MainPage(driver)
    data = main_page.form_data()
    main_page.fill_form_with_data(data)
    main_page.click_button()
    color_is_green =  main_page.field_is_not_empty(2, "background-color")
    color_is_red = main_page.field_is_empty(2, "background-color")
    with allure.step("Check if color is green"):
        assert color_is_green == "rgba(209, 231, 221, 1)"
    with allure.step("Check if color is red"):
        assert color_is_red == "rgba(248, 215, 218, 1)"

    driver.quit()