import re
import time
from os import name
from pages.dpia_page import DpiaPage

from playwright.sync_api import Page,expect

class AssessmentManagementPage:
    def __init__(self,page: Page):
        self.page = page
        self.dpia = DpiaPage(page)
        self.assessment_management_btn = page.locator("a span:has-text('Assessment Management')")
        self.assessment_management_title = page.locator("h2:has-text('Assessment Management')")
        # assessment input field locators
        self.template_category_txt = page.get_by_label("Template Category")
        self.template_txt = page.get_by_label("Template").nth(1)
        self.select_template = page.locator("div[role='option']:last-child")
        self.priority_txt = page.get_by_label("Priority ")
        self.assignee_txt = page.locator("span:has-text('Select assignee')")
        self.dropdown_list = page.get_by_role("option")
        self.reviewer_txt = page.locator("span:has-text('Select reviewer')")



    def click_assessment_management_btn(self):
        try:
            self.assessment_management_btn.click()
            self.assessment_management_btn.click()
        except Exception as e:
            print(f" Exception while click on assessment management button : {e}")
            raise

    def get_assessment_management_title(self):
        try:
            return self.assessment_management_title
        except Exception as e:
            print(f" Exception while fetching assessment management title: {e}")
            return None


    def fill_assessment_details(self, assessment_name: str, assessment_description: str, legal_entity_name:str, assignee_name:str, reviewer_name:str):
        try:
            self.dpia.new_assessment_btn.click()
            self.dpia.assessment_name_txt.fill(assessment_name)
            self.dpia.assessment_desc_txt.fill(assessment_description)
            self.template_category_txt.click()
            self.dpia.dropdown.nth(1).click()
            self.template_txt.click()
            self.select_template.click()
            self.dpia.pick_date_start_txt.click()
            self.dpia.next_month_txt.click()
            self.dpia.date_15.click()
            self.priority_txt.click()
            self.dpia.dropdown.nth(2).click()
            self.dpia.select_legal_entity(legal_entity_name)
            self.dpia.select_departments()
            self.select_assignee(assignee_name)
            self.select_reviewer(reviewer_name)
            self.dpia.create_assessment_btn.click()

        except Exception as e:
            print(f" Exception while fill assessment management details : {e}")
            raise

    def select_assignee(self, assignee_name:str):
        try:
            self.assignee_txt.click()
            self.page.wait_for_selector("[role='option']")
            self.dropdown_list.filter(has_text=assignee_name).click()
        except Exception as e:
            print(f" Exception while selecting assignee name : {e}")
            raise

    def select_reviewer(self, reviewer_name:str):
        try:
            self.reviewer_txt.click()
            self.page.wait_for_selector("[role='option']")
            self.dropdown_list.filter(has_text=reviewer_name).click()
        except Exception as e:
            print(f" Exception while selecting reviewer name : {e}")
            raise


















