import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    # chrome_driver.minimize_window()
    return chrome_driver