import time
import re
from playwright.sync_api import Page, expect


class UserManagementPage:

    def __init__(self, page: Page):
        self.page = page

        # Navigation
        self.btn_access_management = page.get_by_role("button", name="Access Management")
        self.link_user_management = page.locator("a:has-text('User Management')")

        # Add user
        self.btn_add_user = page.get_by_role(
            "button",
            name="right arrow sign Add User"
        )

        # Form fields
        self.txt_first_name = page.get_by_role(
            "textbox",
            name="Enter first name"
        )

        self.txt_last_name = page.get_by_role(
            "textbox",
            name="Enter last name"
        )

        self.txt_username = page.get_by_role(
            "textbox",
            name="Username"
        )

        self.txt_email = page.get_by_role(
            "textbox",
            name="Enter email"
        )

        self.txt_phone_number = page.get_by_role(
            "textbox",
            name="Enter phone number"
        )

        # Role dropdown
        self.dropdown_role = page.get_by_role(
            "combobox",
            name="Select Role*"
        )

        # Group assignment
        self.txt_group_assigned = page.get_by_role(
            "textbox",
            name="Group Assigned*"
        )

        # Buttons
        self.btn_assign_unassign = page.get_by_role(
            "button",
            name="Assign/Unassign"
        )

        self.btn_submit = page.get_by_role(
            "button",
            name="Submit"
        )

        self.btn_yes = page.get_by_role(
            "button",
            name="Yes"
        )

        # Success message
        self.success_message = page.locator(".Toastify__toast")
    # ================= NAVIGATION =================

    def navigate_to_user_management(self):
        expect(self.btn_access_management).to_be_visible(timeout=15000) #wait for access management button to be visible
        self.btn_access_management.click() #click on access management button

        self.page.wait_for_timeout(2000)  # Wait for the dropdown to appear

        expect(self.link_user_management).to_be_visible(timeout=15000) #wait for user management link to be visible
        self.link_user_management.click() #click on user management link

        self.page.wait_for_timeout(1000)  # small wait 
        self.link_user_management.click() #double click to ensure the page loads (sometimes single click might not work due to UI responsiveness)



    # ================= USER ACTIONS =================

    def click_add_user(self):
        self.btn_add_user.click()

    def fill_user_details(
            self,
            first_name: str,
            last_name: str,
            username: str,
            email: str,
            phone_number: str
    ):

        self.txt_first_name.fill(first_name)
        self.txt_last_name.fill(last_name)
        self.txt_username.fill(username)
        self.txt_email.fill(email)
        self.txt_phone_number.fill(phone_number)

    # def select_role(self, role_name: str):

    #     self.dropdown_role.click()

    #     self.page.get_by_label(role_name)\
    #         .get_by_text(role_name)\
    #         .click()
    def select_role(self, role_name):
     self.dropdown_role.click()
     option = self.page.locator(
        '[role="option"]',
        has_text=role_name
     ).first

     expect(option).to_be_visible(timeout=10000)
     option.click()

    def assign_groups(self, group_names: list):

        self.txt_group_assigned.click()

        for group in group_names:
            self.page.get_by_role(
                "checkbox",
                name=group,
                exact=True
            ).click()

    def click_assign_unassign(self):
        self.btn_assign_unassign.click()

    def click_submit(self):
        self.btn_submit.click()

    def click_yes(self):
        self.btn_yes.click()

    # ================= VALIDATIONS =================

    def get_success_message(self):
        return self.success_message
    
    # ============== Edit User ==============
    def open_first_user_for_edit(self):
        edit_button = self.page.get_by_role("button", name="Table Action Icon").nth(0)
        expect(edit_button).to_be_visible()
        edit_button.click()

    def edit_user_details(
            self,
            first_name,
            last_name,
            phone_number
    ):

        self.page.get_by_role("textbox", name= "First Name").fill(first_name)
        self.page.get_by_role("textbox", name= "Last Name").fill(last_name)
        self.page.get_by_role("textbox", name= "Phone*").fill(phone_number)

    def edit_user_role(self, role_name):
        self.page.get_by_role("combobox", name="Select Role*").click()
        self.page.get_by_label(role_name).get_by_text(role_name).click()

    def edit_user_groups(self,group_names):
        self.page.get_by_role("textbox", name="Group Assigned*").click()
        for group in group_names:
            self.page.get_by_role("checkbox", name=group, exact=True).click()
      
    def get_edit_success_message(self):
       return self.page.locator(".Toastify__toast")  # better method to capture dynamic success message after edit, as it appears in a toast notification.

