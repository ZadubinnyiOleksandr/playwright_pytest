from playwright.sync_api import Page, expect


class TodoList:

    def __init__(self, page: Page):
        self.page = page

        self.__todo_list = self.page.locator('#container ul')
        self.__todo_list_elements = self.page.locator('#container ul li')
        self.__todo_list_element = self.page.locator('#container ul li:last-child')
        self.__todo_list_element_delete_button = self.page.locator('#container ul li:last-child .fa-trash')
        self.__todo_input = self.page.locator("input")

    def clear_todo_list(self) -> None:
        todo_list = list(self.__todo_list_elements.all())
        for i in todo_list:
            self.__todo_list_element.hover()
            self.page.wait_for_timeout(300)
            self.__todo_list_element_delete_button.click()
            self.page.wait_for_timeout(300)
        expect(self.__todo_list).not_to_be_visible()

    def create_todos(self) -> None:
        i = 0
        while i < 3:
            self.__todo_input.click()
            self.__todo_input.press(f'{i}')
            self.__todo_input.press("Enter")
            i = i + 1
        expect(self.__todo_list_elements).to_have_count(3)

