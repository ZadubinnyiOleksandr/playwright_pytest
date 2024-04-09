from playwright.sync_api import Page, expect


class PopupAlert:

    def __init__(self, page: Page):
        self.page = page

        self.__modal_popup_button = self.page.locator('#button2')
        self.__ajax_loader_button = self.page.locator('#button3 a')
        self.__js_confirm_box_button = self.page.locator('#button4')
        self.__js_confirm_box_result = self.page.locator('#confirm-alert-text')
        self.__popup = self.page.locator('.modal-content')
        self.__popup_close_button = self.page.locator('.modal-footer .btn-default')
        self.__ajax_loader_popup_button = self.page.locator('#button1')

    def modal_popup(self) -> None:
        self.__modal_popup_button.click()
        expect(self.__popup).to_be_visible()
        self.__popup_close_button.click()
        expect(self.__popup).not_to_be_visible()

    def ajax_loader(self) -> None:
        self.__ajax_loader_button.click()
        self.__ajax_loader_popup_button.wait_for(state='visible')
        self.__ajax_loader_popup_button.click()
        expect(self.__popup).to_be_visible()
        self.__popup_close_button.click()
        expect(self.__popup).not_to_be_visible()

    def accept_js_confirm_allert(self) -> None:
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.__js_confirm_box_button.click()
        expect(self.__js_confirm_box_result).to_have_text('You pressed OK!')

    def dismiss_js_confirm_allert(self) -> None:
        self.page.on("dialog", lambda dialog: dialog.dismiss())
        self.__js_confirm_box_button.click()
        expect(self.__js_confirm_box_result).to_have_text('You pressed Cancel!')

