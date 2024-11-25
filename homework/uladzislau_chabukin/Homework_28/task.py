import json

from playwright.sync_api import Page, expect, Route


def test_iphone(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()

        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 16 про'

        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route('**/digitalmat', handle_route)
    url = 'https://www.apple.com/shop/buy-iphone'

    page.goto(url)
    iphone_16_pro = page.locator('.rf-hcard-copy').locator('nth=0')
    iphone_16_pro.click()

    phone_title = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    expect(phone_title).to_contain_text('яблокофон 16 про')
