from playwright.sync_api import expect
import re

from config import Config
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage

# ==================== TEST CASE: Create User ====================
def test_user_management(page):

    # ================= TEST DATA =================

    dpo_email = Config.dpo_email
    dpo_password = Config.dpo_password

    first_name = Config.user_first_name
    last_name = Config.user_last_name
    username = Config.username
    email = Config.user_email
    phone_number = Config.phone_number
    role_name = Config.role_name

    group_names = Config.group_names

    # ================= PAGE OBJECTS =================

    login_page = LoginPage(page)
    user_management = UserManagementPage(page)

    # ================= LOGIN =================

    login_page.login(
        dpo_email,
        dpo_password
    )

    # ================= NAVIGATION =================

    user_management.navigate_to_user_management()

    # ================= CREATE USER =================

    user_management.click_add_user()

    user_management.fill_user_details(
        first_name,
        last_name,
        username,
        email,
        phone_number
    )

    user_management.select_role(role_name)

    user_management.assign_groups(group_names)

    user_management.click_assign_unassign()

    user_management.click_submit()

    user_management.click_yes()

    # ================= VALIDATION =================

    success_message = user_management.get_success_message()

    expect(success_message).to_be_visible(timeout=15000)


# ==================== TEST CASE: Edit User ====================
def test_edit_user_management(page):

    # ================= TEST DATA =================

    dpo_email = Config.dpo_email
    dpo_password = Config.dpo_password
    edit_first_name = Config.edit_first_name
    edit_last_name = Config.edit_last_name
    edit_phone_number = Config.edit_phone_number
    edit_role_name = Config.edit_role_name
    edit_group_names = Config.edit_group_names

    # ================= PAGE OBJECTS =================
    login_page = LoginPage(page)
    user_management = UserManagementPage(page)

    # ================= LOGIN =================
    login_page.login(
        dpo_email,
        dpo_password
    )

    # ================= NAVIGATION =================
    user_management.navigate_to_user_management()

    # ================= EDIT USER =================
    user_management.open_first_user_for_edit()  

    user_management.edit_user_details(
        edit_first_name,
        edit_last_name,
        edit_phone_number
    )
    user_management.edit_user_role(edit_role_name)
    user_management.edit_user_groups(edit_group_names)
    user_management.click_submit()
    user_management.click_yes() 

    # ================= VALIDATION =================
    success_message = user_management.get_edit_success_message()
    # expect(success_message).to_be_visible(timeout=15000)
    expect(success_message).to_contain_text("success",timeout=15000)















