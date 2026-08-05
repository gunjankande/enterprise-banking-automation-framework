from playwright.sync_api import Page
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self,page):
        super().__init__(page)

        self.new_account_button = page.get_by_role(
            "button",
            name="New Account",
        )

    