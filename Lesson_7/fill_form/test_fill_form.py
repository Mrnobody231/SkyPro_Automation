from selenium import webdriver

from .MainPage import MainPage

def test_personal_form():
    driver = webdriver.Chrome()
    
    main_page = MainPage(driver)
    data = main_page.form_data()
    main_page.fill_form_with_data(data)
    main_page.click_button()
    color_is_green =  main_page.field_is_not_empty(2, "background-color")
    color_is_red = main_page.field_is_empty(2, "background-color")

    assert color_is_green == "rgba(209, 231, 221, 1)"
    assert color_is_red == "rgba(248, 215, 218, 1)"

    driver.quit()