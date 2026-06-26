 
from pages.login_page import LoginPage
from pages.role_management_page import RoleManagementPage
from playwright.sync_api import expect
from config import Config
 
def test_open_role_management(page):
 
  # LOGIN DATA
    dpo_email = Config.dpo_email
    dpo_password = Config.dpo_password
    role_name = Config.role_name
 
    # Login
    login_page = LoginPage(page)
    login_page.login(dpo_email, dpo_password)
 
    
    role_page = RoleManagementPage(page)
 
    role_page.open_role_management()
    role_page.create_role(role_name)
    role_page.view_role()
    role_page.edit_role()
    role_page.add_user()
 