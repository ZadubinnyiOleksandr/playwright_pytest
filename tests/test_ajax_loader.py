import pytest

from pages.ajax_page import AjaxLoader


class TestAjaxLoader:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.ajax_loader = AjaxLoader(self.page)

        self.page.goto('https://webdriveruniversity.com/Ajax-Loader/index.html')

    def test_ajax_loader(self, test_setup):
        self.ajax_loader.click_btn()
        self.ajax_loader.check_done_modal()