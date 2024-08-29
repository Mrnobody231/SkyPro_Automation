from selenium import webdriver
import allure

from .MainCalculator import MainCalculator

@allure.epic("Calculator")
@allure.severity("Critical")
@allure.title("Counting")
@allure.description("By using calculator count all integers together")
@allure.feature("Count")
def test_calculator():
    with allure.step("Initialize Chrome driver"):
        driver = webdriver.Chrome()
    with allure.step("Create MainCalculator's class object"):
        calculator = MainCalculator(driver)
    calculator.set_timer(45)
    calculator.insert_integers()
    result = calculator.get_result(47, '15')
    with allure.step("Check if result is the same as we wrote in parameter 'result'"):
        assert result == '15'