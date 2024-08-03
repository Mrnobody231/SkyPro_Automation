from selenium import webdriver

from calculator.MainCalculator import MainCalculator

def test_calculator():
    driver = webdriver.Chrome()

    calculator = MainCalculator(driver)
    calculator.set_timer(45)
    calculator.insert_integers()
    result = calculator.get_result(47, '15')

    assert result == '15'