from playwright.sync_api import Page, expect


class AjaxLoader:

    def __init__(self, page: Page):
        self.page = page

        self.__click_me_btn = self.page.locator('#button1')
        self.__done_header_modal = self.page.locator('[class="modal-title"]')

    def click_btn(self) -> None:
        self.__click_me_btn.wait_for(state='visible')
        self.__click_me_btn.click()

    def check_done_modal(self) -> None:
        self.__done_header_modal.wait_for(state='visible')
        expect(self.__done_header_modal).to_have_text('Well Done For Waiting....!!!')