import time
import pytest
from pages.home_dashboard_page import HomeDashboardPage
from pages.login_page import LoginPage
from pages.org_structure_page import OrgStructurePage
from utilities.data_reader_util import read_csv_data
from playwright.sync_api import expect


# Read the data from the test data files
csv_data=read_csv_data("testdata/logindata.csv")

@pytest.mark.parametrize("testName,email,password,expected",csv_data)
def test_home_dashboard(page,testName,email,password,expected):
    login_page = LoginPage(page)
    home_dashboard_page = HomeDashboardPage(page)
    # org_structure = OrgStructurePage(page)
    login_page.login(email, password)
    time.sleep(1)
    # home_dashboard_page.click_profile_confi()
    # time.sleep(1)
    # home_dashboard_page.click_organization_structure()
    # time.sleep(5)

    expect(home_dashboard_page.get_my_account_page_name()).to_be_visible(timeout=3000)
    time.sleep(3)


