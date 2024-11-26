def test_click_on_button_shop_women_deals(sale_page, women_sale_page):
    sale_page.open_page()

    sale_page.click_on_button_women_deals()

    women_sale_page.check_is_this_women_sale_page()


def test_click_on_link_shop_men_deals(sale_page, men_sale_page):
    sale_page.open_page()

    sale_page.click_on_link_men_deals()

    men_sale_page.check_is_this_men_sale_page()


def test_click_on_link_luma_gear(sale_page, gear_page):
    sale_page.open_page()

    sale_page.click_on_link_luma_gear()

    gear_page.check_is_this_gear_page()
