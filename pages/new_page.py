from pages.base_page import BasePage
from pages.locators import new_locs as loc
import requests


class NewPage(BasePage):
    editions = (
        'www',
        'tr',
        'lat',
        'jp',
    )

    def click_to_get_started_button(self):
        self.click_to_element(loc.GET_STARTED_BUTTON)

    def check_title(self):
        self.element_visible(loc.H1)

    def main_url_list(self):
        test = self.get_url_list(loc.MAIN_MENUE)
        return test

    def switch_front_edition(self, edition):
        if edition == 'ac':
            if self.server == '-s':
                url = 'https://m0t007:m0t007@www-s.autosport.com/'
            else:
                url = 'https://www.autosport.com/'
        else:
            url = f'https://m0t007:m0t007@{edition}{self.server}.motorsport.com/'
        self.page.on("console", lambda msg: print(f"Console log: {msg.text}"))
        response = self.page.goto(url, wait_until="load")
        if response and response.status != 200:
            raise Exception(f"Failed to load page: {response.status}")

    def get_url_list(self, loc):
        path_list = []
        urls = self.page.locator(loc).all()
        for url in urls:
            href = url.get_attribute('href')
            path_list.append(href)
        return path_list

    def check_page_code(self, url_list):
        for i in url_list:
            print(i)
            if 'http' in i:
                pass
            else:
                r = requests.get(f"https://m0t007:m0t007@www{self.server}.motorsport.com{i.strip()}")
                assert r.status_code == 200 or 404
