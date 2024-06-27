import pytest

from locators import Locators as L
from selenium.webdriver.common.by import By
from test_utils import TestUtils as tu, MAIN_PAGE_URL, FEED_PAGE_URL


class TestMyAccount:

    @pytest.mark.parametrize(
        "path",
        [
            MAIN_PAGE_URL,
            FEED_PAGE_URL,
        ],
    )
    def test_go_to_my_account_from_different_pages_logged_in(self, driver, path, login_data):
        login_email, login_password = login_data
        tu.log_in(driver, login_email, login_password)
        driver.get(path)
        driver.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        tu.wait_for_loading(driver, L.PROFILE_HEADER)
        assert driver.find_element(By.XPATH, L.PROFILE_USER_EMAIL)
        tu.log_out(driver)

    @pytest.mark.parametrize(
        "path",
        [
            MAIN_PAGE_URL,
            FEED_PAGE_URL,
        ],
    )
    def test_go_to_my_account_from_different_pages_not_logged_in(self, driver, path):
        driver.get(path)
        driver.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        assert driver.find_element(By.XPATH, L.ENTRY_HEADER)

    @pytest.mark.parametrize(
        "xpath",
        [
            L.CONSTRUCTOR_BUTTON,
            L.LOGO,
        ],
    )
    def test_from_my_account_go_to_constructor_logged_in(self, driver, xpath: str, login_data):
        login_email, login_password = login_data
        tu.log_in(driver, login_email, login_password)
        driver.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        tu.wait_for_loading(driver, L.PROFILE_HEADER)
        driver.find_element(By.XPATH, xpath).click()
        assert driver.find_element(By.XPATH, L.MAKE_BURGER_HEADER)
        tu.log_out(driver)

    @pytest.mark.parametrize(
        "xpath",
        [
            L.CONSTRUCTOR_BUTTON,
            L.LOGO,
        ],
    )
    def test_from_my_account_go_to_constructor_not_logged_in(self, driver, xpath: str):
        driver.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, xpath).click()
        assert driver.find_element(By.XPATH, L.MAKE_BURGER_HEADER)
