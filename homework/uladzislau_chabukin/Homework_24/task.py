import random

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_add_item(driver):
    url = 'https://www.demoblaze.com/index.html'
    driver.get(url)
    WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'card')))

    products = driver.find_elements(By.CLASS_NAME, 'hrefch')
    random_product = random.choice(products)
    random_product_name = random_product.text
    ActionChains(driver).key_down(Keys.CONTROL).click(random_product).key_up(Keys.CONTROL).perform()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    button_add_to_cart = (By.CLASS_NAME, 'btn-success')
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(button_add_to_cart))
    driver.find_element(*button_add_to_cart).click()

    alert = Alert(driver)
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.accept()

    driver.close()
    driver.switch_to.window(tabs[0])

    cart = driver.find_element(By.ID, 'cartur')
    cart.click()

    added_product = (By.CLASS_NAME, 'success')
    WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located(added_product))
    added_product_text = driver.find_element(*added_product).text

    assert random_product_name in added_product_text


def test_compare(driver):
    url = 'https://magento.softwaretestingboard.com/gear/bags.html'
    driver.get(url)

    products = (By.CSS_SELECTOR, 'li.product-item')
    WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located(products))

    products = driver.find_elements(*products)
    random_product = random.choice(products)
    random_product_name = random_product.find_element(By.TAG_NAME, 'strong').text

    compare = random_product.find_element(By.CLASS_NAME, 'tocompare')
    ActionChains(driver).move_to_element(random_product).move_to_element(compare).click().perform()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'compare-items')))
    compare_items_name = driver.find_element(By.CSS_SELECTOR, '#compare-items strong').text

    assert random_product_name == compare_items_name
