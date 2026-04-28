from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainCalcs:
    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.implicitly_wait(10)
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def delay_taming(self):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

    def calculate(self):
        self._driver.find_element(
            By.XPATH, "//span[text()='7']").click()
        self._driver.find_element(
            By.XPATH, "//span[text()='+']").click()
        self._driver.find_element(
            By.XPATH, "//span[text()='8']").click()
        self._driver.find_element(
            By.XPATH, "//span[text()='=']").click()

    def assert_result(self):
        waiter = WebDriverWait(self._driver, 50)
        waiter.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15")
        )
        return self._driver.find_element(By.CSS_SELECTOR, ".screen").text
