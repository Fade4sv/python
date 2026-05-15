from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://uitestingplayground.com/classattr")

search_locator = ".btn-primary"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.click()
