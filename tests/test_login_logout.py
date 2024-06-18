from test_utils import *


def test_log_in_login_button(login_data):
    login_email, login_password = login_data
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    wait_for_loading(".//h2[text()='Вход']")
    check_log_in(login_email, login_password)

    assert (
        "Оформить заказ" in driver.find_element(By.XPATH, ".//section[2]//button").text
    )
    log_out()


def test_log_in_my_account_button(login_data):
    login_email, login_password = login_data
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    wait_for_loading(".//h2[text()='Вход']")
    check_log_in(login_email, login_password)
    assert (
        "Оформить заказ" in driver.find_element(By.XPATH, ".//section[2]//button").text
    )
    log_out()


def test_log_in_registration_form(login_data):
    login_email, login_password = login_data
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    wait_for_loading(".//h2[text()='Вход']")
    driver.find_element(By.XPATH, "//p[1]/a[@href='/register']").click()
    wait_for_loading(".//h2[text()='Регистрация']")
    driver.find_element(By.XPATH, ".//a[@href='/login']").click()
    wait_for_loading(".//h2[text()='Вход']")
    check_log_in(login_email, login_password)
    assert (
        "Оформить заказ" in driver.find_element(By.XPATH, ".//section[2]//button").text
    )
    log_out()


def test_log_in_restore_password_form(login_data):
    login_email, login_password = login_data
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    wait_for_loading(".//h2[text()='Вход']")
    driver.find_element(By.XPATH, "//p[2]/a[@href='/forgot-password']").click()
    wait_for_loading(".//h2[text()='Восстановление пароля']")
    driver.find_element(By.XPATH, ".//a[@href='/login']").click()
    wait_for_loading(".//h2[text()='Вход']")
    check_log_in(login_email, login_password)
    assert (
        "Оформить заказ" in driver.find_element(By.XPATH, ".//section[2]//button").text
    )
    log_out()


def test_log_out(login_data):
    login_email, login_password = login_data
    log_in(login_email, login_password)
    log_out()
    assert "/login" in driver.current_url



