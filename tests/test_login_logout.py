from tests.test_utils import *
from tests.selectors import *


def test_log_in_login_button(login_data):
    login_email, login_password = login_data
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, LOG_IN_BUTTON).click()
    wait_for_loading(ENTRY_HEADER)
    check_log_in(login_email, login_password)

    assert (
            "Оформить заказ" in driver.find_element(By.XPATH, MAKE_ORDER_BUTTON).text
    )
    log_out()


def test_log_in_my_account_button(login_data):
    login_email, login_password = login_data
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, MY_ACCOUNT_BUTTON).click()
    wait_for_loading(ENTRY_HEADER)
    check_log_in(login_email, login_password)
    assert (
            "Оформить заказ" in driver.find_element(By.XPATH, MAKE_ORDER_BUTTON).text
    )
    log_out()


def test_log_in_registration_form(login_data):
    login_email, login_password = login_data
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, MY_ACCOUNT_BUTTON).click()
    wait_for_loading(ENTRY_HEADER)
    driver.find_element(By.XPATH, REGISTRATION_LINK).click()
    wait_for_loading(REGISTRATION_HEADER)
    driver.find_element(By.XPATH, LOG_IN_LINK).click()
    wait_for_loading(ENTRY_HEADER)
    check_log_in(login_email, login_password)
    assert (
            "Оформить заказ" in driver.find_element(By.XPATH, MAKE_ORDER_BUTTON).text
    )
    log_out()


def test_log_in_recover_password_form(login_data):
    login_email, login_password = login_data
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, MY_ACCOUNT_BUTTON).click()
    wait_for_loading(ENTRY_HEADER)
    driver.find_element(By.XPATH, RECOVER_PASSWORD_LINK).click()
    wait_for_loading(PASSWORD_RECOVERY_HEADER)
    driver.find_element(By.XPATH, LOG_IN_LINK).click()
    wait_for_loading(ENTRY_HEADER)
    check_log_in(login_email, login_password)
    assert (
            "Оформить заказ" in driver.find_element(By.XPATH, MAKE_ORDER_BUTTON).text
    )
    log_out()


def test_log_out(login_data):
    login_email, login_password = login_data
    log_in(login_email, login_password)
    log_out()
    assert "/login" in driver.current_url
