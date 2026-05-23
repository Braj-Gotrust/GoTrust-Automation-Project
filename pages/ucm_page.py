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
        self.name_txt = page.locator("#name, #pp-name")
        self.description_txt = page.locator("#description, #pp-description, .tiptap")
        self.add_processing_category_confi_msg = page.get_by_text("Processing category added successfully")
        self.item_per_page_txt = page.locator("span button[role='combobox']")
        self.dropdown = page.locator("div[role='option']")
        self.all_processing_category = page.locator("table tbody tr p")
        self.plus_btn = page.locator("button:has(svg.lucide-plus)")
        self.add_btn = page.locator("button:has-text('Add')")
        self.add_processing_activity_confi_msg_1 = page.get_by_text("Processing activity added successfully")
        # Processing Activities Tab
        self.processing_activity_tab = page.locator("a:has-text('Processing Activities')")
        self.add_processing_activities_btn = page.locator("button:has-text('Add Processing Activities')")
        self.add_processing_activity_confi_msg_2 = page.get_by_text("Processing activity added successfully")
        # Processing Purpose Tab
        self.processing_purpose_tab = page.locator("a:has-text('Processing Purpose')")
        self.add_processing_purpose_btn = page.locator("button:has-text('Add Processing Purpose')")
        self.expiry_days_clear_txt = page.locator("input[placeholder='Enter expiry']")
        self.expiry_days_fill_txt = page.locator("input[placeholder='Enter expiry']")
        self.add_processing_purpose_confi_msg = page.get_by_text("Processing purpose added successfully")

        # privacy notice
        self.task_overview_btn = page.locator("span:has-text('Task Overview')")
        self.privacy_notice = page.locator("a:has-text('Privacy Notice')")
        self.create_btn = page.locator("button:has-text('Create')")
        self.select_txt = page.locator("span:has-text('Select')")
        self.notice_name_txt = page.locator("input[placeholder='Enter Privacy Notice Title']")
        self.privacy_notice_description = page.locator(".tiptap")
        self.privacy_notice_save_confi_msg = page.get_by_text("Privacy notice saved successfully")

        # consent form
        self.consent_collection_builder_btn = page.locator("span:has-text('Consent Collection Builder')")
        self.create_consent_collection_temp_btn = page.locator("button:has-text('Create Consent Collection Template')")
        # step 1 - Basic Info
        self.template_name_txt = page.locator("input[placeholder='Enter Template Name']")
        self.unique_data_identifier_txt = page.get_by_label("Unique Data Identifier Type").or_(page.locator("span:has-text('Select')"))
        self.continue_btn = page.locator("button:has-text('Continue')")
        self.record_create_confirmation_msg = page.get_by_text("Record Created Successfully")
        # step 2 - Processing Purpose

        # step 3 - Privacy Notice
        self.exist_btn = page.locator("button:has-text('Existing')")

        # step 4 - Sources or consent form
        self.input_field_txt = page.locator("input[type='text']")
        self.next_btn = page.locator("button:has-text('Next')")
        self.customize_form_txt = page.locator("button:has-text('Customize Form - Desktop')")
        self.remove_logo = page.locator("img[alt='Remove Logo'], button:has(svg.lucide-x):nth-child(2)")
        self.file_input = page.locator("input[type='file']")
        self.logo_upload_confi_attribute = page.locator("img[alt='Uploaded Logo']")
        self.reset_btn = page.locator("button:has-text('Reset')")
        self.reset_confirmation_attribute = page.locator("img[src='/assets/svg/gotrustTitle_light.DIPQ8Yl4.svg']")
        self.switch_btn = page.locator("button[role='switch']")

        # step 5 - Preference Center
        self.all_consent_template_name = page.locator("table tbody tr td:first-child div")
        self.consent_template_title = page.get_by_text("Create Consent Collection Template")
        self.preference_center_title_txt = page.get_by_label("Preference Center Title")
        self.new_btn = page.locator("button:has-text('New')")
        self.full_screen_btn = page.locator("button:has-text('View on full screen')")
        self.cross_btn = page.locator("span:has-text('Close')")
        self.verify_input_tab = page.locator("button:has-text('Verify Input')")
        self.swap_button_order =  page.locator("button:has-text('Swap Button Order')")
        self.preference_center_tab = page.locator("button:has-text('Preference Center')")
        self.consent_preference_tab = page.locator("button:has-text('Consent Preferences')")
        self.dsr_tab = page.locator("button:has-text('DSR')")
        self.consent_flow_tab = page.locator("button:has-text('Consent Flow')")

        # step 6 - Language
        self.consent_form_tab = page.locator("button:has-text('Consent Form')")
        self.preference_form_tab = page.locator("button:has-text('Preference Form')")
        self.language_btn_txt = page.locator("button[role='combobox']:nth-child(1)")
        self.save_translation_txt = page.locator("button:has-text('Save Translation')")
        self.change_language_confi_msg = page.get_by_text("Translations saved successfully")

        # step - 7 Code Snippets
        self.mobile_consent_sdk_tab = page.locator("button:has-text('Mobile Consent SDK')")
        self.web_preference_center_tab = page.locator("button:has-text('Web Preference Center')")
        self.mobile_preference_sdk_tab = page.locator("button:has-text('Mobile Preference SDK')")
        self.download_btn = page.locator("button:has-text('Download Guide')")
        self.download_title_txt = page.locator("h2:has-text('Download Integration Guide')")
        self.download_cross_btn = page.locator("button:has(svg.lucide-x)")
        ucm_title = page.locator("a:has-text('Universal Consent Management')")


    def click_code_snippets_page_tab(self):
        try:
            self.mobile_consent_sdk_tab.click()
            time.sleep(1)
            self.web_preference_center_tab.click()
            time.sleep(1)
            self.mobile_preference_sdk_tab.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while click on step - 7 code snippets page tab : {e}")
            raise

    def click_download_btn(self):
        try:
            self.download_btn.click()
        except Exception as e:
            print(f" Exception while click on download button : {e}")
            raise

    def get_download_title_txt(self):
        try:
            return self.download_title_txt
        except Exception as e:
            print(f" Exception while getting download title text : {e}")
            return None

    def click_download_cross_btn(self):
        try:
            self.download_cross_btn.click()
        except Exception as e:
            print(f" Exception while click on download cross button : {e}")
            raise















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

    def select_pii_label_in_table(self,pii_label_name:str):
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


    def click_task_overview_btn(self):
        try:
            self.task_overview_btn.nth(2).click()
            self.task_overview_btn.nth(2).click()
            time.sleep(3)
        except Exception as e:
            print(f" Exception while click on pii inventory button : {e}")
            raise

    def get_privacy_notice_title(self):
        try:
            return self.privacy_notice
        except Exception as e:
            print(f" Exception while getting privacy notice title : {e}")
            return None

    def create_privacy_notice(self, legal_entity_name:str, privacy_notice_name:str):
        try:
            self.create_btn.click()
            self.select_legal_entity(legal_entity_name)
            # select department
            self.select_txt.nth(0).click()
            self.dropdown.nth(1).click()
            # fill privacy notice name and description
            self.notice_name_txt.fill(privacy_notice_name)
            self.privacy_notice_description.fill("This a privacy notice description")
            self.click_save_btn()

        except Exception as e:
            print(f" Exception while click on pii inventory button : {e}")
            raise

    def select_legal_entity(self, legal_entity_name: str):
        try:
            self.select_txt.nth(0).click()
            self.page.wait_for_selector("[role='option']")
            option = self.dropdown.filter(has_text=legal_entity_name)

            if option.is_visible():
                option.click()
            else:
                print(f" {legal_entity_name} not found, selecting Gotrust option")
                self.dropdown.nth(1).click()

        except Exception as e:
            print(f"Exception while selecting legal entity name: {e}")
            raise

    def get_privacy_notice_save_confi_msg(self):
        try:
            return self.privacy_notice_save_confi_msg
        except Exception as e:
            print(f" Exception while getting privacy notice save confirmation message : {e}")
            return None

    def click_consent_collection_builder_btn(self):
        try:
            self.consent_collection_builder_btn.click()
            self.consent_collection_builder_btn.click()
        except Exception as e:
            print(f" Exception while click on pii inventory button : {e}")
            raise

    def click_create_consent_template(self, consent_template_name:str, legal_entity_name:str, pii_label_name:str):
        try:
            self.create_consent_collection_temp_btn.click()
            self.template_name_txt.fill(consent_template_name)
            self.select_legal_entity(legal_entity_name)
            # select owner
            self.select_txt.nth(0).click()
            self.dropdown.nth(1).click()
            # select unique data identifier
            self.unique_data_identifier_txt.first.click()
            self.select_pii_label_in_list(pii_label_name)
        except Exception as e:
            print(f" Exception while click on pii inventory button : {e}")
            raise

    def select_pii_label_in_list(self, pii_label_name: str):
        try:
            self.page.wait_for_selector("[role='option']")
            option = self.dropdown.filter(has_text=pii_label_name)
            if option.is_visible():
                option.click()
            else:
                print(f" {pii_label_name} is not found")
        except Exception as e:
            print(f"Exception while selecting pii label name: {e}")
            raise

    def click_continue_btn(self):
        try:
            self.continue_btn.click()
        except Exception as e:
            print(f" Exception while click on continue button : {e}")
            raise

    def get_record_create_confirmation_msg(self):
        try:
            return self.record_create_confirmation_msg
        except Exception as e:
            print(f" Exception while getting record create success confirmation message in step 1 : {e}")
            return None

    def add_processing_purpose(self, processing_purpose_name:str, pii_label_name:str):
        try:
            self.add_processing_purpose_btn.click()
            # select processing purpose
            self.select_txt.nth(0).click()
            self.select_processing_purpose(processing_purpose_name)
            self.add_btn.nth(1).click()
            # select pii label
            self.select_txt.nth(0).click()
            self.select_pii_label_in_list(pii_label_name)
            self.save_btn.nth(1).click()
            time.sleep(3)
            self.save_btn.nth(0).click()
        except Exception as e:
            print(f" Exception while add on processing purpose : {e}")
            raise

    def select_processing_purpose(self, processing_purpose_name):
        try:
            self.page.wait_for_selector("[role='option']")
            option = self.dropdown.filter(has_text=processing_purpose_name)
            if option.is_visible():
                option.click()
            else:
                print(f" {processing_purpose_name} is not found")
        except Exception as e:
            print(f"Exception while selecting processing purpose name: {e}")
            raise

    def click_exist_btn(self):
        try:
            self.exist_btn.click()
        except Exception as e:
            print(f" Exception while click on exist button : {e}")
            raise


    def select_privacy_notice(self, privacy_notice_name:str):
        try:
            self.select_txt.nth(0).click()
            self.page.wait_for_selector("[role='option']")
            option = self.dropdown.filter(has_text=privacy_notice_name)
            if option.is_visible():
                option.click()
            else:
                print(f" {privacy_notice_name} is not found")
        except Exception as e:
            print(f"Exception while selecting privacy notice name: {e}")
            raise

    def select_source(self, source_name:str):
        try:
            self.select_txt.nth(0).click()
            self.page.wait_for_selector("[role='option']")
            option = self.dropdown.filter(has_text=source_name)
            if option.is_visible():
                option.click()
            else:
                print(f" {source_name} is not found")
        except Exception as e:
            print(f"Exception while selecting source name: {e}")
            raise

    def fill_consent_form_title_and_description(self):
        try:
            self.input_field_txt.nth(1).fill("consent form title 1")
            self.input_field_txt.nth(2).fill("consent form description 1")
        except Exception as e:
            print(f"Exception while selecting source name: {e}")
            raise

    def click_next_btn(self):
        try:
            self.next_btn.click()
        except Exception as e:
            print(f" Exception while click on next button : {e}")
            raise

    def click_customize_form_txt(self):
        try:
            self.customize_form_txt.click()
        except Exception as e:
            print(f" Exception while click on customize form text : {e}")
            raise

    def upload_logo(self, file_path: str):
        try:
            time.sleep(2)
            self.remove_logo.click()
            time.sleep(2)
            self.file_input.set_input_files(file_path)
        except Exception as e:
            print(f"Exception while uploading logo: {e}")
            raise

    def get_logo_upload_confi_attribute(self):
        try:
            return self.logo_upload_confi_attribute
        except Exception as e:
            print(f" Exception while getting logo upload confirmation success attribute : {e}")
            return None

    def click_reset_btn(self):
        try:
            self.reset_btn.click()
        except Exception as e:
            print(f" Exception while click on reset button : {e}")
            raise

    def get_reset_confirmation_attribute(self):
        try:
            return self.reset_confirmation_attribute
        except Exception as e:
            print(f" Exception while getting reset confirmation attribute : {e}")
            return None

    def click_switch_btn(self):
        try:
            self.switch_btn.nth(0).click()
        except Exception as e:
            print(f" Exception while click on switch button : {e}")
            raise

    def select_consent_template(self, consent_template_name):
        try:
            count = self.all_consent_template_name.count()
            for i in range(count):
                text = self.all_consent_template_name.nth(i).inner_text().strip()
                if text.lower() == consent_template_name.lower():
                    print("\template name : ", text)
                    self.all_consent_template_name.nth(i).click()
                    break
        except Exception as e:
            print(f"Exception while selecting consent template name: {e}")
            raise

    def get_consent_template_title(self):
        try:
            return self.consent_template_title
        except Exception as e:
            print(f" Exception while getting select consent template title/text : {e}")
            return None

    def enter_preference_center_title(self, preference_center_title_name:str):
        try:
            if self.input_field_txt.nth(1).is_visible():
                self.input_field_txt.nth(1).fill(preference_center_title_name)
                time.sleep(1)
                self.next_btn.click()
            if self.new_btn.is_visible():
                self.new_btn.click()
                self.input_field_txt.nth(1).fill(preference_center_title_name)
                time.sleep(1)
                self.next_btn.click()
        except Exception as e:
            print(f" Exception while enter preference center title name : {e}")
            raise

    def click_full_screen_btn(self):
        try:
            self.full_screen_btn.click()
        except Exception as e:
            print(f" Exception while click on full screen button : {e}")
            raise

    def click_cross_btn(self):
        try:
            self.cross_btn.click()
        except Exception as e:
            print(f" Exception while click on cross button : {e}")
            raise

    def click_verify_input_tab(self):
        try:
            self.verify_input_tab.nth(0).click()
        except Exception as e:
            print(f" Exception while click on verify input tab : {e}")
            raise

    def click_swap_button_order(self):
        try:
            self.swap_button_order.click()
            time.sleep(1)
            self.swap_button_order.click()
        except Exception as e:
            print(f" Exception while click on swap button order : {e}")
            raise

    def click_preference_center_tab(self):
        try:
            self.preference_center_tab.nth(1).click()
        except Exception as e:
            print(f" Exception while click on preference center tab : {e}")
            raise

    def click_preference_center_page_tab(self):
        try:
            self.consent_preference_tab.nth(1).click()
            time.sleep(1)
            self.dsr_tab.click()
            time.sleep(1)
            self.consent_flow_tab.click()
        except Exception as e:
            print(f" Exception while click on preference center tab : {e}")
            raise

    def change_language(self):
        try:
            self.consent_form_tab.nth(0).click()
            time.sleep(2)
            self.preference_form_tab.nth(0).click()
            time.sleep(2)
            self.language_btn_txt.click()
            self.dropdown.filter(has_text="Hindi").click()
            self.save_translation_txt.click()
        except Exception as e:
            print(f" Exception while change language : {e}")
            raise

    def get_change_language_confi_msg(self):
        try:
            return self.change_language_confi_msg
        except Exception as e:
            print(f" Exception while getting change language confirmation successful message : {e}")
            return None






