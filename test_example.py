import pytest

from pages.new_page import NewPage


class TestArticleEdp:

    @pytest.mark.parametrize('edition', NewPage.editions)
    def test_click_to_start(self, edition, setUp):
        page = NewPage(setUp)
        page.switch_front_edition(edition)
        url_list = page.main_url_list()
        page.check_page_code(url_list)
