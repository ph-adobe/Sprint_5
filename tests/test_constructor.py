from tests.test_utils import *
from tests.selectors import *


def test_scroll_ingredients():
    driver.get("https://stellarburgers.nomoreparties.site/")
    wait_for_loading(MAKE_BURGER_HEADER)
    element = driver.find_element(By.XPATH, LAST_INGREDIENT)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    assert element


def test_click_on_buns():
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, SAUCE_BUTTON).click()  # to make 'Булки' clickable
    driver.find_element(By.XPATH, BUNS_BUTTON).click()
    header = driver.find_element(By.XPATH, BUNS_HEADER)
    assert header.text == "Булки"


def test_click_on_sauce():
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(By.XPATH, SAUCE_BUTTON).click()
    header = driver.find_element(By.XPATH, SAUCE_HEADER)
    assert header.text == "Соусы"


def test_click_on_filling():
    driver.get("https://stellarburgers.nomoreparties.site/")
    ingredient = driver.find_element(By.XPATH, FILLING_BUTTON)
    ingredient.click()
    header = driver.find_element(By.XPATH, FILLING_HEADER)
    assert header.text == "Начинки"
