import pytest
import generator
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture
def user_name():
    return generator.generate_name()


@pytest.fixture
def email(user_name):
    return generator.generate_email(user_name)


@pytest.fixture
def valid_password():
    return generator.generate_password()


@pytest.fixture(scope="module")
def login_data():
    name = generator.generate_name()
    login_email = generator.generate_email(name)
    login_password = generator.generate_password()

    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//h2[text()='Вход']")
        )
    )

    driver.find_element(By.XPATH, "//p[1]/a[@href='/register']").click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//h2[text()='Регистрация']")
        )
    )
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(name)
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(login_email)
    driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys(login_password)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, ".//h2[text()='Вход']")
        )
    )

    return login_email, login_password
