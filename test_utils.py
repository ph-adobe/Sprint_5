from locators import Locators as L
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


MAIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/"
FEED_PAGE_URL = "https://stellarburgers.nomoreparties.site/feed"


class TestUtils:
    @staticmethod
    def wait_for_loading(driver, xpath):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))

    @staticmethod
    def enter_registration_details(driver, name, email, password):
        driver.find_element(By.XPATH, L.INPUT_NAME).send_keys(name)
        driver.find_element(By.XPATH, L.INPUT_EMAIL).send_keys(email)
        driver.find_element(By.XPATH, L.INPUT_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, L.REGISTRATION_BUTTON).click()

    @staticmethod
    def check_log_in(driver, email, password):
        driver.find_element(By.XPATH, L.INPUT_EMAIL).send_keys(email)
        driver.find_element(By.XPATH, L.INPUT_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, L.ENTRY_BUTTON).click()
        TestUtils.wait_for_loading(driver, L.MAKE_BURGER_HEADER)

    @staticmethod
    def log_in(driver, email, password):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(By.XPATH, L.LOG_IN_BUTTON).click()
        TestUtils.wait_for_loading(driver, L.ENTRY_HEADER)
        driver.find_element(By.XPATH, L.INPUT_EMAIL).send_keys(email)
        driver.find_element(By.XPATH, L.INPUT_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, L.ENTRY_BUTTON).click()
        TestUtils.wait_for_loading(driver, L.MAKE_BURGER_HEADER)

    @staticmethod
    def log_out(driver):
        driver.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        TestUtils.wait_for_loading(driver, L.LOGOUT_BUTTON)
        driver.find_element(By.XPATH, L.LOGOUT_BUTTON).click()
        TestUtils.wait_for_loading(driver, L.ENTRY_HEADER)

