import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class MainShop:
    def __init__(self, driver: WebDriver) -> None:
        self._driver: WebDriver = driver
        self._driver.maximize_window()
        self._driver.implicitly_wait(10)
        self._driver.get("https://www.saucedemo.com/")

    @allure.step("Ввод учетных данных: логин '{username}'")
    def input_data(self, username: str, password: str) -> None:
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(username)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)

    @allure.step("Нажатие на кнопку входа")
    def press_login(self) -> None:
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self) -> None:
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переход в корзину и заполнение данных клиента: {name} {surname}")
    def checkout(self, name: str, surname: str, postal_code: str) -> None:
        self._driver.get("https://www.saucedemo.com/cart.html")
        self._driver.find_element(By.ID, "checkout").click()
        self._driver.find_element(By.ID, "first-name").send_keys(name)
        self._driver.find_element(By.ID, "last-name").send_keys(surname)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self._driver.find_element(By.ID, "continue").click()

    @allure.step("Получение итоговой суммы заказа")
    def assert_total(self) -> str:
        total_text: str = self._driver.find_element(By.CLASS_NAME, "summary_total_label").text
        return total_text
