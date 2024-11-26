import pytest
from faker import Faker
from playwright.sync_api import BrowserContext

from test_UI_magneto.pages.account_page import AccountPage
from test_UI_magneto.pages.create_account_page import CreateAccount
from test_UI_magneto.pages.eco_friendly_page import EcoFriendlyPage
from test_UI_magneto.pages.gear_page import GearPage
from test_UI_magneto.pages.men_sale_page import MenSalePage
from test_UI_magneto.pages.product_page import ProductPage
from test_UI_magneto.pages.sale_page import SalePage
from test_UI_magneto.pages.sign_in_page import SignInPage
from test_UI_magneto.pages.women_sale_page import WomenSalePage

fake = Faker()


@pytest.fixture
def page(context: BrowserContext):
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture
def create_account(page):
    return CreateAccount(page)


@pytest.fixture
def account_page(page):
    return AccountPage(page)


@pytest.fixture
def eco_friendly_page(page):
    return EcoFriendlyPage(page)


@pytest.fixture
def sale_page(page):
    return SalePage(page)


@pytest.fixture
def product_page(page):
    return ProductPage(page)


@pytest.fixture
def sing_in_page(page):
    return SignInPage(page)


@pytest.fixture
def women_sale_page(page):
    return WomenSalePage(page)


@pytest.fixture
def men_sale_page(page):
    return MenSalePage(page)


@pytest.fixture
def gear_page(page):
    return GearPage(page)


@pytest.fixture
def first_name():
    return fake.first_name()


@pytest.fixture
def last_name():
    return fake.last_name()


@pytest.fixture
def email():
    return fake.email()


@pytest.fixture
def password():
    return fake.password()
