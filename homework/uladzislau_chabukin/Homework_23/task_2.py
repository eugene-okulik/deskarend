import random

from faker import Faker
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

fake = Faker('')


def test_form(driver):
    url = "https://demoqa.com/automation-practice-form"
    driver.get(url)

    field_first_name = driver.find_element(By.ID, 'firstName')
    field_last_name = driver.find_element(By.ID, 'lastName')
    field_email_name = driver.find_element(By.ID, 'userEmail')
    fields_genders = driver.find_elements(By.CSS_SELECTOR, '[for^="gender"]')
    field_mobile = driver.find_element(By.ID, 'userNumber')
    field_birthday = driver.find_element(By.ID, 'dateOfBirthInput')
    field_subjects = driver.find_element(By.ID, 'subjectsInput')
    field_hobbies = driver.find_elements(By.CSS_SELECTOR, '[for^="hobbies"]')
    field_address = driver.find_element(By.ID, 'currentAddress')
    field_state = driver.find_element(By.CSS_SELECTOR, '#state input')
    field_city = driver.find_element(By.CSS_SELECTOR, '#city input')
    button_submit = driver.find_element(By.ID, 'submit')

    field_first_name.send_keys(fake.first_name())
    field_last_name.send_keys(fake.last_name())
    field_email_name.send_keys(fake.email())

    random_gender = random.choice(fields_genders)
    random_gender.click()

    field_mobile.send_keys(random.randint(10_000_000_00, 99_999_999_99))
    field_birthday.send_keys('11 Sep 1998')
    field_birthday.send_keys(Keys.ENTER)

    field_subjects.send_keys('Maths')
    field_subjects.send_keys(Keys.ENTER)

    random_hobby = random.choice(field_hobbies)
    random_hobby.click()

    field_address.send_keys(fake.address())

    field_state.send_keys('NCR')
    field_state.send_keys(Keys.ENTER)

    field_city.send_keys('Delhi')
    field_city.send_keys(Keys.ENTER)

    button_submit.click()

    result_form = driver.find_elements(By.TAG_NAME, 'tbody')

    for element in result_form:
        print(element.text)
