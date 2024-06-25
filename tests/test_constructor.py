from locators import Locators as L
from selenium.webdriver.common.by import By
from test_utils import TestUtils as tu



class TestConstructor:
    def test_scroll_ingredients(self, driver):
        tu.wait_for_loading(driver, L.MAKE_BURGER_HEADER)
        element = driver.find_element(By.XPATH, L.LAST_INGREDIENT)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        assert element

    def test_click_on_buns(self, driver):
        driver.find_element(By.XPATH, L.SAUCE_BUTTON).click()  # to make 'Булки' clickable
        driver.find_element(By.XPATH, L.BUNS_BUTTON).click()
        header = driver.find_element(By.XPATH, L.BUNS_HEADER)
        assert header.text == "Булки"

    def test_click_on_sauce(self, driver):
        driver.find_element(By.XPATH, L.SAUCE_BUTTON).click()
        header = driver.find_element(By.XPATH, L.SAUCE_HEADER)
        assert header.text == "Соусы"

    def test_click_on_filling(self, driver):
        ingredient = driver.find_element(By.XPATH, L.FILLING_BUTTON)
        ingredient.click()
        header = driver.find_element(By.XPATH, L.FILLING_HEADER)
        assert header.text == "Начинки"
