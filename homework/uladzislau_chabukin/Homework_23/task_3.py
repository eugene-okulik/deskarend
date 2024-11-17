from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_choose_language(driver):
    url = "https://www.qa-practice.com/elements/select/single_select"
    txt = 'Python'

    driver.get(url)
    field_languages = driver.find_element(By.ID, 'id_choose_language')
    select = Select(field_languages)
    select.select_by_visible_text(txt)

    button_submit = driver.find_element(By.ID, 'submit-id-submit')
    button_submit.click()
    field_chose_language = driver.find_element(By.ID, 'result-text')

    assert field_chose_language.text == txt


def test_check_text(driver):
    url = 'https://the-internet.herokuapp.com/dynamic_loading/2'
    wait = WebDriverWait(driver, 5)

    driver.get(url)

    button_start = driver.find_element(By.CSS_SELECTOR, '#start > button')
    button_start.click()

    greeting_text_selector = (By.ID, 'finish')
    wait.until(EC.visibility_of_element_located(greeting_text_selector))

    greeting_text = driver.find_element(By.ID, 'finish').text
    assert greeting_text == 'Hello World!'
