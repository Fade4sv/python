from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from classShop import MainShop


def test_shop_checkout():
    driver = webdriver.Firefox(service=FirefoxService
                               (GeckoDriverManager().install()))
    shop = MainShop(driver)
    shop.input_data("standard_user", "secret_sauce")
    shop.press_login()
    shop.add_to_cart()
    shop.checkout("Ivan", "Ivanov", "123456")
    assert "58.29" in shop.assert_total()
    driver.quit()
