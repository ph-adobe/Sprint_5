import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests import generator
from tests.selectors import *


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
    driver.find_element(By.XPATH, LOG_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ENTRY_HEADER)))

    driver.find_element(By.XPATH, REGISTRATION_LINK).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, REGISTRATION_HEADER))
    )
    driver.find_element(By.XPATH, REGISTRATION_INPUT_NAME).send_keys(name)
    driver.find_element(By.XPATH, REGISTRATION_INPUT_EMAIL).send_keys(login_email)
    driver.find_element(By.XPATH, REGISTRATION_INPUT_PASSWORD).send_keys(login_password)
    driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ENTRY_HEADER))
    )
    return login_email, login_password
