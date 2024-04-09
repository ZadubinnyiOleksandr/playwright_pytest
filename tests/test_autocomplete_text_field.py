import pytest

from pages.autocomplete_text_field_page import AutocompleteTextField

class TestAutocompleteTextField:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.autocomplete_text_field = AutocompleteTextField(self.page)

        self.page.goto('https://webdriveruniversity.com/Autocomplete-TextField/autocomplete-textfield.html')

    def test_autocomplete_text_field(self, test_setup):
        self.autocomplete_text_field.set_random_letter_text_field()
        self.autocomplete_text_field.choose_random_option()