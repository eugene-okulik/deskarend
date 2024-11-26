from test_UI_magneto.locators.sing_in_locators import SignInLocators
from test_UI_magneto.pages.base_page import BasePage


class SignInPage(BasePage):
    def check_is_this_sign_in_page(self):
        self.check_page_title(SignInLocators.TITLE)
