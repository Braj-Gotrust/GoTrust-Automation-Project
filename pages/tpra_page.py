import re
import time
from os import name

from playwright.sync_api import Page,expect

class TpraPage:
    def __init__(self,page: Page):
        self.page = page
        self.tpra_btn =page.locator("a span:has-text('TPRA')").nth(0)
        self.tpra_title = page.locator("h1:has-text('Third Party Risk Assessment')")
        self.add_vendor_btn = page.locator("button:has-text('Add Vendor')")
        # vendor locators
        self.vendor_name_txt = page.get_by_placeholder("Enter vendor name")
        self.vendor_email_txt = page.get_by_placeholder("Enter email").nth(0)
        self.vendor_address_txt =  page.get_by_placeholder("Enter address")
        self.vendor_admin_name_txt = page.get_by_placeholder("Enter admin name")
        self.vendor_phone_number_txt = page.get_by_placeholder("Enter phone number")
        self.legal_entities_txt = page.locator("span:has-text('Select legal entities')")
        self.legal_entities_dropdown = page.locator("div[role='group'] span")
        self.close_btn = page.locator("div[role='option']:has-text('Close')")
        self.save_and_continue_btn = page.locator("button:has-text('Save and continue')")
        self.vendor_add_confi_msg = page.get_by_text("Vendor added successfully")
        # vendor list
        self.vendor = page.locator("tbody tr")
        self.vendor_name_list = page.locator("tbody tr td:first-child span")
        self.start_vendor_assessment_btn = page.locator("button:has-text('Start Vendor Assessment')")
        self.vendor_assessment_description = page.get_by_placeholder("Description")
        self.legal_entity_txt = page.locator("span:has-text('Select legal entity')")
        self.legal_entity_dropdown = page.locator("div[role='option'] span span")
        self.departments_txt = page.locator("span:has-text('Select departments')")
        self.departments_dropdown = page.locator("div[role='option'] span")
        self.spoc_txt = page.locator("span:has-text('Select Internal SPOC')")
        self.spoc_dropdown = page.locator("div[role='option'] span:nth-child(2)")
        self.type_of_vendor_txt = page.get_by_label("Types of Vendor")
        self.type_of_vendor_dropdown = page.locator("div[role='option'] span:nth-child(2)")
        self.intake_temp_txt = page.locator("span:has-text('Select Intake Template')")
        self.intake_temp_dropdown = page.locator("div[role='option'] span:nth-child(2)")
        self.pick_date_start_txt = page.locator("button:has-text('Pick a date')")
        self.next_month_txt = page.locator("button[name='next-month']")
        self.date_15 = page.get_by_role("gridcell", name="15")
        self.date_10 = page.get_by_role("gridcell", name="10")
        self.pick_date_end_txt = page.get_by_label("Vendor Risk Assessment Due Date")
        self.assignee_txt = page.locator("span:has-text('Select assignee name')")
        self.assignee_dropdown = page.locator("div[role='option'] span:nth-child(2)")
        self.reviewer_txt = page.locator("span:has-text('Select reviewer name')")
        self.reviewer_dropdown = page.locator("div[role='option'] span:nth-child(2)")
        self.vendor_assessment_confi_msg = page.get_by_text("Assessment created successfully")
        # vendor assessment
        self.vendor_assess_txt = page.locator("tbody tr td:first-child")
        self.save_and_next_btn = page.locator("button:has-text('Save and Next')")
        # add collaborator
        self.add_collaborator_btn = page.locator("button:has-text('Add Collaborator')")
        self.add_collaborator_txt = page.locator("button:has-text('Select collaborators')")
        self.collaborator_dropdown = page.locator("div[role='group'] span")
        self.collaborator_submit_btn = page.locator("//button[normalize-space()='Submit']")
        self.collaborator_add_confi_msg = page.get_by_text("Collaborator added successfully!")
        # questions and answers
        self.questions = page.locator("button[role='combobox']")
        self.answers = page.locator("div[role='option']:visible")
        self.save_btn = page.locator("button:has-text('Save')")
        self.save_msg = page.get_by_text("Saved successfully").first
        self.submit_for_review_btn = page.locator("button:has-text('Submit for Review')")
        # reviewer review all questions and answers
        self.all_yes_button = page.locator("label:has-text('Yes')")


    def review_questions_and_answers(self):
        try:
            count_yes_btn = self.all_yes_button.count()
            for i in range(count_yes_btn):
                self.all_yes_button.nth(i).click()
        except Exception as e:
            print(f" Exception while review all questions and answers : {e}")
            raise


    def click_tpra_btn(self):
        try:
            self.tpra_btn.click()
            self.tpra_btn.click()
        except Exception as e:
            print(f" Exception while clicking TPRA button : {e}")
            raise

    def get_tpra_title(self):
        try:
            return self.tpra_title
        except Exception as e:
            print(f" Exception while fetching TPRA title: {e}")
            return None

    def fill_vendor_details(self,name:str, email:str, address:str, admin_name:str, phone:str ,legal_entity_name:str):
        try:
            self.add_vendor_btn.click()
            self.vendor_name_txt.fill(name)
            self.vendor_email_txt.fill(email)
            self.vendor_address_txt.fill(address)
            self.vendor_admin_name_txt.fill(admin_name)
            self.vendor_phone_number_txt.fill(phone)
            self.select_legal_entities(legal_entity_name)
            self.save_and_continue_btn.click()
        except Exception as e:
            print(f" Exception while filling vendor details : {e}")
            raise

    def select_legal_entities(self,legal_entity_name:str):
        try:
            self.legal_entities_txt.click()
            count = self.legal_entities_dropdown.count()
            found = False
            for i in range(count):
                dropdown_text = self.legal_entities_dropdown.nth(i).inner_text()
                if dropdown_text == legal_entity_name:
                    self.legal_entities_dropdown.nth(i).click()
                    self.close_btn.click()
                    found = True
                    break
            if not found:
                self.legal_entities_dropdown.nth(1).click()
                self.close_btn.click()
        except Exception as e:
            print(f" Exception while selecting legal entities name : {e}")
            raise

    def get_vendor_add_confi_msg(self):
        try:
            return self.vendor_add_confi_msg
        except Exception as e:
            print(f" Exception while getting vendor confirmation message : {e}")
            return None

    # select the vendor name assessment under the 'TPRA dashboard'
    def select_vendor_name_assessment(self, vendor_name:str):
        try:
            self.vendor.first.wait_for(state="visible", timeout=15000)
            count_vendor = self.vendor_name_list.count()
            for i in range(count_vendor):
                text = self.vendor_name_list.nth(i).inner_text()
                if vendor_name in text:
                    self.vendor_name_list.nth(i).click()
                    break
        except Exception as e:
            print(f" Exception while selection vendor name assessment : {e}")
            raise


    def fill_vendor_assessment_details(self, description:str, legal_entity_name:str, spoc_name:str, assignee_name:str, reviewer_name:str):
        try:
            self.start_vendor_assessment_btn.click()
            self.vendor_assessment_description.fill(description)
            self.select_legal_entity(legal_entity_name)
            self.select_departments()
            self.select_spoc(spoc_name)
            self.select_type_of_vendor()
            self.select_intake_temp()
            self.select_pick_date_start()
            self.select_pick_date_end()
            self.select_assignee(assignee_name)
            self.select_reviewer(reviewer_name)
            self.save_and_continue_btn.click()
        except Exception as e:
            print(f" Exception while filling vendor assessment details : {e}")
            raise

    def select_legal_entity(self,legal_entity_name:str):
        try:
            self.legal_entity_txt.click()
            count = self.legal_entity_dropdown.count()
            found = False
            for i in range(count):
                dropdown_text = self.legal_entity_dropdown.nth(i).inner_text()
                if dropdown_text == legal_entity_name:
                    self.legal_entity_dropdown.nth(i).click()
                    found = True
                    break
            if not found:
                self.legal_entity_dropdown.nth(0).click()
        except Exception as e:
            print(f" Exception while selecting legal entity name : {e}")
            raise

    def select_departments(self):
        try:
            self.departments_txt.click()
            self.departments_dropdown.nth(0).click()
            self.close_btn.click()
        except Exception as e:
            print(f" Exception while selecting departments : {e}")
            raise

    def select_spoc(self, spoc_name:str):
        try:
            self.spoc_txt.click()
            count = self.spoc_dropdown.count()
            found = False
            for i in range(count):
                time.sleep(1)
                text = self.spoc_dropdown.nth(i).inner_text()
                if spoc_name in text:
                    self.spoc_dropdown.nth(i).click()
                    found = True
                    break
            if not found:
                self.spoc_dropdown.nth(0).click()
        except Exception as e:
            print(f" Exception while selecting SPOC : {e}")
            raise

    def select_type_of_vendor(self):
        try:
            self.type_of_vendor_txt.click()
            self.type_of_vendor_dropdown.nth(2).click()
        except Exception as e:
            print(f" Exception while selecting type of vendor : {e}")
            raise

    def select_intake_temp(self):
        try:
            self.intake_temp_txt.click()
            count = self.intake_temp_dropdown.count()
            for i in range(count):
                dropdown_text = self.intake_temp_dropdown.nth(i).inner_text()
                if dropdown_text == "Intake Assessment(Default)":
                    self.intake_temp_dropdown.nth(i).click()
                    break
        except Exception as e:
            print(f" Exception while selecting intake template : {e}")
            raise

    def select_pick_date_start(self):
        try:
            self.pick_date_start_txt.nth(0).click()
            self.next_month_txt.click()
            self.date_15.click()
        except Exception as e:
            print(f" Exception while selecting date for start assessment : {e}")
            raise

    def select_pick_date_end(self):
        try:
            self.pick_date_end_txt.click()
            time.sleep(3)
            self.next_month_txt.click()
            time.sleep(2)
            self.date_10.click()
            time.sleep(1)
        except Exception as e:
            print(f" Exception while selecting date for end assessment : {e}")
            raise


    def select_assignee(self, assignee_name:str):
        try:
            self.assignee_txt.click()
            count = self.assignee_dropdown.count()
            for i in range(count):
                text = self.assignee_dropdown.nth(i).inner_text()
                if assignee_name in text:
                    self.assignee_dropdown.nth(i).click()
                    break
        except Exception as e:
            print(f" Exception while selecting assignee name : {e}")
            raise

    def select_reviewer(self, reviewer_name:str):
        try:
            self.reviewer_txt.click()
            count = self.reviewer_dropdown.count()
            for i in range(count):
                text = self.reviewer_dropdown.nth(i).inner_text()
                if reviewer_name in text:
                    self.reviewer_dropdown.nth(i).click()
                    break
        except Exception as e:
            print(f" Exception while selecting reviewer name : {e}")
            raise

    def get_vendor_assessment_confi_msg(self):
        try:
            return self.vendor_assessment_confi_msg
        except Exception as e:
            print(f" Exception while getting vendor assessment confirmation message : {e}")
            return None

    # select the vendor assessment under the 'vendor assessment name'
    def select_vendor_assessment(self):
        try:
            self.vendor.first.wait_for(state="visible", timeout=15000)
            self.vendor_assess_txt.nth(0).click()
        except Exception as e:
            print(f" Exception while selection vendor assessment : {e}")
            raise

    def click_save_and_next_btn(self):
        try:
            self.save_and_next_btn.click()
        except Exception as e:
            print(f" Exception while click on save and next button : {e}")
            raise


    def select_collaborator(self,collaborator_name: str):
        try:
            self.add_collaborator_btn.click()
            self.add_collaborator_txt.click()
            count = self.collaborator_dropdown.count()
            for i in range(count):
                text = self.collaborator_dropdown.nth(i).inner_text()
                if collaborator_name in text:
                    self.collaborator_dropdown.nth(i).click()
                    self.close_btn.click()
                    self.collaborator_submit_btn.click()
                    break
        except Exception as e:
            print(f"Exception while selecting collaborator: {e}")

    def get_collaborator_add_confi_msg(self):
        try:
            return self.collaborator_add_confi_msg
        except Exception as e:
            print(f" Exception while getting collaborator add confirmation message: {e}")
            return None


    def questions_and_answers(self):
        try:
            # 1 question
            self.questions.nth(0).click()
            self.answers.nth(1).click()  # no

            # 2 question
            self.questions.nth(1).click()
            self.answers.nth(0).click()  # yes

            # 3 question
            self.questions.nth(2).click()
            self.answers.nth(0).click()  # yes

            # 4 question
            self.questions.nth(3).click()
            self.answers.nth(1).click()  # no

            # 5 question
            self.questions.nth(4).click()
            self.answers.nth(0).click()  # yes

            # 6 question
            self.questions.nth(5).click()
            self.answers.nth(1).click()  # no

            # 7 question
            self.questions.nth(6).click()
            self.answers.nth(0).click()  # yes

            # 8 question
            self.questions.nth(7).click()
            self.answers.nth(1).click()  # no

            # save button
            self.save_btn.click()

        except Exception as e:
            print(f" Exception while clicking TPRA button : {e}")
            raise

    def get_save_msg(self):
        try:
            return self.save_msg
        except Exception as e:
            print(f" Exception while save confirmation message: {e}")
            return None

    def click_save_btn(self):
        try:
            self.save_btn.click()
        except Exception as e:
            print(f" Exception while click on save button : {e}")
            raise

    def click_submit_for_review_btn(self):
        try:
            self.submit_for_review_btn.click()
        except Exception as e:
            print(f" Exception while click on submit for review button : {e}")
            raise
