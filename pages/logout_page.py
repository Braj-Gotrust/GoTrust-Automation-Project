import time
from playwright.sync_api import Page


# this is a class
class LogoutPage:

    # constructor
    def __init__(self,page: Page):
        self.page = page

        # locators
        self.txt_my_account = self.page.locator(".hidden.text-left")
        self.btn_sign_out = self.page.get_by_role("menuitem", name="Sign out")
        self.btn_confirm_sign_out = self.page.locator("#kc-logout")
        self.sign_out_msg = self.page.locator("#kc-page-title")


    def click_my_account(self):
        # Click the my account.
        try:
            self.txt_my_account.click()
        except Exception as e:
            print(f" Exception while click my account: {e}")
            raise

    def click_sign_out_btn(self):
        # Click the sign out button.
        try:
            self.btn_sign_out.click()
        except Exception as e:
            print(f" Exception while click sign out button: {e}")
            raise

    def click_confirm_sign_out_btn(self):
        # Click the confirm sign out button.
        try:
            self.btn_confirm_sign_out.click()
        except Exception as e:
            print(f" Exception while click confirm sign out button: {e}")
            raise

    def get_confirm_signout_message(self):
        # Again login page visible
        return self.sign_out_msg


    def signout(self):
        """
        Perform the complete login operation:
        1. click my account
        2. click sign out button
        3. Click confirm sign out button
        """
        self.click_my_account()
        time.sleep(1)
        self.click_sign_out_btn()
        time.sleep(1)
        # sign out confirmation modal/ popup
        #self.click_confirm_sign_out_btn()

        return self.sign_out_msg

