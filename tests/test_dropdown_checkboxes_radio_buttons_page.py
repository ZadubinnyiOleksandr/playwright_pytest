import pytest

from pages.dropdown_checkboxes_radio_buttons_page import Dropdown, Checkbox, RadioButton

class TestDropdownCheckboxRadio:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.dropdown = Dropdown(self.page)
        self.checkbox = Checkbox(self.page)
        self.radio_button = RadioButton(self.page)

        self.page.goto('https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html')

    def test_dropdown(self, test_setup):
        self.dropdown.iterate_all_options_dropdowns()

    def test_checkbox(self, test_setup):
        self.checkbox.check_all_options()
        self.checkbox.uncheck_all_options()

    def test_radio_button(self, test_setup):
        self.radio_button.check_radio()