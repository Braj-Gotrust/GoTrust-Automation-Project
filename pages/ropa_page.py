import re
import time

from playwright.sync_api import Page,expect

class RopaPage:
    def __init__(self,page: Page):
        self.page = page
        self.ropa_registry_btn =page.locator("a span:has-text('Ropa Registry')")
        self.ropa_registry_title = page.locator("h1:has-text('ROPA Registry')")
        self.processing_activity_btn = page.locator("button:has-text('Processing Activity')")
        self.ropa_form_title = page.locator("form h3:has-text('Processing Activity Information')")
        self.processing_activity_name = page.get_by_placeholder("e.g., Customer Registration")
        self.processing_activity_description = page.get_by_placeholder("Short explanation...")
        self.legal_entity_txt = page.locator("span:has-text('Select legal entity')").nth(0)
        self.legal_entity_dropdown = page.locator("div[role='presentation'] span span")
        self.department_txt = page.locator("span:has-text('Select department')")
        self.select_department = page.locator("div[role='option'] span span").nth(0)
        self.due_date = page.locator("div.mt-2 button[aria-haspopup='dialog']")
        self.current_month_year = page.locator("div[aria-live='polite']")
        self.next_month = page.locator("button[name='next-month']")
        self.previous_month = page.locator("button[name='previous-month']")
        self.dates = page.locator(".rdp-tbody td")
        self.assignee_txt = page.locator("span:has-text('Select assignee')")
        self.assignee_list = page.locator("div[role='option'] span span")
        # FIRST REVIEWER
        self.first_yes_btn = page.locator("label:has-text('Yes')")
        self.level_2_reviewer_title = page.locator("label:has-text('Do you want to add more level of reviewer?')").nth(0)
        self.level_1_reviewer_txt = page.locator("span:has-text('Select reviewers for Level 1...')")
        self.level_1_reviewer_list = page.locator("div[role='group'] span")
        self.level_1_reviewer_list_close = page.locator("div[role='option']:has-text('Close')")
        # SECONDE REVIEWER
        self.second_yes_btn = page.locator("label:has-text('Yes')").nth(1)
        self.level_3_reviewer_title = page.locator("label:has-text('Do you want to add more level of reviewer?')").nth(1)
        self.level_2_reviewer_txt = page.locator("span:has-text('Select reviewers for Level 2...')")
        self.level_2_reviewer_list = page.locator("div[role='group'] span")
        self.level_2_reviewer_list_close = page.locator("div[role='option']:has-text('Close')")
        self.create_ropa_btn = page.locator("button:has-text('Create ROPA')")
        self.ropa_title = page.locator("h3:has-text('Create Processing Activity')")
        # add collaborator
        self.add_collab_txt = page.locator("button:has-text('Collaborator')")
        self.collaborator_popup = page.locator("h3:has-text('Add Collaborator')")

        self.collab_dropdown_txt = page.locator("span:has-text('Select collaborators')")
        self.collaborator_list = page.locator("div[role='group'] span")
        self.close = page.locator("div[role='option']:has-text('Close')")
        self.collab_submit_btn = page.locator("//button[normalize-space()='Submit']")
        #self.collab_add_confi_msg = page.get_by_text("Collaborators added")
        self.collab_add_confi_msg = page.get_by_text("Collaborators updated successfully")

        self.organization_role_txt = page.locator("span[style='pointer-events: none;'] span:has-text('Select organizational role')")
        self.select_role = page.locator("span:has-text('Fiduciary')").nth(0)
        self.update_btn = page.locator("button:has-text('Update')")
        #self.update = page.get_by_text("Grounds for Processing Personal Data updated successfully.")
        self.update_msg = page.get_by_text("ROPA updated successfully")

        # data principal tagging
        self.data_principal_tagging_txt = page.locator("span:has-text('Data Principal Tagging')")
        self.data_principal_category_txt = page.locator("span[style='pointer-events: none;'] span:has-text('Select Data Principal Category')")
        self.dropdown = page.locator("div[role='option'] span:nth-child(2)")
        self.data_principal_txt = page.locator("span:has-text('Select Data Principal')")
        self.data_principal_list = page.locator("div[role='group'] span")
        self.countries_txt = page.locator("span:has-text('Select Country')")
        self.select_country = page.locator("span:has-text('India')").nth(1)
        self.update_data_principal_tagging_msg = page.get_by_text("Data Principal updated successfull")

        # pii tagging section
        self.pii_tagging_txt = page.locator("span:has-text('PII Tagging')")
        self.pii_type_txt = page.locator("span span:has-text('Select PII type')")
        self.select_pii_type = page.locator("span span:has-text('EMAIL ADDRESS')")
        self.department_collecting_data_txt = page.locator("button[role='combobox'] span span:has-text('Select Department')")
        self.depart_dropdown = page.locator("div[role='option'] span:nth-child(2)")
        self.department_process_txt = page.locator("span span:has-text('Select Department')")
        self.depart_process_dropdown = page.locator("div[role='option'] span")
        self.source_of_personal_data_txt = page.get_by_placeholder("e.g., User provided, Third-party, Public records")
        self.personal_data_collection_txt = page.get_by_placeholder("e.g., Web form, API, CSV upload")
        self.purpose_of_processing_txt = page.get_by_placeholder("Describe why this personal data is being processed...")
        self.update_pii_tagging_msg = update_msg = page.get_by_text("Personal Data Updated Successfully")

        # After login with collaborator account
        # ROPA NAME COUNT
        self.all_ropa_name = page.locator(".cursor-pointer.break-words.text-sm")
        self.three_dot = page.locator("button:has(svg.lucide-ellipsis)")
        self.edit_ropa_btn = page.get_by_role("menuitem", name="Edit")
        self.edit_ropa_page_title = page.locator("h3:has-text('Create Processing Activity')")

        # Legal basis section
        self.legal_basis_txt = page.locator("span:has-text('Grounds for Processing Personal Data')")
        #self.legal_basis_for_india_txt = page.locator("span:has-text('Legal Basis for India')")
        self.checkbox_label = page.locator("label:has-text('Personal data voluntarily provided')")
        self.first_yes_button = page.locator(".inline-flex.items-center.gap-2 span:has-text('Yes')").nth(0)
        self.critical_modal = page.locator("h2:has-text('Set sensitivity to CRITICAL?')")
        self.make_critical_btn = page.locator("button:has-text('Make Critical')")
        self.critical_msg = page.get_by_text("Sensitivity set to CRITICAL")
        self.second_yes_button = page.locator(".inline-flex.items-center.gap-2 span:has-text('Yes')").nth(1)
        self.third_yes_button = page.locator(".inline-flex.items-center.gap-2 span:has-text('Yes')").nth(2)
        self.legal_basis_update_msg = page.get_by_text("Grounds for Processing Personal Data updated successfully.")
        # click on submit button
        self.collab_submit_for_review_btn = page.locator("button:has-text('Submit')")
        self.collab_submit_for_review_msg = page.get_by_text("Submitted as collaborator")
        # assignee submit for review button
        self.assignee_submit_for_review_btn = page.locator("button:has-text('Submit for Review')")
        self.assignee_submit_for_review_msg = page.get_by_text("Processing activity submitted for review.")
        # reviewer acknowledge
        self.reviewer_acknowledge_btn = page.locator("button:has-text('Acknowledge')")
        self.reviewer_add_comment = page.get_by_placeholder("Comment (required)")
        self.reviewer_submit_comment = page.locator("button:has-text('Submit')")
        self.reviewer_acknowledge_msg = page.get_by_text("Reviewer action submitted")





    def click_ropa_registry_btn(self):
        try:
            time.sleep(1)
            self.ropa_registry_btn.click()
            self.ropa_registry_btn.click()
        except Exception as e:
            print(f" Exception while clicking processing activity button : {e}")
            raise

    def get_ropa_registry_title(self):
        try:
            return self.ropa_registry_title
        except Exception as e:
            print(f" Exception while fetching ropa registry title: {e}")
            return None


    def click_processing_activity_btn(self):
        try:
            self.processing_activity_btn.click()
        except Exception as e:
            print(f" Exception while clicking processing activity button : {e}")
            raise

    def get_ropa_form_title(self):
        try:
            return self.ropa_form_title
        except Exception as e:
            print(f" Exception while fetching ropa form title: {e}")
            return None


    def processing_activity_form(self,name:str,description:str, legal_entity_name:str):
        try:
            time.sleep(1)
            self.processing_activity_name.fill(name)
            time.sleep(1)
            self.processing_activity_description.fill(description)
            time.sleep(2)
            self.legal_entity_txt.click()
            time.sleep(1)
            self.select_legal_entity(legal_entity_name)
            self.department_txt.click()
            self.select_department.click()
        except Exception as e:
            print(f" Exception while filling processing activity form: {e}")
            return None



    # def select_legal_entity(self,legal_entity_name:str):
    #     try:
    #         count = self.legal_entity_dropdown.count()
    #         found = False
    #         for i in range(count):
    #             dropdown_text = self.legal_entity_dropdown.nth(i).inner_text()
    #             if dropdown_text == legal_entity_name:
    #                 self.legal_entity_dropdown.nth(i).click()
    #                 found = False
    #                 break
    #         if not found:
    #             self.legal_entity_dropdown.first.click()
    #     except Exception as e:
    #         print(f" Exception while selection legal entity: {e}")
    #         return None
    def select_legal_entity(self, legal_entity_name: str):
        try:
            options = self.page.locator("div[role='option']")
            options.first.wait_for()
            target = self.page.locator(f"div[role='option']:has-text('{legal_entity_name}')")

            if target.count() > 0:
                target.first.click()
            else:
                options.first.click()

        except Exception as e:
            print(f"Exception while selecting legal entity: {e}")



    def select_due_date(self,target_month_year:str, target_date:str, is_future:bool):
        try:
            self.due_date.click()
            all_dates = self.dates.all()
            while True:
                current_month_year = self.current_month_year.inner_text()
                if current_month_year == target_month_year:
                    break
                if is_future:
                    self.next_month.click()
                else:
                    self.previous_month.click()
            for date in all_dates:
                date_text = date.inner_text()
                if date_text == target_date:
                    date.click()
                    break
        except Exception as e:
            print(f" Exception while selecting due date : {e}")
            return None

    def select_assignee(self,assignee_name:str):
        try:
            self.assignee_txt.click()
            count = self.assignee_list.count()
            for i in range(count):
                text = self.assignee_list.nth(i).inner_text()
                if assignee_name in text:
                    self.assignee_list.nth(i).click()
                    break
        except Exception as e:
            print(f" Exception while selecting assignee : {e}")
            raise



    def select_level_1_reviewer(self,reviewer_1_name:str):
        try:
            self.level_1_reviewer_txt.click()
            count = self.level_1_reviewer_list.count()
            for i in range(count):
                text = self.level_1_reviewer_list.nth(i).inner_text()
                if reviewer_1_name in text:
                    self.level_1_reviewer_list.nth(i).click()
                    self.level_1_reviewer_list_close.click()
                    break
        except Exception as e:
            print(f" Exception while clicking processing activity button : {e}")
            raise

    def get_level_2_reviewer_title(self):
        try:
            self.first_yes_btn.click()
            return self.level_2_reviewer_title
        except Exception as e:
            print(f" Exception while clicking processing activity button : {e}")
            return None



    def select_level_2_reviewer(self,reviewer_2_name:str):
        try:
            self.level_2_reviewer_txt.click()
            count = self.level_2_reviewer_list.count()
            for i in range(count):
                text = self.level_2_reviewer_list.nth(i).inner_text()
                if reviewer_2_name in text:
                    self.level_2_reviewer_list.nth(i).click()
                    self.level_2_reviewer_list_close.click()
                    break
        except Exception as e:
            print(f" Exception while clicking processing activity button : {e}")
            raise

    def get_level_3_reviewer_title(self):
        try:
            self.second_yes_btn.click()
            return self.level_3_reviewer_title
        except Exception as e:
            print(f" Exception while clicking processing activity button : {e}")
            return None


    def click_and_get_title_ropa(self):
        try:
            self.create_ropa_btn.click()
            return self.ropa_title
        except Exception as e:
            print(f" Exception while clicking create ropa button : {e}")
            return None

    def click_and_get_collab_popup(self):
        try:
            self.add_collab_txt.click()
            return self.collaborator_popup
        except Exception as e:
            print(f" Exception while fetching collaborator title: {e}")
            return None


    def select_collaborator(self,collaborator_name: str):
        try:
            time.sleep(3)
            self.collab_dropdown_txt.click()
            count = self.collaborator_list.count()
            for i in range(count):
                text = self.collaborator_list.nth(i).inner_text()
                if collaborator_name in text:
                    self.collaborator_list.nth(i).click()
                    self.close.click()
                    break
        except Exception as e:
            print(f"Exception while selecting collaborator: {e}")


    def click_and_get_collab_confi_msg(self):
        try:
            self.collab_submit_btn.click()
            return self.collab_add_confi_msg
        except Exception as e:
            print(f" Exception while fetching collaborator confirmation message : {e}")
            return None


    def click_and_select_role(self):
        try:
            self.organization_role_txt.click()
            self.select_role.click()
        except Exception as e:
            print(f" Exception while selecting organization role : {e}")
            raise

    def click_update_btn_and_get_msg(self):
        try:
            self.update_btn.click()
            return self.update_msg
        except Exception as e:
            print(f" Exception while fetching ropa update message : {e}")
            return None


    def data_principal_tagging_section(self):
        try:
            self.data_principal_tagging_txt.click()
            time.sleep(1)
            self.data_principal_category_txt.click()
            time.sleep(1)
            self.dropdown.first.click()
            self.data_principal_txt.click()
            self.data_principal_list.nth(0).click()
            self.close.click()
            self.countries_txt.click()
            self.select_country.click()
            self.close.click()

        except Exception as e:
            print(f" Exception while selecting data principal tagging section : {e}")
            raise

    def click_update_data_principal_tagging_btn_and_get_msg(self):
        try:
            self.update_btn.click()
            return self.update_data_principal_tagging_msg
        except Exception as e:
            print(f" Exception while fetching data principal tagging message : {e}")
            return None


    def pii_tagging_section(self):
        try:
            self.pii_tagging_txt.click()
            self.pii_type_txt.click()
            self.select_pii_type.click()
            self.department_collecting_data_txt.click()
            time.sleep(1)
            self.depart_dropdown.nth(1).click()
            self.department_process_txt.click()
            self.depart_process_dropdown.nth(1).click()
            self.close.click()
            self.source_of_personal_data_txt.fill("Third-party")
            self.personal_data_collection_txt.fill("Web form")
            self.purpose_of_processing_txt.fill("test description")

        except Exception as e:
            print(f" Exception while filling pii tagging section : {e}")
            raise

    def click_update_pii_tagging_btn_and_get_msg(self):
        try:
            self.update_btn.click()
            return self.update_pii_tagging_msg
        except Exception as e:
            print(f" Exception while fetching pii tagging message : {e}")
            return None


    def select_and_edit_processing_activity(self, processing_activity_name:str):
        try:
            time.sleep(3)
            count = self.all_ropa_name.count()
            for i in range(count):
                text = self.all_ropa_name.nth(i).inner_text().strip()
                if text == processing_activity_name:
                    self.three_dot.nth(i).click()
                    # click on ropa edit button
                    self.edit_ropa_btn.click()
                    break
        except Exception as e:
            print(f" Exception while selecting ropa : {e}")
            raise

    def get_edit_ropa_page_title(self):
        try:
            return self.edit_ropa_page_title
        except Exception as e:
            print(f" Exception while fetching edit ropa page title: {e}")
            return None



    def legal_basis_section(self):
        try:
            self.legal_basis_txt.nth(0).click()
            self.legal_basis_txt.nth(1).click()
            self.page.locator("button[role='checkbox']").nth(0).click()
            #self.legal_basis_for_india_txt.click()
            checkbox = self.checkbox_label.locator("button[role='checkbox']")
            state = checkbox.get_attribute("aria-checked")
            if state == "false":
                self.checkbox_label.click()
            self.first_yes_button.click()
            if self.critical_modal.is_visible(timeout=5000):
                expect(self.critical_modal).to_be_visible(timeout=15000)
                # click make critical button
                self.make_critical_btn.click()
                expect(self.critical_msg).to_be_visible(timeout=10000)
            self.second_yes_button.click()
            self.third_yes_button.click()
        except Exception as e:
            print(f" Exception while clicking processing activity button : {e}")
            raise

    def click_update_legal_basis_btn_and_get_msg(self):
        try:
            self.update_btn.click()
            return self.legal_basis_update_msg
        except Exception as e:
            print(f" Exception while fetching legal basis message : {e}")
            return None

    def click_collab_submit_for_review_btn_and_get_msg(self):
        try:
            self.collab_submit_for_review_btn.click()
            return self.collab_submit_for_review_msg
        except Exception as e:
            print(f" Exception while submit for review button and fetching error message : {e}")
            return None


    def click_assignee_submit_for_review_btn_and_get_msg(self):
        try:
            self.assignee_submit_for_review_btn.click()
            return self.assignee_submit_for_review_msg
        except Exception as e:
            print(f" Exception while submit for review and fetching submit message : {e}")
            return None



    def click_reviewer_acknowledge_btn_and_get_msg(self):
        try:
            self.reviewer_acknowledge_btn.click()
            self.reviewer_add_comment.fill("Done")
            self.reviewer_submit_comment.click()
            return self.reviewer_acknowledge_msg
        except Exception as e:
            print(f" Exception while submit for review and fetching submit message : {e}")
            return None



