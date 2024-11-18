from selenium.webdriver.common.by import By


def test_submit(driver):
    url = "https://www.qa-practice.com/elements/input/simple"
    driver.get(url)

    field_submit_me = driver.find_element(By.ID, 'id_text_string')
    something_string = "something_string"

    field_submit_me.send_keys(something_string)
    field_submit_me.submit()

    field_inputted_text = driver.find_element(By.ID, 'result-text')

    print(field_inputted_text.text)
