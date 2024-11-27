from test_UI_magneto.locators.men_sale_locators import MenSaleLocators
from test_UI_magneto.pages.base_page import BasePage


class MenSalePage(BasePage):
    def check_is_this_men_sale_page(self):
        self.check_page_title(MenSaleLocators.TITLE)
