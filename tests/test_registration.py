from test_utils import *


def test_registration_from_login_button(user_name, email, valid_password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    wait_for_loading(".//h2[text()='Вход']")
    driver.find_element(By.XPATH, "//p[1]/a[@href='/register']").click()
    wait_for_loading(".//h2[text()='Регистрация']")
    enter_registration_details(user_name, email, valid_password)
    wait_for_loading(".//h2[text()='Вход']")
    assert "/login" in driver.current_url, f"Текущий url = {driver.current_url}"
    check_log_in(email, valid_password)
    assert (
        "Оформить заказ" in driver.find_element(By.XPATH, ".//section[2]//button").text
    )
    log_out()


def test_registration_from_my_account_button(user_name, email, valid_password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    wait_for_loading(".//h2[text()='Вход']")
    driver.find_element(By.XPATH, "//p[1]/a[@href='/register']").click()
    wait_for_loading(".//h2[text()='Регистрация']")
    enter_registration_details(user_name, email, valid_password)
    wait_for_loading(".//h2[text()='Вход']")

    assert "/login" in driver.current_url, f"Текущий url = {driver.current_url}"

    check_log_in(email, valid_password)
    assert (
        "Оформить заказ" in driver.find_element(By.XPATH, ".//section[2]//button").text
    )
    log_out()


def test_incorrect_password(user_name, email):
    incorrect_password = "123"
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    wait_for_loading(".//h2[text()='Вход']")
    driver.find_element(By.XPATH, "//p[1]/a[@href='/register']").click()
    wait_for_loading(".//h2[text()='Регистрация']")
    enter_registration_details(user_name, email, incorrect_password)
    assert driver.find_element(
        By.XPATH, ".//fieldset[3]//p[text()='Некорректный пароль']"
    )
    driver.quit()




