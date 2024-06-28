from locators import Locators as L
from selenium.webdriver.common.by import By
from test_utils import TestUtils as tu, MAIN_PAGE_URL


class TestLoginLogout:

    def test_log_in_login_button(self, driver, login_data):
        login_email, login_password = login_data
        driver.get(MAIN_PAGE_URL)
        driver.find_element(By.XPATH, L.LOG_IN_BUTTON).click()
        tu.wait_for_loading(driver, L.ENTRY_HEADER)
        tu.check_log_in(driver, login_email, login_password)

        assert (
                "Оформить заказ" in driver.find_element(By.XPATH, L.MAKE_ORDER_BUTTON).text
        )
        tu.log_out(driver)

    def test_log_in_my_account_button(self, driver, login_data):
        login_email, login_password = login_data
        driver.get(MAIN_PAGE_URL)
        driver.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        tu.wait_for_loading(driver, L.ENTRY_HEADER)
        tu.check_log_in(driver, login_email, login_password)
        assert (
                "Оформить заказ" in driver.find_element(By.XPATH, L.MAKE_ORDER_BUTTON).text
        )
        tu.log_out(driver)

    def test_log_in_registration_form(self, driver, login_data):
        login_email, login_password = login_data
        driver.get(MAIN_PAGE_URL)
        driver.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        tu.wait_for_loading(driver, L.ENTRY_HEADER)
        driver.find_element(By.XPATH, L.REGISTRATION_LINK).click()
        tu.wait_for_loading(driver, L.REGISTRATION_HEADER)
        driver.find_element(By.XPATH, L.LOG_IN_LINK).click()
        tu.wait_for_loading(driver, L.ENTRY_HEADER)
        tu.check_log_in(driver, login_email, login_password)
        assert (
                "Оформить заказ" in driver.find_element(By.XPATH, L.MAKE_ORDER_BUTTON).text
        )
        tu.log_out(driver)

    def test_log_in_recover_password_form(self, driver, login_data):
        login_email, login_password = login_data
        driver.get(MAIN_PAGE_URL)
        driver.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        tu.wait_for_loading(driver, L.ENTRY_HEADER)
        driver.find_element(By.XPATH, L.RECOVER_PASSWORD_LINK).click()
        tu.wait_for_loading(driver, L.PASSWORD_RECOVERY_HEADER)
        driver.find_element(By.XPATH, L.LOG_IN_LINK).click()
        tu.wait_for_loading(driver, L.ENTRY_HEADER)
        tu.check_log_in(driver, login_email, login_password)
        assert (
                "Оформить заказ" in driver.find_element(By.XPATH, L.MAKE_ORDER_BUTTON).text
        )
        tu.log_out(driver)

    def test_log_out(self, driver, login_data):
        login_email, login_password = login_data
        driver.get(MAIN_PAGE_URL)
        tu.log_in(driver, login_email, login_password)
        tu.log_out(driver)
        assert "/login" in driver.current_url
