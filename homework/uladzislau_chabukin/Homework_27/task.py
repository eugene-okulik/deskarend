from playwright.sync_api import Page, expect, BrowserContext


def test_alert(page: Page):
    url = ' https://www.qa-practice.com/elements/alert/confirm'
    page.goto(url)

    page.on('dialog', lambda alert: alert.accept())

    button = page.get_by_role('link', name='Click')
    button.click()

    result_text = page.locator('#result-text')
    expected_text = 'Ok'
    expect(result_text).to_have_text(expected_text)


def test_tabs(page: Page, context: BrowserContext):
    url = 'https://www.qa-practice.com/elements/new_tab/button'
    page.goto(url)

    button = page.get_by_role('link', name='Click')
    with context.expect_page() as new_page_event:
        button.click()
    new_page = new_page_event.value

    result_text = new_page.locator('#result-text')
    expected_text = 'I am a new page in a new tab'

    expect(result_text).to_have_text(expected_text)
    expect(button).to_be_enabled()


def test_color_change(page: Page):
    url = 'https://demoqa.com/dynamic-properties'
    page.goto(url)

    button_color_change = page.get_by_role('button', name='Color Change')
    expect(button_color_change).to_have_css('color', 'rgb(220, 53, 69)', timeout=5500)
    button_color_change.click()
