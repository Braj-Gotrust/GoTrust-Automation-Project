import time
from playwright.sync_api import Page
class UcmPage:
    def __init__(self,page: Page):
        self.page = page
        self.risk_register_txt = page.locator("span:has-text('Risk Register')")
        self.pii_label_inventory_txt =page.locator("span:has-text('PII Label Inventory')")
        self.ucm_title = page.locator("a:has-text('Universal Consent Management')")