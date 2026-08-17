import time

from playwright.sync_api import Page


# this is a class
class LoginPage:

    # constructor
    def __init__(self,page: Page):
        self.page = page
        self.cookie_banner_close = page.locator("button:has-text('Allow all')")
        # locators
        self.txt_email_address = self.page.locator("#username")
        self.txt_password = self.page.locator("#password")
        self.btn_login_button = self.page.locator("button[type='submit']:has-text('Sign In'), input[type='submit'][value='Sign In']")
        self.txt_error_message = self.page.locator("div[aria-live='polite']")

    def set_email(self,email: str):
        # Enter the email address in the Email field.
        try:
            self.txt_email_address.clear()
            self.txt_email_address.fill(email)
        except Exception as e:
            print(f" Exception while entering email: {e}")
            raise

    def set_password(self,password: str):
        # Enter the password in the password field.
        try:
            self.txt_password.clear()
            self.txt_password.fill(password)
        except Exception as e:
            print(f" Exception while entering password: {e}")
            raise

    def click_login(self):
        # Click the login button.
        try:
            self.btn_login_button.click()
        except Exception as e:
            print(f" Exception while click login button: {e}")
            raise

    def click_cookie_banner_close_btn(self):
        # Click the login button.
        try:
            if self.cookie_banner_close.is_visible():
                self.cookie_banner_close.click()
        except Exception as e:
            print(f" Exception while click on cookie banner close button: {e}")
            raise

    def login(self, email: str, password: str):
        """
        Perform the complete login operation:
        1. Enter email
        2. Enter password
        3. Click the Login button
        """
        self.set_email(email)
        self.set_password(password)
        self.click_login()
        self.page.wait_for_timeout(5000)
        self.click_cookie_banner_close_btn()

        # if self.cookie_banner_close.is_visible():
        #     self.cookie_banner_close.click()

    def get_login_error(self):
        # Return the error message element if login fails.
        try:
            return self.txt_error_message
        except Exception as e:
            print(f" Exception while fetching login error message: {e}")
            return None