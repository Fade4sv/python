from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
input_field = driver.find_element(By.CSS_SELECTOR, "#username")
input_field.send_keys("tomsmith")
sleep(2)
input_field = driver.find_element(By.CSS_SELECTOR, "#password")
input_field.send_keys("SuperSecretPassword!")
sleep(2)
input_field = driver.find_element(By.CSS_SELECTOR, ".fa.fa-2x")
input_field.click()
sleep(2)
driver.quit()
