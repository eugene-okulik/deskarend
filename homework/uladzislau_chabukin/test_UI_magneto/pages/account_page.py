from playwright.sync_api import expect

from test_UI_magneto.pages.base_page import BasePage
from test_UI_magneto.locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
    def check_is_this_account_page(self):
        expect(self.find_element(AccountPageLocators.TITLE_MY_ACCOUNT_TAB)).to_be_visible()

    def check_creating_new_account(self, creating_new_account_text):
        self.check_is_this_account_page()
        self.check_element_text(AccountPageLocators.SUCCESSFUL_CREATING_ALERT, creating_new_account_text)
