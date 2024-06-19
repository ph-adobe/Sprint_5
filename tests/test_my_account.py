import pytest
from tests.test_utils import *
from tests.selectors import *


@pytest.mark.parametrize(
    "path",
    [
        "https://stellarburgers.nomoreparties.site/",
        "https://stellarburgers.nomoreparties.site/feed",
    ],
)
def test_go_to_my_account_from_different_pages_logged_in(path, login_data):
    login_email, login_password = login_data
    if not logged_in():
        log_in(login_email, login_password)
    driver.get(path)
    driver.find_element(By.XPATH, MY_ACCOUNT_BUTTON).click()
    wait_for_loading(PROFILE_HEADER)
    assert driver.find_element(By.XPATH, PROFILE_USER_EMAIL).get_attribute("value") == login_email


@pytest.mark.parametrize(
    "path",
    [
        "https://stellarburgers.nomoreparties.site/",
        "https://stellarburgers.nomoreparties.site/feed",
    ],
)
def test_go_to_my_account_from_different_pages_not_logged_in(path):
    if logged_in():
        log_out()
    driver.get(path)
    driver.find_element(By.XPATH, MY_ACCOUNT_BUTTON).click()
    assert driver.find_element(By.XPATH, ENTRY_HEADER)


@pytest.mark.parametrize(
    "css_selector",
    [
        CONSTRUCTOR_BUTTON,
        LOGO,
    ],
)
def test_from_my_account_go_to_constructor_logged_in(css_selector: str, login_data):
    login_email, login_password = login_data
    if not logged_in():
        log_in(login_email, login_password)
    driver.find_element(By.XPATH, MY_ACCOUNT_BUTTON).click()
    wait_for_loading(PROFILE_HEADER)
    driver.find_element(By.CSS_SELECTOR, css_selector).click()
    assert driver.find_element(By.XPATH, MAKE_BURGER_HEADER)


@pytest.mark.parametrize(
    "css_selector",
    [
        CONSTRUCTOR_BUTTON,
        LOGO,
    ],
)
def test_from_my_account_go_to_constructor_not_logged_in(css_selector: str):
    if logged_in():
        log_out()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, MY_ACCOUNT_BUTTON).click()
    driver.find_element(By.CSS_SELECTOR, css_selector).click()
    assert driver.find_element(By.XPATH, MAKE_BURGER_HEADER)
