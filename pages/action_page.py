from playwright.sync_api import Page, expect


class Action:

    def __init__(self, page: Page):
        self.page = page

        self.__object = self.page.locator('#draggable')
        self.__target = self.page.locator('#droppable')
        self.__double_click = self.page.locator('#double-click')
        self.__first_dropdown_hover = self.page.get_by_text('Hover Over Me First!')
        self.__button_for_first_dropdown_hover = self.page.get_by_text('Hover Over Me First!').locator('+ div a')
        self.__second_dropdown_hover = self.page.get_by_text('Hover Over Me Second!')
        self.__button_for_second_dropdown_hover = self.page.get_by_text('Hover Over Me Second!').locator('+ div a')
        self.__third_dropdown_hover = self.page.get_by_text('Hover Over Me Third!')
        self.__first_button_for_second_dropdown_hover = self.page.get_by_text('Hover Over Me Third!').locator(
            '+ div a').first
        self.__second_button_for_second_dropdown_hover = self.page.get_by_text('Hover Over Me Third!').locator(
            '+ div a').last
        self.__click_and_hold_box = self.page.locator("#click-box")

    def drag_and_drop(self) -> None:
        self.__object.drag_to(self.__target)
        expect(self.__target).to_have_text('Dropped!')

    def double_click(self) -> None:
        self.__double_click.dblclick()
        expect(self.__double_click).to_have_css(value='rgb(147, 203, 90)', name='background-color')

    def hover_and_js_alert(self) -> None:
        def accept_dialog(self, trigger_dialog):
            dialog_message = None

            def handle_dialog(dialog):
                nonlocal dialog_message
                dialog_message = dialog.message
                dialog.dismiss()

            self.page.once("dialog", handle_dialog)
            trigger_dialog()
            return dialog_message

        self.__first_dropdown_hover.hover()
        dialog_message = accept_dialog(self, lambda: self.__button_for_first_dropdown_hover.click())
        print("First dialog message: " + f'{dialog_message}')

        self.__second_dropdown_hover.hover()
        dialog_message = accept_dialog(self, lambda: self.__button_for_second_dropdown_hover.click())
        print("Second dialog message: " + f'{dialog_message}')

        self.__third_dropdown_hover.hover()
        dialog_message = accept_dialog(self, lambda: self.__first_button_for_second_dropdown_hover.click())
        print("Third dialog message: " + f'{dialog_message}')

        self.__third_dropdown_hover.hover()
        dialog_message = accept_dialog(self, lambda: self.__second_button_for_second_dropdown_hover.click())
        print("Fourth dialog message: " + f'{dialog_message}')

    def click_and_hold(self) -> None:
        self.__click_and_hold_box.hover()
        self.page.mouse.down()
        expect(self.__click_and_hold_box).to_have_css(value='rgb(0, 255, 0)', name='background-color')
        expect(self.__click_and_hold_box).to_have_text('Well done! keep holding that click now.....')
        self.page.mouse.up()
        expect(self.__click_and_hold_box).to_have_css(value='rgb(255, 99, 71)', name='background-color')
        expect(self.__click_and_hold_box).to_have_text('Dont release me!!!')
