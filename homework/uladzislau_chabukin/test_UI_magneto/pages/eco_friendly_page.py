import random

from test_UI_magneto.locators.eco_friendly_page_locators import EcoFriendlyPageLocators
from test_UI_magneto.pages.base_page import BasePage


class EcoFriendlyPage(BasePage):
    page_url = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

    def click_on_sale_link(self):
        self.click_on_element(EcoFriendlyPageLocators.LINK_SALE)

    def click_random_product(self):
        products = self.find_elements(EcoFriendlyPageLocators.PRODUCTS_NAMES)
        random_product = random.choice(products)
        self.random_product_name = random_product.inner_text()
        random_product.click()

    def get_random_product_name(self):
        return self.random_product_name

    def click_on_sign_in_link(self):
        self.find_element(EcoFriendlyPageLocators.AUTHORIZATION_LINK).click()
