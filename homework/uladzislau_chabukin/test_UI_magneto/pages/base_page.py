from playwright.sync_api import Page, expect, Locator


class BasePage:
    page_url = None

    random_product_name = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        self.page.goto(self.page_url)

    def find_element(self, element) -> Locator:
        return self.page.locator(element).first

    def find_elements(self, element):
        return self.page.locator(element).all()

    def click_on_element(self, element):
        return self.page.locator(element).click()

    def fill_field(self, element, value):
        self.page.locator(element).fill(value)

        expect(self.find_element(element)).to_have_value(value)

    def check_element_text(self, element, text):
        expect(self.find_element(element)).to_have_text(text)

    def check_page_title(self, page_title_locator):
        expect(self.find_element(page_title_locator)).to_be_visible()
