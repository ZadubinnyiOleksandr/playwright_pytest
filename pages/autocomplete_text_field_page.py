import string
import random

from playwright.sync_api import Page, expect


class AutocompleteTextField:

    def __init__(self, page: Page):
        self.page = page

        self.__text_field = self.page.locator('#myInput')
        self.__autocomplete_list = self.page.locator('#myInputautocomplete-list')
        self.__elements_autocomplete_list = self.page.locator('#myInputautocomplete-list div')

    def set_random_letter_text_field(self) -> None:
        self.__text_field.fill(random.choice(string.ascii_letters))

    def choose_random_option(self) -> None:
        self.__autocomplete_list.wait_for(state='visible')
        random.choice(list(self.__elements_autocomplete_list.all())).click()
        print(self.__text_field.input_value())
