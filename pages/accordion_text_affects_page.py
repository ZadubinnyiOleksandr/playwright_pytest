from playwright.sync_api import Page, expect


class AccordionTextAffects:

    def __init__(self, page: Page):
        self.page = page

        self.__accordion_buttons_list = self.page.locator('[class="accordion active"]')
        self.__manual_testing_description = self.page.locator('#manual-testing-description')
        self.__cucumber_testing_description = self.page.locator('#cucumber-testing-description')
        self.__automation_testing_description = self.page.locator('#automation-testing-description')
        self.__appearing_text = self.page.locator('#timeout')
        self.__text_appear_box = self.page.locator('text-appear-box')

    def click_on_list_items(self) -> None:
        for item in list(self.__accordion_buttons_list.all()):
            item.click()

    def check_is_visible(self) -> None:
        self.__manual_testing_description.wait_for(state='visible')
        expect(self.__manual_testing_description).to_have_text('Manual testing has for some time been the most popular way to test code. For this method, the tester plays an important role of end user and verifies that all the features of the application work correctly. Manual testing however is on the decline. Companies and developers have realised the efficiency, accuracy and cost savings that is possible by adopting the use of automation testing.')
        self.__cucumber_testing_description.wait_for(state='visible')
        expect(self.__cucumber_testing_description).to_have_text('Cucumber (BDD) simplifies the requirement capturing process. Requirements can be captured, broken down and simplified effortlessly; making the captured requirements readable to anyone within the organisation and in turn providing the required details and backbone to develop accurate test cases also known as ‘Feature Files’.')
        self.__automation_testing_description.wait_for(state='visible')
        expect(self.__automation_testing_description).to_have_text('Automation testing has been steadily grown in popularity these past few years thanks to the time/ cost savings and efficiency that it offers. Companies throughout the world have or plan to use automation testing to rapidly speed up their test capabilities. Automation test engineers are in great demand and offer an average salary of £45,000+ (2018). Now is a great time to learn about automation test engineering and this course has been carefully developed to slowly introduce you from the basics, all the way to building advanced frameworks.')
        self.page.wait_for_timeout(5000)
        self.__appearing_text.wait_for(state='visible')
        expect(self.__appearing_text).to_have_text('This text has appeared after 5 seconds!')