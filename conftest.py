import pytest
from pages.base_page import BasePage

server = BasePage.server

ADMIN_URL = f"https://www{server}.motorsport.com/?edition_force=global"


@pytest.fixture(scope='function')
def setUp(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    yield page
    browser.close()
