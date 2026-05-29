import re
import time
from os import name

from playwright.sync_api import Page,expect

class DpiaPage:
    def __init__(self,page: Page):
        self.page = page
        self.dpia_btn =page.locator("a span:has-text('DPIA')")
        self.dpia_title = page.locator("h1:has-text('Data Protection Impact Assessment')")
        self.new_assessment_btn = page.locator("button:has-text('New Assessment')")
        # assessment input field locators
        self.assessment_name_txt = page.get_by_label("Assessment Name")
        self.assessment_desc_txt = page.get_by_label("Description")
        self.pick_date_start_txt = page.locator("button:has-text('Pick a date')")
        self.next_month_txt = page.locator("button[name='next-month']")
        self.date_15 = page.get_by_role("gridcell", name="15")
        self.legal_entity_txt = page.locator("span:has-text('Select legal entity')").nth(0)
        self.legal_entity_dropdown = page.locator("div[role='option'] span:last-child")
        self.departments_txt = page.locator("span:has-text('Select departments')")
        self.departments_dropdown = page.locator("div[role='option'] span").nth(0)
        self.close_btn = page.locator("div[role='option']:has-text('Close')")
        self.assignee_txt = page.locator("span:has-text('Select assignee')")
        self.dropdown_list = page.get_by_role("option")
        self.reviewer_txt = page.locator("span:has-text('Select reviewer')")
        self.save_btn = page.locator("button:has-text('Save')")
        self.create_assessment_btn = page.locator("button:has-text('Create Assessment')")
        self.create_assessment_msg = page.get_by_text("Assessment card created successfully")
        # add collaborator
        self.add_collaborator_btn = page.locator("button:has-text('Add Collaborator')")
        self.collaborator_input_txt = page.get_by_placeholder("Type name or email to search users...")
        self.collaborator_dropdown = page.locator("div.text-sm.font-medium")
        self.collaborator_plus_btn = page.locator("button:has(svg.lucide-plus)")
        self.collaborator_add_confi_msg = page.get_by_text("Collaborator added successfully")
        self.close = page.locator("button:has-text('Close')")
        # assessment questions and answers
        self.yes_buttons = page.locator("button[role='radio'][value='0']")
        self.no_buttons = page.locator("button[role='radio'][value='1']")
        self.not_buttons = page.locator("button[role='radio'][value='2']")
        # questions
        self.likelihood = page.locator("label:has-text('Likelihood') + button")
        self.dropdown = page.locator("div[role='option']")
        self.impact = page.locator("label:has-text('Impact') + button")
        self.submit_for_review_btn = page.locator("button:has-text('Submit')")
        self.submit_for_review_msg = page.get_by_text("assessment submitted successfully!")
        self.next_btn = page.locator("button:has-text('Next')")
        # reviewer
        self.submit_btn = page.locator("button:has-text('Submit')")
        self.submit_confirmation_msg = page.get_by_text("review submitted successfully!")
        self.yes_review_btn = page.locator("button[role='radio'][value='true']")
        self.no_review_btn = page.locator("button[role='radio'][value='false']")
        #self.save_review_btn = page.locator("button:has-text('Save Review')")
        self.data_protection_governance_category_txt = page.locator("span:has-text('Data Protection Governance')")









    def click_dpia_btn(self):
        try:
            time.sleep(1)
            self.dpia_btn.click()
            self.dpia_btn.click()
        except Exception as e:
            print(f" Exception while click on DPIA button : {e}")
            raise

    def get_dpia_title(self):
        try:
            return self.dpia_title
        except Exception as e:
            print(f" Exception while fetching dpia title: {e}")
            return None


    def fill_dpia_details(self, assessment_name: str, assessment_description: str, legal_entity_name:str, assignee_name:str, reviewer_name:str):
        try:
            self.new_assessment_btn.click()
            self.assessment_name_txt.fill(assessment_name)
            self.assessment_desc_txt.fill(assessment_description)
            self.select_pick_date_start()
            self.select_legal_entity(legal_entity_name)
            self.select_departments()
            time.sleep(1)
            self.select_assignee(assignee_name)
            self.select_reviewer(reviewer_name)
            self.save_btn.click()
            self.create_assessment_btn.click()

        except Exception as e:
            print(f" Exception while filling dpia details : {e}")
            raise

    def select_pick_date_start(self):
        try:
            self.pick_date_start_txt.nth(0).click()
            self.next_month_txt.click()
            self.date_15.click()
        except Exception as e:
            print(f" Exception while selecting date for start assessment : {e}")
            raise


    def select_legal_entity(self, legal_entity_name: str):
        try:
            self.legal_entity_txt.click()
            self.page.wait_for_selector("[role='option']")
            option = self.legal_entity_dropdown.filter(has_text=legal_entity_name)

            if option.is_visible():
                option.click()
            else:
                print(f" {legal_entity_name} not found, selecting first option")
                self.legal_entity_dropdown.first.click()

        except Exception as e:
            print(f"Exception while selecting legal entity name: {e}")
            raise

    def select_departments(self):
        try:
            self.departments_txt.click()
            self.departments_dropdown.nth(0).click()
            self.close_btn.click()
        except Exception as e:
            print(f" Exception while selecting departments : {e}")
            raise


    def select_assignee(self, assignee_name:str):
        try:
            time.sleep(1)
            self.assignee_txt.click()
            self.page.wait_for_selector("[role='option']")
            self.dropdown_list.filter(has_text=assignee_name).click()
        except Exception as e:
            print(f" Exception while selecting assignee name : {e}")
            raise

    def select_reviewer(self, reviewer_name:str):
        try:
            time.sleep(1)
            self.reviewer_txt.click()
            self.page.wait_for_selector("[role='option']")
            self.dropdown_list.filter(has_text=reviewer_name).click()
        except Exception as e:
            print(f" Exception while selecting reviewer name : {e}")
            raise

    def get_create_assessment_msg(self):
        try:
            return self.create_assessment_msg
        except Exception as e:
            print(f" Exception while getting create assessment successful message : {e}")
            return None

    def select_assessment_start_and_continue(self, assessment_name:str):
        try:
            card = self.page.locator(
                "div.rounded-lg",
                has=self.page.locator(f"h3 span:has-text('{assessment_name}')")
            )
            card.locator("button:has-text('Start'), button:has-text('Continue')").first.click()
            time.sleep(2)

        except Exception as e:
            print(f" Exception while selecting dpia assessment : {e}")
            raise

    def select_assessment_and_review(self, assessment_name:str):
        try:
            card = self.page.locator(
                "div.rounded-lg",
                has=self.page.locator(f"h3 span:has-text('{assessment_name}')")
            )
            card.locator("button:has-text('Review')").first.click()
            time.sleep(2)

        except Exception as e:
            print(f" Exception while selecting dpia assessment : {e}")
            raise

    def select_assessment_and_edit(self, assessment_name:str):
        try:
            card = self.page.locator(
                "div.rounded-lg",
                has=self.page.locator(f"h3 span:has-text('{assessment_name}')")
            )
            card.locator("button:has-text('Edit')").first.click()
            time.sleep(2)

        except Exception as e:
            print(f" Exception while selecting dpia assessment : {e}")
            raise


    def select_collaborator(self,collaborator_email: str):
        try:
            self.add_collaborator_btn.click()
            self.collaborator_input_txt.first.fill(collaborator_email)
            self.page.wait_for_selector("div.text-sm.font-medium")
            # self.collaborator_dropdown.filter(has_text=collaborator_email).click()
            self.collaborator_dropdown.first.click()
            self.collaborator_plus_btn.first.click()

        except Exception as e:
            print(f"Exception while selecting collaborator: {e}")

    def get_collaborator_add_confi_msg(self):
        try:
            return self.collaborator_add_confi_msg
        except Exception as e:
            print(f" Exception while getting add collaborator successful message : {e}")
            return None

    def collaborator_assessment_answers(self):
        try:
            yes_count = self.yes_buttons.count()
            for i in range(yes_count):
                self.yes_buttons.nth(i).click()
                self.likelihood.nth(i).click()
                self.dropdown.nth(2).click()
                self.impact.nth(i).click()
                self.dropdown.nth(2).click()
        except Exception as e:
            print(f" Exception while giving the control question answers : {e}")
            raise

    def get_submit_for_review_btn(self):
        try:
            return self.submit_for_review_btn
        except Exception as e:
            print(f" Exception while click on submit for review button: {e}")
            return None


    def give_assessment_and_submit_for_review(self, max_attempts=3):
        attempt = 1
        while attempt <= max_attempts:
            self.complete_assessment()  # this is function
            self.submit_for_review_btn.wait_for(state="visible", timeout=15000)
            self.submit_for_review_btn.click()
            try:
                expect(self.submit_for_review_msg).to_be_visible(timeout=5000)
                print("Submit for review submitted successfully")
                break
            except:
                print("Submit for review failed — retrying...")
                attempt += 1
                self.data_protection_governance_category_txt.click()

    def complete_assessment(self):
        while True:
            count = self.yes_buttons.count()
            for i in range(count):
                self.yes_buttons.nth(i).click()
                self.likelihood.nth(i).click()
                self.dropdown.nth(2).click()
                self.impact.nth(i).click()
                self.dropdown.nth(2).click()

            if self.submit_for_review_btn.is_visible():
                break

            if self.next_btn.is_visible():
                self.next_btn.click()
                time.sleep(2)
            else:
                break



    def assessment_review_and_change_request(self, max_attempts=3):
        attempt = 1
        while attempt <= max_attempts:
            self.change_request_review()
            time.sleep(1)
            self.submit_btn.wait_for(state="visible", timeout=15000)
            self.submit_btn.click()
            time.sleep(3)
            try:
                expect(self.submit_confirmation_msg).to_be_visible(timeout=5000)
                print("Review submitted successfully")
                break
            except:
                print("Submit failed — retrying...")
                attempt += 1
                self.data_protection_governance_category_txt.click()

    def change_request_review(self):
        while True:

            count = self.yes_review_btn.count()
            #print("\n total yes button",count)

            for i in range(count):
                self.yes_review_btn.nth(i).click()
                #self.save_review_btn.nth(i).click()
                #time.sleep(1)

            if self.submit_btn.is_visible():
                # No buttons
                no_btn_count = self.no_review_btn.count()
                for i in range(no_btn_count):
                    self.no_review_btn.nth(i).click()
                    #self.save_review_btn.nth(i).click()
                    #time.sleep(1)
                break

            if self.next_btn.is_visible():
                self.next_btn.click()
                time.sleep(1)
            else:
                break



    def assessment_review_and_submit(self, max_attempts=3):
        attempt = 1
        while attempt <= max_attempts:
            self.complete_review()
            self.submit_btn.wait_for(state="visible", timeout=15000)
            self.submit_btn.click()
            try:
                expect(self.submit_confirmation_msg).to_be_visible(timeout=5000)
                print("Review submitted successfully")
                break
            except:
                print("Submit failed — retrying...")
                attempt += 1

    def complete_review(self):
        while True:
            count = self.yes_review_btn.count()

            for i in range(count):
                self.yes_review_btn.nth(i).click()
                #self.save_review_btn.nth(i).click()
                #time.sleep(1)

            if self.submit_btn.is_visible():
                break

            if self.next_btn.is_visible():
                self.next_btn.click()
                time.sleep(1)
            else:
                break

