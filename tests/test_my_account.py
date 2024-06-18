import pytest
from test_utils import *


@pytest.mark.parametrize(
    "path",
    [
        "https://stellarburgers.nomoreparties.site/",
        "https://stellarburgers.nomoreparties.site/feed",
    ],
)
def test_go_to_my_account_from_different_pages_logged_in(path, login_data):
    login_email, login_password = login_data
    if not logged_in():
        log_in(login_email, login_password)
    driver.get(path)
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    wait_for_loading(".//li[1]/a[@href='/account/profile']")
    assert (
        driver.find_element(
            By.XPATH, "//li[2][@class='Profile_profileListItem__2th0t mb-6']//input"
        ).get_attribute("value")
        == login_email
    )


@pytest.mark.parametrize(
    "path",
    [
        "https://stellarburgers.nomoreparties.site/",
        "https://stellarburgers.nomoreparties.site/feed",
    ],
)
def test_go_to_my_account_from_different_pages_not_logged_in(path):
    if logged_in():
        log_out()
    driver.get(path)
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    assert driver.find_element(By.XPATH, ".//h2[text()='Вход']")
