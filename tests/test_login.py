
from playwright.sync_api import expect

from config.config import BASE_URL
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.json_reader import read_json


def test_valid_login(page):


    # Read Login Test Data
    data = read_json("testdata/login_data.json")
    login_data = data["valid_user"]

     # Navigate to Login Page
    login = LoginPage(page)
    login.navigate(BASE_URL)

    page.wait_for_timeout(5000)

    # Login
    login.login(
        login_data["api_token"]
    )

    page.wait_for_timeout(5000)

    # Dashboard
    dashboard = DashboardPage(page)

    # Verify Successful Login
    expect(dashboard.new_account_button).to_be_visible()


