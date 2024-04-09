from playwright.sync_api import Page, expect


class Dropdown:

    def __init__(self, page: Page):
        self.page = page

        self.__first_dropdown = self.page.locator('#dropdowm-menu-1')
        self.__options_first_dropdown = self.page.locator('#dropdowm-menu-1 option')
        self.__second_dropdown = self.page.locator('#dropdowm-menu-2')
        self.__options_second_dropdown = self.page.locator('#dropdowm-menu-2 option')
        self.__third_dropdown = self.page.locator('#dropdowm-menu-3')
        self.__options_third_dropdown = self.page.locator('#dropdowm-menu-3 option')

    def iterate_all_options_dropdowns(self) -> None:
        options_first_dropdown = list(self.__options_first_dropdown.all())
        options_second_dropdown = list(self.__options_second_dropdown.all())
        options_third_dropdown = list(self.__options_third_dropdown.all())
        for i in options_first_dropdown:
            self.__first_dropdown.select_option(f'{i.text_content()}')
            for j in options_second_dropdown:
                self.__second_dropdown.select_option(f'{j.text_content()}')
                for k in options_third_dropdown:
                    self.__third_dropdown.select_option(f'{k.text_content()}')
                    expect(self.__first_dropdown).to_have_value(f'{i.text_content().lower()}')
                    expect(self.__second_dropdown).to_have_value(f'{j.text_content().lower()}')
                    expect(self.__third_dropdown).to_have_value(f'{k.text_content().lower()}')


class Checkbox:

    def __init__(self, page: Page):
        self.page = page

        self.__first_option = self.page.get_by_label("Option 1")
        self.__second_option = self.page.get_by_label("Option 2")
        self.__third_option = self.page.get_by_label("Option 3")
        self.__fourth_option = self.page.get_by_label("Option 4")
        self.options = (self.__first_option, self.__second_option, self.__third_option, self.__fourth_option)

    def check_all_options(self) -> None:
        for i in self.options:
            i.check()
            expect(i).to_be_checked()

    def uncheck_all_options(self) -> None:
        for i in self.options:
            i.uncheck()
            expect(i).not_to_be_checked()


class RadioButton:

    def __init__(self, page: Page):
        self.page = page

        self.__radio_buttons_form = self.page.locator('#radio-buttons')
        self.__radio_buttons = self.page.locator('#radio-buttons input')

    def check_radio(self) -> None:
        radio_buttons_list = list(self.__radio_buttons.all())
        for i in radio_buttons_list:
            i.check()
            expect(i).to_be_checked()