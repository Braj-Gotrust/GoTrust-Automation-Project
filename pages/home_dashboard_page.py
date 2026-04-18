from playwright.sync_api import Page


# this is a class
class HomeDashboardPage:

    # constructor
    def __init__(self,page: Page):
        self.page = page
        # locators
        self.txt_account_name = self.page.locator("div[class='hidden text-left sm:block']")



    def get_my_account_page_name(self):
        # Return the account name
        try:
            return self.txt_account_name
        except Exception as e:
            print(f"Error returning My Account page name: {e}")
            return None



