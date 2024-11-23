import random

from faker import Faker
from playwright.sync_api import Page

fake = Faker()


def test_authorization(page: Page):
    url = 'https://the-internet.herokuapp.com/'
    page.goto(url)

    form_authentication = page.get_by_role('link', name='Form Authentication')
    form_authentication.click()

    username = page.get_by_role('textbox', name='username')
    username.fill(fake.user_name())

    password = page.get_by_role('textbox', name='password')
    password.fill(fake.password())

    button_login = page.get_by_role('button', name='Login')
    button_login.click()


def test_form(page: Page):
    url = 'https://demoqa.com/automation-practice-form'
    page.goto(url)

    field_first_name = page.get_by_placeholder('First Name')
    field_last_name = page.get_by_placeholder('Last Name')
    field_email_name = page.locator('#userEmail')
    fields_genders = page.locator('[for*="gender"]').all()
    field_mobile = page.get_by_placeholder('Mobile Number')
    field_birthday = page.locator('#dateOfBirthInput')
    field_subjects = page.locator('#subjectsInput')
    field_hobbies = page.locator('[for^="hobbies"]').all()
    field_address = page.get_by_placeholder('Current Address')
    field_state = page.locator('#state input')
    field_city = page.locator('#city input')
    button_submit = page.get_by_role('button', name='submit')

    field_first_name.fill(fake.first_name())
    field_last_name.fill(fake.last_name())
    field_email_name.fill(fake.email())

    random_gender = random.choice(fields_genders)
    random_gender.click()

    field_mobile.fill(str(random.randint(10_000_000_00, 99_999_999_99)))
    field_birthday.fill('11 Sep 1998')
    field_birthday.press('Enter')

    field_subjects.fill('Maths')
    field_subjects.press('Enter')

    random_hobby = random.choice(field_hobbies)
    random_hobby.check()

    field_address.fill(fake.address())

    field_state.fill('NCR')
    field_state.press('Enter')

    field_city.fill('Delhi')
    field_city.press('Enter')

    button_submit.click()
