from selenium.webdriver.common.by import By


class MainShop:
    def __init__(self, driver):
        self._driver = driver
        self._driver.maximize_window()
        self._driver.implicitly_wait(10)
        self._driver.get(
            "https://www.saucedemo.com/")

    def input_data(self, username, password):
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(username)
        self._driver.find_element(
            By.CSS_SELECTOR, "#password").send_keys(password)

    def press_login(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "#login-button").click()

    def add_to_cart(self):
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    def checkout(self, name, surname, postal_code):
        self._driver.get("https://www.saucedemo.com/cart.html")
        self._driver.find_element(By.ID, "checkout").click()
        self._driver.find_element(By.ID, "first-name").send_keys(name)
        self._driver.find_element(By.ID, "last-name").send_keys(surname)
        self._driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self._driver.find_element(By.ID, "continue").click()

    def assert_total(self):
        total_text = self._driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
        return total_text
