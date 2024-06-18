from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Chrome()


def wait_for_loading(xpath):
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, xpath))
    )


def enter_registration_details(name, email, password):
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(name)
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(email)
    driver.find_element(By.XPATH, ".//fieldset[3]//input").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()


def check_log_in(email, password):
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(email)
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    wait_for_loading(".//h1[text()='Соберите бургер']")


def log_in(email, password):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
    wait_for_loading(".//h2[text()='Вход']")
    driver.find_element(By.XPATH, ".//fieldset[1]//input").send_keys(email)
    driver.find_element(By.XPATH, ".//fieldset[2]//input").send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
    wait_for_loading(".//h1[text()='Соберите бургер']")


def logged_in():
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    return "/profile" in driver.current_url


def log_out():
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    wait_for_loading(".//li[3]/button[text()='Выход']")
    driver.find_element(By.XPATH, ".//li[3]/button[text()='Выход']").click()
    wait_for_loading(".//h2[text()='Вход']")

