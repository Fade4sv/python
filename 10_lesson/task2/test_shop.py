import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from classShop import MainShop

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()

@allure.feature("Оформление заказа в интернет-магазине")
@allure.title("Проверка полной стоимости корзины при покупке нескольких товаров")
@allure.description("Тест авторизует пользователя, добавляет товары в корзину, заполняет данные формы и проверяет итоговую сумму заказа.")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_checkout(driver) -> None:
    shop = MainShop(driver)
    shop.input_data("standard_user", "secret_sauce")
    shop.press_login()
    shop.add_to_cart()
    shop.checkout("Ivan", "Ivanov", "123456")
    with allure.step("Финальная проверка: итоговая сумма содержит '58.29'"):
        total_price: str = shop.assert_total()
        assert "58.29" in total_price, f"Ожидалась сумма '58.29', но получено: '{total_price}'"
