from playwright.sync_api import expect

from test_UI_magneto.locators.item_page_locators import ItemPageLocators
from test_UI_magneto.pages.base_page import BasePage


class ProductPage(BasePage):
    def check_product_page_name(self, product_name):
        expect(self.find_element(ItemPageLocators.ITEM_NAME)).to_have_text(product_name)
