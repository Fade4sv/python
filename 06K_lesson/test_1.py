from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

def test_form_validation():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.implicitly_wait(10)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name, value in form_data.items():
        driver.find_element(By.NAME, name).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button.btn-outline-primary").click()

    zip_class = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert "alert-danger" in zip_class

    fields_to_check = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company"]

    for field in fields_to_check:
        field_class = driver.find_element(By.ID, field).get_attribute("class")
        assert "alert-success" in field_class
    driver.quit()
