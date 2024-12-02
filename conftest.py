import pytest
import os
from pages.base_page import BasePage

server = BasePage.server
headless = os.getenv('HEADLESS', False)

@pytest.fixture(scope='function')
def setUp(playwright):
    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context()
    page = context.new_page()
    page.goto(BasePage.ADMIN_URL, wait_until="load")
    yield page
    browser.close()
