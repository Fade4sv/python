from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from classCalc import MainCalcs


def test_slow_calculator():
    driver = webdriver.Chrome(service=ChromeService
                              (ChromeDriverManager().install()))
    calc = MainCalcs(driver)
    calc.delay_taming()
    calc.calculate()
    result = calc.assert_result()
    assert result == "15"
    driver.quit()
