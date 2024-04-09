import pytest

from pages.popups_alerts_page import PopupAlert


class TestAction:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.popup_allert = PopupAlert(self.page)

        self.page.goto('https://webdriveruniversity.com/Popup-Alerts/index.html')

    def test_modal_popup(self, test_setup):
        self.popup_allert.modal_popup()

    def test_ajax_popup(self, test_setup):
        self.popup_allert.ajax_loader()

    def test_accept_js_confirm(self, test_setup):
        self.popup_allert.accept_js_confirm_allert()

    def test_dismiss_js_confirm(self, test_setup):
        self.popup_allert.dismiss_js_confirm_allert()