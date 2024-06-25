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
    def test_go_to_my_account_from_different_pages_logged_in(self, driver_scope_module, path, login_data):
        login_email, login_password = login_data
        tu.log_in(driver_scope_module, login_email, login_password)
        driver_scope_module.get(path)
        driver_scope_module.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        tu.wait_for_loading(driver_scope_module, L.PROFILE_HEADER)
        assert driver_scope_module.find_element(By.XPATH, L.PROFILE_USER_EMAIL)
        tu.log_out(driver_scope_module)

    @pytest.mark.parametrize(
        "path",
        [
            MAIN_PAGE_URL,
            FEED_PAGE_URL,
        ],
    )
    def test_go_to_my_account_from_different_pages_not_logged_in(self, driver_scope_module, path):
        driver_scope_module.get(path)
        driver_scope_module.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        assert driver_scope_module.find_element(By.XPATH, L.ENTRY_HEADER)

    @pytest.mark.parametrize(
        "xpath",
        [
            L.CONSTRUCTOR_BUTTON,
            L.LOGO,
        ],
    )
    def test_from_my_account_go_to_constructor_logged_in(self, driver_scope_module, xpath: str, login_data):
        login_email, login_password = login_data
        tu.log_in(driver_scope_module, login_email, login_password)
        driver_scope_module.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        tu.wait_for_loading(driver_scope_module, L.PROFILE_HEADER)
        driver_scope_module.find_element(By.XPATH, xpath).click()
        assert driver_scope_module.find_element(By.XPATH, L.MAKE_BURGER_HEADER)
        tu.log_out(driver_scope_module)

    @pytest.mark.parametrize(
        "xpath",
        [
            L.CONSTRUCTOR_BUTTON,
            L.LOGO,
        ],
    )
    def test_from_my_account_go_to_constructor_not_logged_in(self, driver_scope_module, xpath: str):
        driver_scope_module.find_element(By.XPATH, L.MY_ACCOUNT_BUTTON).click()
        driver_scope_module.find_element(By.XPATH, xpath).click()
        assert driver_scope_module.find_element(By.XPATH, L.MAKE_BURGER_HEADER)
