from tests.test_utils import *
from tests.selectors import *


def test_registration_from_login_button(user_name, email, valid_password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, LOG_IN_BUTTON).click()
    wait_for_loading(ENTRY_HEADER)
    driver.find_element(By.XPATH, REGISTRATION_LINK).click()
    wait_for_loading(REGISTRATION_HEADER)
    enter_registration_details(user_name, email, valid_password)
    wait_for_loading(ENTRY_HEADER)
    assert "/login" in driver.current_url, f"Текущий url = {driver.current_url}"
    check_log_in(email, valid_password)
    assert "Оформить заказ" in driver.find_element(By.XPATH, MAKE_ORDER_BUTTON).text
    log_out()


def test_registration_from_my_account_button(user_name, email, valid_password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, MY_ACCOUNT_BUTTON).click()
    wait_for_loading(ENTRY_HEADER)
    driver.find_element(By.XPATH, REGISTRATION_LINK).click()
    wait_for_loading(REGISTRATION_HEADER)
    enter_registration_details(user_name, email, valid_password)
    wait_for_loading(ENTRY_HEADER)

    assert "/login" in driver.current_url, f"Текущий url = {driver.current_url}"

    check_log_in(email, valid_password)
    assert "Оформить заказ" in driver.find_element(By.XPATH, MAKE_ORDER_BUTTON).text
    log_out()


def test_incorrect_password(user_name, email):
    incorrect_password = "123"
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, MY_ACCOUNT_BUTTON).click()
    wait_for_loading(ENTRY_HEADER)
    driver.find_element(By.XPATH, REGISTRATION_LINK).click()
    wait_for_loading(REGISTRATION_HEADER)
    enter_registration_details(user_name, email, incorrect_password)
    assert driver.find_element(By.XPATH, INCORRECT_PASSWORD_MESSAGE)
    driver.quit()
