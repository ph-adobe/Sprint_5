from generator import *
from locators import Locators as L
from selenium.webdriver.common.by import By
from test_utils import TestUtils as tu


class TestRegistration:

    def test_registration_from_login_button(self, driver):
        user_name, email, valid_password = generate_registration_data()
        driver.find_element(By.XPATH, L.LOG_IN_BUTTON).click()
        tu.wait_for_loading(driver, L.ENTRY_HEADER)
        driver.find_element(By.XPATH, L.REGISTRATION_LINK).click()
        tu.wait_for_loading(driver, L.REGISTRATION_HEADER)
        tu.enter_registration_details(driver, user_name, email, valid_password)
        tu.wait_for_loading(driver, L.ENTRY_HEADER)
        assert "/login" in driver.current_url, f"Текущий url = {driver.current_url}"
        tu.check_log_in(driver, email, valid_password)
        assert "Оформить заказ" in driver.find_element(By.XPATH, L.MAKE_ORDER_BUTTON).text
        tu.log_out(driver)

    def test_registration_from_my_account_button(self, driver):
        user_name, email, valid_password = generate_registration_data()
        driver.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        tu.wait_for_loading(driver, L.ENTRY_HEADER)
        driver.find_element(By.XPATH, L.REGISTRATION_LINK).click()
        tu.wait_for_loading(driver, L.REGISTRATION_HEADER)
        tu.enter_registration_details(driver, user_name, email, valid_password)
        tu.wait_for_loading(driver, L.ENTRY_HEADER)

        assert "/login" in driver.current_url, f"Текущий url = {driver.current_url}"

        tu.check_log_in(driver, email, valid_password)
        assert "Оформить заказ" in driver.find_element(By.XPATH, L.MAKE_ORDER_BUTTON).text
        tu.log_out(driver)

    def test_incorrect_password(self, driver):
        user_name, email, valid_password = generate_registration_data()
        incorrect_password = "123"
        driver.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        tu.wait_for_loading(driver, L.ENTRY_HEADER)
        driver.find_element(By.XPATH, L.REGISTRATION_LINK).click()
        tu.wait_for_loading(driver, L.REGISTRATION_HEADER)
        tu.enter_registration_details(driver, user_name, email, incorrect_password)
        assert driver.find_element(By.XPATH, L.INCORRECT_PASSWORD_MESSAGE)
