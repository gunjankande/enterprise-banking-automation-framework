from playwright.sync_api import expect

from config.config import BASE_URL
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.new_account_page import NewAccountPage
from utils.json_reader import read_json


def test_create_new_savings_account(page):

    # Read login Data
    data = read_json("testdata/login_data.json")
    login_data = data["valid_user"]

    # Login
    login = LoginPage(page)
    login.navigate(BASE_URL)
    login.login(login_data["api_token"])

    # Open Create Account Dialog
    dashboard = DashboardPage(page)
    dashboard.open_new_account()

    # Create New Account

    new_account = NewAccountPage(page)
    new_account.create_account(
        account_type="SAVINGS",
        amount=5000
    )

    # TODO
    # Verify account created successfully - Future Scope
