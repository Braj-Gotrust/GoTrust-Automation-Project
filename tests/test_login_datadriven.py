import time

import pytest
from playwright.sync_api import Playwright
from pages.login_page import LoginPage
from pages.home_dashboard_page import HomeDashboardPage
from playwright.sync_api import expect
from utilities.data_reader_util import read_excel_data


# Read the data from the test data files
excel_data=read_excel_data("testdata/logindata.xlsx", "Login_Data")

@pytest.mark.parametrize("testName,email,password,expected",excel_data)
def test_login_data_driven(page,testName,email,password,expected):
    login_page = LoginPage(page)
    home_dashboard_page = HomeDashboardPage(page)
    login_page.login(email, password)
    time.sleep(2)

    if expected=="success":
        expect(home_dashboard_page.get_my_account_page_name()).to_be_visible(timeout=3000)
        time.sleep(5)
    else:
        expect(login_page.get_login_error()).to_be_visible(timeout=3000)



