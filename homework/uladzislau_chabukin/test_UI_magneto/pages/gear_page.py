from test_UI_magneto.locators.gear_page_locators import GearPageLocators
from test_UI_magneto.pages.base_page import BasePage


class GearPage(BasePage):
    def check_is_this_gear_page(self):
        self.check_page_title(GearPageLocators.TITLE)
