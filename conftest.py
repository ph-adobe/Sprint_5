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


@pytest.fixture()
def login_data(driver):

    name, login_email, login_password = generate_registration_data()

    driver.find_element(By.XPATH, L.LOG_IN_BUTTON).click()
    tu.wait_for_loading(driver, L.ENTRY_HEADER)

    driver.find_element(By.XPATH, L.REGISTRATION_LINK).click()
    tu.wait_for_loading(driver, L.REGISTRATION_HEADER)

    tu.enter_registration_details(driver, name, login_email, login_password)
    tu.wait_for_loading(driver, L.ENTRY_HEADER)

    return login_email, login_password
