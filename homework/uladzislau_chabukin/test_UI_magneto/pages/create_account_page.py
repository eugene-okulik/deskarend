from test_UI_magneto.locators.create_account_locators import CreateAccountLocators
from test_UI_magneto.pages.base_page import BasePage


class CreateAccount(BasePage):
    page_url = 'https://magento.softwaretestingboard.com/customer/account/create/'

    def fill_first_name(self, f_name):
        self.fill_field(CreateAccountLocators.FIELD_FIRST_NAME, f_name)

    def fill_last_name(self, l_name):
        self.fill_field(CreateAccountLocators.FIELD_LAST_NAME, l_name)

    def fill_email(self, email):
        self.fill_field(CreateAccountLocators.FIELD_EMAIL, email)

    def fill_password(self, password):
        self.fill_field(CreateAccountLocators.FIELD_PASSWORD, password)

    def fill_confirm_password(self, password):
        self.fill_field(CreateAccountLocators.FIELD_CONFIRM_PASSWORD, password)

    def fill_form(self, f_name, l_name, email, password, confirm_password):
        self.fill_first_name(f_name)
        self.fill_last_name(l_name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_confirm_password(confirm_password)

    def click_create_account(self):
        self.click_on_element(CreateAccountLocators.BUTTON_CREATE_ACCOUNT)

    def create_account(self, f_name, l_name, email, password, confirm_password):
        self.fill_form(f_name, l_name, email, password, confirm_password)
        self.click_create_account()

    def check_is_there_email_error(self, email_error_text):
        self.check_element_text(CreateAccountLocators.EMAIL_ERROR, email_error_text)

    def check_is_there_confirm_error(self, confirm_password_error):
        self.check_element_text(CreateAccountLocators.CONFIRM_PASSWORD_ERROR, confirm_password_error)
