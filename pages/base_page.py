import os

from playwright.sync_api import expect


class BasePage:
    #Test
    #Test 2
    server = os.getenv('SERVER', "")
    ADMIN_URL = f"https://m0s0n07:m0s0n07@www{server}.motorsport.com/"

    # server = '-s'
    # server = '-t'
    def __init__(self, page):
        self.page = page

    def click_to_element(self, loc):
        element = self.page.locator(loc)
        element.click()

    def element_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()
