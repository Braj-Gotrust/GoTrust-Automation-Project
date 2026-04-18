import time
from pages.home_dashboard_page import HomeDashboardPage
from playwright.sync_api import expect
from config import Config
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


def test_logout(page):
    login_page = LoginPage(page)
    home_dashboard_page = HomeDashboardPage(page)
    logout_page = LogoutPage(page)
    login_page.login(Config.dpo_email, Config.dpo_password)
    time.sleep(2)

    expect(home_dashboard_page.get_my_account_page_name()).to_be_visible(timeout=3000)

    logout_page.signout()
    time.sleep(2)
    expect(logout_page.get_confirm_signout_message()).to_be_visible(timeout=3000)
    time.sleep(3)

