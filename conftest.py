import pytest

from generator import *
from locators import Locators as L
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_utils import TestUtils as tu, MAIN_PAGE_URL


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get(MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def driver_scope_module():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver_scope_module = webdriver.Chrome(options=options)
    driver_scope_module.get(MAIN_PAGE_URL)
    yield driver_scope_module
    driver_scope_module.quit()


@pytest.fixture(scope="module")
def login_data(driver_scope_module):
    """
    Данная фикстура позволяет получить логин и пароль только что зарегистрированного пользователя.
    Данные используются для всех тестов в модулях test_login_logout.py, test_my_account.py.
    :param driver_scope_module: Для такой фикстуры необходим отдельный инстанс driver с таким же scope.
    :return:
   """
    name, login_email, login_password = generate_registration_data()

    driver_scope_module.find_element(By.XPATH, L.LOG_IN_BUTTON).click()
    tu.wait_for_loading(driver_scope_module, L.ENTRY_HEADER)

    driver_scope_module.find_element(By.XPATH, L.REGISTRATION_LINK).click()
    tu.wait_for_loading(driver_scope_module, L.REGISTRATION_HEADER)

    tu.enter_registration_details(driver_scope_module, name, login_email, login_password)
    tu.wait_for_loading(driver_scope_module, L.ENTRY_HEADER)

    return login_email, login_password
