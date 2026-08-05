from playwright.sync_api import Page
from pages.base_page import BasePage


class NewAccountPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)

        self.account_type = page.locator("#modalAccountType")
        self.initial_deposit = page.locator("#modalInitialDeposit")
        self.create_account_button = page.get_by_role(
            "button",
            name="Create Account"
        )

    def select_account_type(self,account_type):
        self.account_type.select_option(account_type)

    def enter_initial_deposit(self,amount):
        self.initial_deposit.fill(str(amount))

    def click_create_account(self):
        self.create_account_button.click()

    def create_account(self,account_type,amount):
        self.select_account_type(account_type)
        self.enter_initial_deposit(amount)
        self.click_create_account()

