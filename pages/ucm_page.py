import time
from playwright.sync_api import Page
class UcmPage:
    def __init__(self,page: Page):
        self.page = page
        self.ucm_lab_txt = page.locator("span:has-text('UCM Lab')")
        self.pii_label_inventory_txt =page.locator("span:has-text('PII Label Inventory')")
        self.ucm_title = page.locator("a:has-text('Universal Consent Management')")
        # pii label tab
        self.search_box_txt = page.locator("input[placeholder='Search']")
        self.all_pii_label = page.locator("table tbody tr p")
        self.edit_btn = page.locator("button:has(svg.lucide-pencil)")
        self.radio_btn = page.locator("button[role='radio']")
        self.save_btn = page.locator("button:has-text('Save')")
        self.pii_label_update_confi_msg = page.get_by_text("PII label updated successfully")
        # processing category tab
        self.processing_category_tab = page.locator("a:has-text('Processing Category')")
        self.add_processing_category_btn = page.locator("button:has-text('Add Processing Category')")
        self.name_txt = page.locator("#name")
        self.description_txt = page.locator("#description")
        self.add_processing_category_confi_msg = page.get_by_text("Processing category added successfully")
        self.item_per_page_txt = page.locator(".lucide.lucide-chevron-down.size-4")
        self.dropdown = page.locator("div[role='option']")
        self.all_processing_category = page.locator("table tbody tr p")
        self.plus_btn = page.locator("button:has(svg.lucide-plus)")
        self.add_btn = page.locator("button:has-text('Add')")
        self.add_processing_activity_confi_msg_1 = page.get_by_text("Processing activity added successfully")
        # Processing Activities Tab
        self.processing_activity_tab = page.locator("a:has-text('Processing Activities')")
        self.add_processing_activities_btn = page.locator("button:has-text('Add Processing Activities')")
        self.select_txt = page.locator("span:has-text('Select')")
        self.add_processing_activity_confi_msg_2 = page.get_by_text("Processing activities added successfully")
        # Processing Purpose Tab
        self.processing_purpose_tab = page.locator("a:has-text('Processing Purpose')")
        self.add_processing_purpose_btn = page.locator("button:has-text('Add Processing Purpose')")
        self.expiry_days_clear_txt = page.locator("input[placeholder='Enter expiry']")
        self.expiry_days_fill_txt = page.locator("input[placeholder='Enter expiry']")
        self.add_processing_purpose_confi_msg = page.get_by_text("Processing purpose added successfully")















    def click_ucm_lab_btn(self):
        try:
            self.ucm_lab_txt.click()
        except Exception as e:
            print(f" Exception while click on ucm lab button : {e}")
            raise

    def click_pii_label_inventory_btn(self):
        try:
            self.pii_label_inventory_txt.click()
            self.pii_label_inventory_txt.click()
        except Exception as e:
            print(f" Exception while click on pii inventory button : {e}")
            raise

    def get_ucm_title(self):
        try:
            return self.ucm_title
        except Exception as e:
            print(f" Exception while getting ucm title : {e}")
            return None

    def fill_search_box(self,pii_label_name:str):
        try:
            self.search_box_txt.fill(pii_label_name)
            time.sleep(1)
        except Exception as e:
            print(f" Exception while search box : {e}")
            raise

    def select_pii_label(self,pii_label_name:str):
        try:
            count = self.all_pii_label.count()
            for i in range(count):
                text = self.all_pii_label.nth(i).inner_text().strip()
                if text.lower() == pii_label_name.lower():
                    self.edit_btn.nth(i).click()
                    time.sleep(1)
                    self.radio_btn.nth(0).click()
                    break
        except Exception as e:
            print(f"Exception while selecting pii label name: {e}")
            raise

    def click_save_btn(self):
        try:
            self.save_btn.click()
        except Exception as e:
            print(f" Exception while click on save button : {e}")
            raise

    def get_pii_label_update_confi_msg(self):
        try:
            return self.pii_label_update_confi_msg
        except Exception as e:
            print(f" Exception while pii label update confirmation message : {e}")
            return None

    def processing_category_tab_action_1(self, processing_category_name:str):
        try:
            self.processing_category_tab.nth(1).click()
            self.add_processing_category_btn.click()
            self.fill_name_and_description(processing_category_name)
            self.save_btn.click()
        except Exception as e:
            print(f" Exception while perform processing category actions : {e}")
            raise

    def fill_name_and_description(self,name:str):
        try:
            self.name_txt.fill(name)
            self.description_txt.fill("test")
        except Exception as e:
            print(f" Exception while fill name and description : {e}")
            raise

    def get_add_processing_category_confi_msg(self):
        try:
            return self.add_processing_category_confi_msg
        except Exception as e:
            print(f" Exception while add processing category confirmation message : {e}")
            return None

    def processing_category_tab_action_2(self, processing_category_name:str, processing_activity_name_1:str):
        try:
            self.page_extend()
            self.select_processing_category_in_table(processing_category_name)
            self.fill_name_and_description(processing_activity_name_1)
            self.add_btn.nth(1).click()
        except Exception as e:
            print(f" Exception while perform processing category actions : {e}")
            raise

    def page_extend(self):
        try:
            self.item_per_page_txt.click()
            self.dropdown.nth(4).click()
            time.sleep(1)
        except Exception as e:
            print(f"Exception while page extend: {e}")
            raise

    def select_processing_category_in_table(self, processing_category_name:str):
        try:
            count = self.all_processing_category.count()
            for i in range(count):
                text = self.all_processing_category.nth(i).inner_text().strip()
                if text.lower() == processing_category_name.lower():
                    self.plus_btn.nth(i).click()
                    break
        except Exception as e:
            print(f"Exception while selecting processing category name: {e}")
            raise

    def get_add_processing_activity_confi_msg_1(self):
        try:
            return self.add_processing_activity_confi_msg_1
        except Exception as e:
            print(f" Exception while getting add processing activity confirmation message 1 : {e}")
            return None

    def processing_activity_tab_action_1(self,processing_activity_name_2:str, processing_category_name:str):
        try:
            self.processing_activity_tab.nth(1).click()
            self.add_processing_activities_btn.click()
            self.fill_name_and_description(processing_activity_name_2)
            time.sleep(1)
            self.select_processing_category_in_list(processing_category_name)
            self.save_btn.click()
        except Exception as e:
            print(f" Exception while processing activity tab actions : {e}")
            raise

    def select_processing_category_in_list(self, processing_category_name:str):
        try:
            self.select_txt.click()
            count = self.dropdown.count()
            for i in range(count):
                text = self.dropdown.nth(i).inner_text().strip()
                if text.lower() == processing_category_name.lower():
                    self.dropdown.nth(i).click()
                    break
        except Exception as e:
            print(f"Exception while selecting processing category name: {e}")
            raise

    def get_add_processing_activity_confi_msg_2(self):
        try:
            return self.add_processing_activity_confi_msg_2
        except Exception as e:
            print(f" Exception while getting add processing activity confirmation message 2 : {e}")
            return None

    def processing_purpose_tab_action_1(self, processing_purpose_name:str, processing_activity_name_1:str):
        try:
            self.processing_purpose_tab.nth(1).click()
            self.add_processing_purpose_btn.click()
            self.fill_name_and_description(processing_purpose_name)
            time.sleep(1)
            self.select_processing_activity(processing_activity_name_1)
            self.expiry_days_clear_txt.clear()
            self.expiry_days_fill_txt.fill("7")
            self.save_btn.click()
        except Exception as e:
            print(f" Exception while perform processing purpose tab action 1 : {e}")
            raise

    def select_processing_activity(self, processing_activity_name_1:str):
        try:
            self.select_txt.click()
            count = self.dropdown.count()
            for i in range(count):
                text = self.dropdown.nth(i).inner_text().strip()
                if text.lower() == processing_activity_name_1.lower():
                    self.dropdown.nth(i).click()
                    break
        except Exception as e:
            print(f"Exception while selecting processing activity name: {e}")
            raise

    def get_add_processing_purpose_confi_msg(self):
        try:
            return self.add_processing_purpose_confi_msg
        except Exception as e:
            print(f" Exception while getting add processing purpose confirmation message : {e}")
            return None