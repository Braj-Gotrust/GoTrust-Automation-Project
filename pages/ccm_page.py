import time
from playwright.sync_api import Page
class CcmPage:
    def __init__(self,page: Page):
        self.page = page
        self.ccm_btn =page.locator("a span:has-text('Cookie Consent')").nth(0)
        self.ccm_title = page.locator("h1:has-text('Cookie Consent Management')")
        self.banner_builder_tab = page.locator("button:has-text('Banner Builder')")
        self.create_btn = page.locator("button:has-text('Create')")
        self.domain_name_txt = page.get_by_label("Domain Name")
        self.domain_url_txt = page.get_by_label("Domain URL")
        self.cookie_policy_link_txt = page.get_by_label("Cookie Policy Link")
        self.consent_framework_txt = page.get_by_label("Consent Framework")
        self.regulation_1 = page.locator("span:has-text('General Data Protection Regulation (GDPR)')")
        self.regulation_2 = page.locator("span:has-text('Digital Personal Data Protection Act, 2023 (DPDPA)')")
        self.close_btn = page.locator("div[role='option']:has-text('Close')")
        self.next_btn = page.locator("button:has-text('Next')")
        self.create_domain_confi_msg = page.get_by_text("Domain details updated successfully")
        # scan now
        self.switch_btn = page.locator("button[role='switch']")
        self.select_frequency_txt = page.locator("span:has-text('Select Frequency')")
        self.dropdown = page.locator("div[role='option']")
        self.scan_now_btn = page.locator("button:has-text('Scan Now')")
        # category and service tab
        self.category_and_service_tab = page.locator("button:has-text('Category & Service')")
        self.add_category_btn = page.locator("button:has-text('Add Category')")
        self.category_name_txt = page.locator("#name")
        self.description_txt = page.locator("#description")
        self.add_category_confi_msg = page.get_by_text("Category saved successfully")
        self.all_category_name = page.locator("tbody td:nth-child(1)")
        self.plus_btn = page.locator("button:has(svg.lucide-circle-plus)")
        self.service_name_txt = page.locator("#name")
        self.add_service_confi_msg = page.get_by_text("Service saved successfully")
        # unique cookies tab
        self.unique_cookies_tab = page.locator("button:has-text('Unique Cookies')")
        self.add_cookies_btn = page.locator("p:has-text('Add Cookies')")
        self.cookie_key_name_txt = page.locator("#cookie_key")
        self.path_txt = page.locator("#path")
        self.all_cookies_category = page.locator("#category_id")
        self.cookies_category_options = page.locator("#category_id option")
        self.all_cookies_service = page.locator("#cookie_service_id")
        self.cookies_service_options = page.locator("#cookie_service_id option")
        self.cookie_type_txt = page.locator("#cookie_type")
        self.cookie_regulation_txt = page.locator("#regulation_id")
        self.session_txt = page.locator("input[value='session']")
        self.domain_txt = page.locator("#scanned_cookie_domain")
        self.add_cookie_confi_msg = page.get_by_text("Cookie created successfully")
        # compliance tab
        self.compliance_tab = page.locator("button:has-text('Compliance')")
        self.observation_txt = page.locator("span:has-text('Add Audit Observation')")
        self.save_btn = page.locator("button:has-text('Save')")
        self.add_observation_confi_msg = page.get_by_text("Observation added successfully")
        # add duty
        self.observation_add_btn = page.locator("button[aria-haspopup='dialog']")
        self.add_duty_txt = page.locator("button:has-text('Add duty')")
        self.duty_title_txt = page.get_by_placeholder("Duty Title")
        self.add_assignee_txt = page.locator("span:has-text('Select Assignee')")
        # due date
        self.pick_date_start_txt = page.locator("button:has-text('Pick a date')")
        self.next_month_txt = page.locator("button[name='next-month']")
        self.date_15 = page.get_by_role("gridcell", name="15")
        self.entity_txt = page.get_by_label("Entity")
        self.standards_txt= page.get_by_placeholder("Enter your standards here...")
        self.comment_txt = page.get_by_placeholder("Enter your comments here...")
        self.add_btn = page.locator("button.gotrust-button:has-text('Add')")
        self.add_duty_confi_msg = page.get_by_text("Duty is created successfully")
        # add action
        self.add_action_txt = page.locator("button:has-text('Add action')")
        self.category_txt = page.get_by_placeholder("Category")
        self.description_txt_placeholder = page.get_by_placeholder("Description")
        self.assigned_by_txt = page.get_by_label("Assigned by")
        self.assigned_to_txt = page.get_by_label("Assigned To")
        self.add_action_confi_msg = page.get_by_text("Action Added Successfully")
        # select recommendations tab
        self.recommendations_tab = page.locator("button:has-text('Recommendations')")

        # page extend
        self.item_per_page_txt = page.locator(".lucide.lucide-chevron-down.size-4")
        self.all_domain_name = page.locator("tbody td:nth-child(1)")
        self.select_domain_name_confi = page.locator("p:has-text('Cookie Configuration')")

        # STEP:4 - User Consent Renewal
        self.user_consent_renewal_txt = page.get_by_label("User consent renewal in months:")
        # STEP:5 - Customize Banner
        self.upload_logo_txt = page.locator("img[alt='Remove Logo']")
        self.file_input_txt = page.locator("input[type='file']")
        self.logo_upload_confi_msg = page.locator("img[alt='Uploaded Logo']")
        self.checkbox = page.locator("button#terms")
        self.reset_banner_txt = page.locator("button:has-text('Reset Changes')")
        self.reset_confi_msg = page.locator("img[alt='Uploaded Logo']")
        self.banner_layout_1 = page.locator("img[alt='banner Wall']")
        self.banner_layout_2 = page.locator("img[alt='banner Corner']")
        # STEP:6 - Language Support
        self.category_tab = page.locator("button:has-text('Category')")
        self.service_tab = page.locator("button:has-text('Service')")
        self.cookie_tab = page.locator("button:has-text('Cookie')")
        self.language_btn_txt = page.locator("button[role='combobox']:nth-child(1)")
        self.save_translation_txt = page.locator("button:has-text('Save Translation')")
        self.change_language_confi_msg = page.get_by_text("Translation saved successfully")
        # STEP:7 - Consent Code
        self.banner_preview_btn = page.locator("button:has-text('Banner Preview')")
        self.details_txt = page.locator("button:has-text('Details')")
        self.about_txt = page.locator("button:has-text('About')")
        self.cross_btn = page.locator("span:has-text('Close')")

        # cookie policy
        self.cookie_dictionary_tab = page.locator("button:has-text('Cookie Dictionary')")
        self.user_guide_tab = page.locator("button:has-text('User Guide')")
        self.analytics_tab = page.locator("button:has-text('Analytics')")
        self.consent_records_tab = page.locator("button:has-text('Consent Records')")
        self.cookie_policy_tab = page.locator("button:has-text('Cookie Policy')")
        self.select_domain_txt = page.locator("button:has-text('Select Domain')")
        self.cookie_policy_title_txt = page.get_by_placeholder("Enter cookie policy title")
        self.introduction_txt = page.locator("h2:has-text('1. Introduction')")
        self.add_cookie_table_btn = page.locator("button:has-text('Add cookie table')")
        self.add_cookie_table_confi_msg = page.get_by_text("Table added successfully")
        self.cookie_policy_create_confi_msg = page.get_by_text("Policy Created Successfully")





    def click_ccm_btn(self):
        try:
            self.ccm_btn.click()
            self.ccm_btn.click()
        except Exception as e:
            print(f" Exception while click on ccm button : {e}")
            raise

    def get_ccm_title(self):
        try:
            return self.ccm_title
        except Exception as e:
            print(f" Exception while fetching ccm title: {e}")
            return None

    def click_banner_builder_tab(self):
        try:
            self.banner_builder_tab.click()
        except Exception as e:
            print(f" Exception while click on banner builder tab : {e}")
            raise

    def fill_domain_details(self, domain_name: str, domain_url: str, cookie_policy_link: str):
        try:
            self.create_btn.click()
            time.sleep(1)
            self.domain_name_txt.fill(domain_name)
            self.domain_url_txt.fill(domain_url)
            self.cookie_policy_link_txt.fill(cookie_policy_link)
            self.consent_framework_txt.click()
            self.regulation_1.click()
            self.regulation_2.click()
            self.close_btn.click()
            self.next_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while filling domain details : {e}")
            raise

    def get_create_domain_confi_msg(self):
        try:
            return self.create_domain_confi_msg
        except Exception as e:
            print(f" Exception while getting create domain confirmation successful message : {e}")
            return None

    def click_scan_now_btn(self):
        try:
            self.switch_btn.click()
            self.select_frequency_txt.click()
            self.dropdown.nth(2).click()
            self.scan_now_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while click on scan now button : {e}")
            raise

    def click_next_btn(self):
        try:
            self.next_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while click on next button : {e}")
            raise

    def click_category_and_service_tab(self):
        try:
            self.category_and_service_tab.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while click on category and service tab : {e}")
            raise

    def fill_category_details(self, category_name:str, category_description:str):
        try:
            self.add_category_btn.click()
            self.category_name_txt.fill(category_name)
            self.description_txt.fill(category_description)
            self.create_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while filling category details : {e}")
            raise

    def get_add_category_confi_msg(self):
        try:
            return self.add_category_confi_msg
        except Exception as e:
            print(f" Exception while getting add category confirmation successful message : {e}")
            return None

    def select_category(self,category_name:str):
        try:
            count = self.all_category_name.count()
            for i in range(count):
                text = self.all_category_name.nth(i).inner_text().strip()
                if text.lower() == category_name.lower():
                    self.plus_btn.nth(i).click()
                    time.sleep(1)
                    break
        except Exception as e:
            print(f" Exception while selecting category name : {e}")
            raise

    def fill_service_details(self,service_name:str, service_description:str):
        try:
            self.service_name_txt.fill(service_name)
            self.description_txt.fill(service_description)
            self.create_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while filling service details : {e}")
            raise

    def get_add_service_confi_msg(self):
        try:
            return self.add_service_confi_msg
        except Exception as e:
            print(f" Exception while getting add service confirmation successful message : {e}")
            return None

    def click_unique_cookies_tab(self):
        try:
            self.unique_cookies_tab.click()
        except Exception as e:
            print(f" Exception while click on unique cookies tab : {e}")
            raise

    def fill_cookie_details(self, cookie_key_name:str, cookie_key_description:str, category_name:str, service_name:str):
        try:
            self.add_cookies_btn.click()
            self.cookie_key_name_txt.fill(cookie_key_name)
            self.description_txt.fill(cookie_key_description)
            self.path_txt.fill("/")
            self.select_cookie_category(category_name)
            self.select_cookie_service(service_name)
            self.select_cookie_type()
            self.select_cookie_regulation()
            self.session_txt.click()
            self.domain_txt.fill("braj/test.com")
            if category_name == "Essential":
                self.switch_btn.nth(0).click()
            self.create_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while filling category details : {e}")
            raise

    def select_cookie_category(self,category_name:str):
        try:
            count = self.cookies_category_options.count()
            for i in range(count):
                text = self.cookies_category_options.nth(i).inner_text().strip()
                if text.lower() == category_name.lower():
                    value = self.cookies_category_options.nth(i).get_attribute("value")
                    self.all_cookies_category.select_option(value=value)
                    time.sleep(1)
                    break
        except Exception as e:
            print(f" Exception while selecting cookies category name : {e}")
            raise

    def select_cookie_service(self,service_name:str):
        try:
            count = self.cookies_service_options.count()
            for i in range(count):
                text = self.cookies_service_options.nth(i).inner_text().strip()
                if text.lower() == service_name.lower():
                    value = self.cookies_service_options.nth(i).get_attribute("value")
                    self.all_cookies_service.select_option(value=value)
                    time.sleep(1)
                    break
        except Exception as e:
            print(f" Exception while selecting cookies service name : {e}")
            raise

    def select_cookie_type(self):
        try:
            self.cookie_type_txt.select_option(value="first-party")
        except Exception as e:
            print(f" Exception while selecting cookies type name : {e}")
            raise

    def select_cookie_regulation(self):
        try:
            self.cookie_regulation_txt.select_option(value="121")
        except Exception as e:
            print(f" Exception while selecting cookies type name : {e}")
            raise

    def get_add_cookie_confi_msg(self):
        try:
            return self.add_cookie_confi_msg
        except Exception as e:
            print(f" Exception while getting add cookie confirmation successful message : {e}")
            return None

    def click_compliance_tab(self):
        try:
            self.compliance_tab.click()
        except Exception as e:
            print(f" Exception while click on compliance tab : {e}")
            raise

    def fill_observation_details(self):
        try:
            time.sleep(3)
            self.observation_txt.nth(0).click()
            self.description_txt.fill("observation")
            self.save_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while click on compliance tab : {e}")
            raise

    def get_add_observation_confi_msg(self):
        try:
            return self.add_observation_confi_msg
        except Exception as e:
            print(f" Exception while getting observation added confirmation successful message : {e}")
            return None

    def fill_duty_details(self):
        try:
            self.observation_add_btn.nth(0).click()
            self.add_duty_txt.click()
            self.duty_title_txt.fill("duty")
            self.add_assignee_txt.click()
            self.dropdown.nth(1).click()
            self.close_btn.click()
            self.select_pick_date_start()
            self.select_entity()
            self.standards_txt.fill("standards")
            self.comment_txt.fill("comments")
            self.add_btn.click()
            time.sleep(3)
        except Exception as e:
            print(f" Exception while click on compliance tab : {e}")
            raise

    def select_pick_date_start(self):
        try:
            self.pick_date_start_txt.nth(0).click()
            self.next_month_txt.click()
            self.date_15.click()
        except Exception as e:
            print(f" Exception while selecting date for start assessment : {e}")
            raise

    def select_entity(self):
        try:
            self.entity_txt.click()
            self.dropdown.nth(1).click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while selecting date for start assessment : {e}")
            raise

    def get_add_duty_confi_msg(self):
        try:
            return self.add_duty_confi_msg
        except Exception as e:
            print(f" Exception while getting add duty confirmation successful message : {e}")
            return None

    def fill_action_details(self):
        try:
            self.observation_add_btn.nth(0).click()
            self.add_action_txt.click()
            self.category_txt.fill("category")
            self.description_txt_placeholder.fill("test")
            self.select_entity()
            self.select_pick_date_start()
            self.assigned_by_txt.click()
            self.dropdown.nth(1).click()
            self.assigned_to_txt.click()
            self.dropdown.nth(1).click()
            self.select_pick_date_start()
            time.sleep(1)
            self.select_pick_date_start()
            self.add_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while fill action details : {e}")
            raise

    def get_add_action_confi_msg(self):
        try:
            return self.add_action_confi_msg
        except Exception as e:
            print(f" Exception while getting add action confirmation successful message : {e}")
            return None

    def click_recommendations_tab(self):
        try:
            self.recommendations_tab.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while click on recommendations tab : {e}")
            raise

    def take_user_consent_renewal(self):
        try:
            self.user_consent_renewal_txt.click()
            self.dropdown.nth(20).click()
            self.next_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while taking user consent renewal : {e}")
            raise

    def select_domain(self, domain_name: str):
        try:
            domain_count = self.all_domain_name.count()
            for i in range(domain_count):
                text = self.all_domain_name.nth(i).inner_text()
                if text == domain_name:
                    self.all_domain_name.nth(i).click()
                    break
            time.sleep(1)
        except Exception as e:
            print(f"Exception while selecting domain name: {e}")
            raise

    def get_select_domain_name_confi(self):
        try:
            return self.select_domain_name_confi
        except Exception as e:
            print(f" Exception while fetching domain name title: {e}")
            return None

    def page_extend(self):
        try:
            self.item_per_page_txt.click()
            self.dropdown.nth(4).click()
            time.sleep(1)
        except Exception as e:
            print(f"Exception while page extend: {e}")
            raise

    def upload_logo(self, file_path: str):
        try:
            self.upload_logo_txt.click()
            self.file_input_txt.set_input_files(file_path)
            time.sleep(1)
        except Exception as e:
            print(f"Exception while uploading logo: {e}")
            raise

    def get_logo_upload_confi_msg(self):
        try:
            return self.logo_upload_confi_msg
        except Exception as e:
            print(f" Exception while fetching upload logo message successfully: {e}")
            return None

    def select_checkbox(self):
        try:
            self.checkbox.wait_for(state="visible")
            if self.checkbox.get_attribute("aria-checked") != "true":
                self.checkbox.click()
            time.sleep(1)
        except Exception as e:
            print(f"Exception while selecting checkbox: {e}")
            raise

    def click_reset_banner_btn(self):
        try:
            self.reset_banner_txt.click()
            time.sleep(1)
        except Exception as e:
            print(f"Exception while click on reset banner button: {e}")
            raise

    def get_reset_confi_msg(self):
        try:
            return self.reset_confi_msg
        except Exception as e:
            print(f" Exception while fetching reset confirmation message successfully: {e}")
            return None

    def customize_banner(self, file_path: str):
        try:
            self.upload_logo(file_path)
            self.select_checkbox()
            self.switch_btn.nth(2).click()
            self.switch_btn.nth(4).click()
            self.switch_btn.nth(5).click()
            self.switch_btn.nth(6).click()
            self.banner_layout_1.click()
            self.banner_layout_2.click()
            self.switch_btn.nth(0).click()
        except Exception as e:
            print(f" Exception while customization banner : {e}")
            raise

    def change_language(self):
        try:
            self.category_tab.click()
            self.service_tab.click()
            self.cookie_tab.click()
            self.language_btn_txt.click()
            self.dropdown.filter(has_text="Dutch").click()
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

    def click_banner_preview_btn(self):
        try:
            self.banner_preview_btn.click()
            # self.details_txt.click()
            # self.about_txt.click()
            self.cross_btn.click()
            self.save_btn.click()
        except Exception as e:
            print(f" Exception while click on banner preview button : {e}")
            raise

    def click_all_cookie_policy_tab(self):
        try:
            self.click_banner_builder_tab()
            self.cookie_dictionary_tab.click()
            self.user_guide_tab.click()
            self.analytics_tab.click()
            self.consent_records_tab.click()
        except Exception as e:
            print(f" Exception while click on ccm button : {e}")
            raise

    def click_cookie_policy_tab(self):
        try:
            self.cookie_policy_tab.click()
        except Exception as e:
            print(f" Exception while click on cookie policy tab : {e}")
            raise

    def create_cookie_policy(self, domain_name: str, cookie_policy_title: str):
        try:
            self.create_btn.click()
            self.select_domain_name(domain_name)
            self.next_btn.click()
            self.fill_details_by_keyboard_actions(cookie_policy_title)
        except Exception as e:
            print(f" Exception while create cookie policy : {e}")
            raise

    def select_domain_name(self, domain_name: str):
        try:
            self.select_domain_txt.click()
            self.page.wait_for_selector("div[role='option']")
            count = self.dropdown.count()
            found = False
            print("\ndomain count :", count)
            for i in range(count):
                text = self.dropdown.nth(i).inner_text()
                if text == domain_name:
                    print("\ndomain name :", text)
                    self.page.wait_for_selector("div[role='option']")
                    self.dropdown.nth(i).click()
                    found = True
                    break
            if not found:
                self.dropdown.nth(1).click()
        except Exception as e:
            print(f"Exception while selecting domain name : {e}")
            raise

    def fill_details_by_keyboard_actions(self, cookie_policy_title: str):
        try:
            self.cookie_policy_title_txt.focus()
            self.page.keyboard.insert_text(cookie_policy_title)
            self.page.keyboard.press("Tab")
            self.page.keyboard.press("Enter")
            self.dropdown.nth(0).click()
            self.introduction_txt.click()
            self.page.keyboard.press("Enter")
            self.add_cookie_table_btn.click()
        except Exception as e:
            print(f" Exception while fill details cookie policy : {e}")
            raise

    def get_add_cookie_table_confi_msg(self):
        try:
            return self.add_cookie_table_confi_msg
        except Exception as e:
            print(f" Exception while getting add cookie table confirmation successful message : {e}")
            return None

    def click_save_change_btn(self):
        try:
            self.save_btn.click()
        except Exception as e:
            print(f" Exception while click on save change button : {e}")
            raise

    def click_close_btn(self):
        try:
            self.cross_btn.click()
        except Exception as e:
            print(f" Exception while click on close button : {e}")
            raise

    def get_cookie_policy_create_confi_msg(self):
        try:
            return self.cookie_policy_create_confi_msg
        except Exception as e:
            print(f" Exception while getting cookie policy create confirmation successful message : {e}")
            return None






