from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.selectors import *

driver = webdriver.Chrome()


def wait_for_loading(xpath):
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))


def enter_registration_details(name, email, password):
    driver.find_element(By.XPATH, REGISTRATION_INPUT_NAME).send_keys(name)
    driver.find_element(By.XPATH, REGISTRATION_INPUT_EMAIL).send_keys(email)
    driver.find_element(By.XPATH, REGISTRATION_INPUT_PASSWORD).send_keys(password)
    driver.find_element(By.XPATH, REGISTRATION_BUTTON).click()


def check_log_in(email, password):
    driver.find_element(By.XPATH, ENTRY_INPUT_LOGIN).send_keys(email)
    driver.find_element(By.XPATH, ENTRY_INPUT_PASSWORD).send_keys(password)
    driver.find_element(By.XPATH, ENTRY_BUTTON).click()
    wait_for_loading(MAKE_BURGER_HEADER)


def log_in(email, password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, LOG_IN_BUTTON).click()
    wait_for_loading(ENTRY_HEADER)
    driver.find_element(By.XPATH, ENTRY_INPUT_LOGIN).send_keys(email)
    driver.find_element(By.XPATH, ENTRY_INPUT_PASSWORD).send_keys(password)
    driver.find_element(By.XPATH, ENTRY_BUTTON).click()
    wait_for_loading(MAKE_BURGER_HEADER)


def logged_in():
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, MY_ACCOUNT_BUTTON).click()
    return "/profile" in driver.current_url


def log_out():
    driver.find_element(By.XPATH, MY_ACCOUNT_BUTTON).click()
    wait_for_loading(LOGOUT_BUTTON)
    driver.find_element(By.XPATH, LOGOUT_BUTTON).click()
    wait_for_loading(ENTRY_HEADER)
