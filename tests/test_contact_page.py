import pytest

from pages.contact_page import ContactForm
from data.test_data import Data


class TestContactForm:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={'width': 1920, 'height': 1080})
        self.contact_form = ContactForm(self.page)

        self.page.goto('https://webdriveruniversity.com/Contact-Us/contactus.html')

    def test_contact_form(self, test_setup):
        self.contact_form.set_user_first_name(Data.user_first_name)
        self.contact_form.set_user_last_name(Data.user_last_name)
        self.contact_form.set_email(Data.email)
        self.contact_form.set_comment(Data.comment)
        self.contact_form.reset_form()
        self.contact_form.check_reseted_form()
        self.contact_form.set_user_first_name(Data.user_first_name)
        self.contact_form.set_user_last_name(Data.user_last_name)
        self.contact_form.set_email(Data.email)
        self.contact_form.set_comment(Data.comment)
        self.contact_form.submit_form()
        self.contact_form.check_submited_form()
