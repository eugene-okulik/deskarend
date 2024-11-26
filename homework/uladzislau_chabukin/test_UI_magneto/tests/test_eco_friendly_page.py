def test_click_on_sale_link(eco_friendly_page, sale_page):
    eco_friendly_page.open_page()

    eco_friendly_page.click_on_sale_link()

    sale_page.check_is_this_sale_page()


def test_click_on_random_product(eco_friendly_page, product_page):
    eco_friendly_page.open_page()

    eco_friendly_page.click_random_product()
    product_name = eco_friendly_page.get_random_product_name()

    product_page.check_product_page_name(product_name)


def test_click_on_sing_in_link(eco_friendly_page, sing_in_page):
    eco_friendly_page.open_page()

    eco_friendly_page.click_on_sign_in_link()

    sing_in_page.check_is_this_sign_in_page()
