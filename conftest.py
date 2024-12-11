import pytest
import os
from pages.base_page import BasePage

server = BasePage.server
headless = os.getenv('HEADLESS', 'False') == 'True'

@pytest.fixture(scope='function')
def setUp(playwright):
    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context()
    page = context.new_page()
    page.goto(BasePage.ADMIN_URL, wait_until="domcontentloaded")
    yield page
    browser.close()
