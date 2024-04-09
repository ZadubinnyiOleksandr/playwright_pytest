import pytest

from pages.action_page import Action


class TestAction:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.action = Action(self.page)

        self.page.goto('https://webdriveruniversity.com/Actions/index.html#')

    def test_drag_and_drop(self, test_setup):
        self.action.drag_and_drop()

    def test_double_click(self, test_setup):
        self.action.double_click()

    def test_hover_and_alert(self, test_setup):
        self.action.hover_and_js_alert()

    def test_click_and_hold_box(self, test_setup):
        self.action.click_and_hold()