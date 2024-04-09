from playwright.sync_api import Page, expect


class ContactForm:

    def __init__(self, page: Page):
        self.page = page

        self.__first_name_input = self.page.locator('input[name="first_name"]')
        self.__last_name_input = self.page.locator('input[name="last_name"]')
        self.__email_input = self.page.locator('input[name="email"]')
        self.__comments_input = self.page.locator('textarea[name="message"]')
        self.__reset_btn = self.page.locator('input[value="RESET"]')
        self.__submit_btn = self.page.locator('input[value="SUBMIT"]')
        self.__thanks_message = self.page.locator('#contact_reply h1')

    def set_user_first_name(self, user_first_name) -> None:
        self.__first_name_input.fill(user_first_name)

    def set_user_last_name(self, user_last_name) -> None:
        self.__last_name_input.fill(user_last_name)

    def set_email(self, email) -> None:
        self.__email_input.fill(email)

    def set_comment(self, comment) -> None:
        self.__comments_input.fill(comment)

    def reset_form(self) -> None:
        self.__reset_btn.click()

    def submit_form(self) -> None:
        self.__submit_btn.click()
        self.__thanks_message.wait_for(state='visible')

    def check_reseted_form(self) -> None:
        expect(self.__first_name_input).to_have_value('')
        expect(self.__last_name_input).to_have_value('')
        expect(self.__email_input).to_have_value('')
        expect(self.__comments_input).to_have_value('')

    def check_submited_form(self) -> None:
        expect(self.__thanks_message).to_have_text('Thank You for your Message!')