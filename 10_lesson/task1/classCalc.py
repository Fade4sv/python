import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainCalcs:
    def __init__(self, driver: WebDriver) -> None:
        self._driver: WebDriver = driver
        self._driver.maximize_window()
        self._driver.implicitly_wait(10)
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Установка задержки в {delay_value} секунд")
    def delay_taming(self, delay_value: str = "45") -> None:
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(delay_value)

    @allure.step("Выполнение математического вычисления: 7 + 8 =")
    def calculate(self) -> None:
        self._driver.find_element(By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(By.XPATH, "//span[text()='+' ]").click()
        self._driver.find_element(By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(By.XPATH, "//span[text()='=']").click()

    @allure.step("Проверка и ожидание результата вычисления")
    def assert_result(self, expected_text: str = "15") -> str:
        waiter = WebDriverWait(self._driver, 50)
        waiter.until(
            EC.text_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), expected_text
            )
        )
        return self._driver.find_element(By.CSS_SELECTOR, ".screen").text
