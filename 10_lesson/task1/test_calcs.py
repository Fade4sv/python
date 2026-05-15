import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from classCalc import MainCalcs


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@allure.feature("Калькулятор с задержкой вычислений")
@allure.title("Проверка сложения чисел 7 и 8")
@allure.description("Тест проверяет корректность работы slow-calculator при сложении чисел с установленной задержкой.")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(driver) -> None:
    calc = MainCalcs(driver)

    calc.delay_taming()
    calc.calculate()

    with allure.step("Финальная проверка: полученный результат равен '15'"):
        result: str = calc.assert_result()
        assert result == "15", f"Ожидалось '15', но калькулятор показал '{result}'"
