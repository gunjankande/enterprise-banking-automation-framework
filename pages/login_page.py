from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.username = self.page.locator("#username")
        self.api_token = self.page.locator("#password")
        self.open_app_button = self.page.locator("#loginBtn")

    def enter_api_token(self,api_token):
        self.api_token.fill(api_token)


    def click_open_app(self):
        self.open_app_button.click()

    def login(self,api_token):
        self.enter_api_token(api_token)

        print("JSON Token :", repr(api_token))
        print("Textbox    :", repr(self.api_token.input_value()))

        self.click_open_app()