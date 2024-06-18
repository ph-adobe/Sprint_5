import pytest
from test_utils import *


@pytest.mark.parametrize(
    "css_selector",
    [
        pytest.param("div li:nth-child(1) p", id="Constructor button"),
        pytest.param("div svg", id="Logo"),
    ],
)
def test_go_to_constructor_from_my_account_logged_in(css_selector: str, login_data):
    login_email, login_password = login_data
    if not logged_in():
        log_in(login_email, login_password)
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    wait_for_loading(".//li[1]/a[@href='/account/profile']")
    driver.find_element(By.CSS_SELECTOR, css_selector).click()
    assert driver.find_element(By.XPATH, ".//h1[text()='Соберите бургер']")


@pytest.mark.parametrize(
    "css_selector",
    [
        pytest.param("div li:nth-child(1) p", id="Constructor button"),
        pytest.param("div svg", id="Logo"),
    ],
)
def test_go_to_constructor_from_my_account_not_logged_in(css_selector: str):
    if logged_in():
        log_out()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    driver.find_element(By.CSS_SELECTOR, css_selector).click()
    assert driver.find_element(By.XPATH, ".//h1[text()='Соберите бургер']")


def test_click_on_buns():
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
    driver.find_element(By.XPATH, "//span[text()='Булки']").click()
    header = driver.find_element(By.XPATH, "//h2[1]")
    assert header.text == "Булки"


def test_click_on_sauce():
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
    header = driver.find_element(By.XPATH, "//h2[2]")
    assert header.text == "Соусы"


def test_click_on_filling():
    driver.get("https://stellarburgers.nomoreparties.site/")
    ingredient = driver.find_element(By.XPATH, "//span[text()='Начинки']")
    ingredient.click()
    header = driver.find_element(By.XPATH, "//h2[3]")
    assert header.text == "Начинки"


# def test_scroll_ingredients():
#     driver.start_client()
#     driver.get("https://stellarburgers.nomoreparties.site/")
#     driver.refresh()
#     wait_for_loading(".//h1[text()='Соберите бургер']")
#     element = driver.find_element(By.XPATH, "//section[1]/div[2]/ul[3]/a[last()]/p")
#     driver.execute_script("arguments[0].scrollIntoView();", element)
#     assert element
#
