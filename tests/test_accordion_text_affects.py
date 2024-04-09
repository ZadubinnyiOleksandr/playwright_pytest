import pytest

from pages.accordion_text_affects_page import AccordionTextAffects


class TestAutocompleteTextField:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.accordion_text_affects = AccordionTextAffects(self.page)

        self.page.goto('https://webdriveruniversity.com/Accordion/index.html')

    def test_accordion_text_affects(self, test_setup):
        self.accordion_text_affects.click_on_list_items()
        self.accordion_text_affects.check_is_visible()