from test_UI_magneto.locators.sale_page_locators import SalePageLocators
from test_UI_magneto.pages.base_page import BasePage


class SalePage(BasePage):
    page_url = 'https://magento.softwaretestingboard.com/sale.html'

    def click_on_button_women_deals(self):
        self.click_on_element(SalePageLocators.BUTTON_WOMEN_DEALS)

    def click_on_link_men_deals(self):
        self.click_on_element(SalePageLocators.LINK_MEN_DEALS)

    def click_on_link_luma_gear(self):
        self.click_on_element(SalePageLocators.LINK_LUMA_GEAR)

    def check_is_this_sale_page(self):
        self.check_page_title(SalePageLocators.TITLE)
