import re
import time

from playwright.sync_api import Page

class OrgStructurePage:
    def __init__(self,page: Page):
        self.page = page
        self.txt_org_setting = self.page.locator(".text-3xl")
        self.txt_profile_configuration = self.page.locator("button>span:has-text('Profile Configuration')")
        self.txt_org_structure = self.page.locator("a>span:has-text('Organization Structure')")
        self.btn_structure_tab = self.page.get_by_role("tab", name="Structure")
        self.txt_structure_tab = self.page.locator("span:has-text('Organization Hierarchy')")
        self.btn_plus_symbol = self.page.locator("div.border-blue-200 button:has(svg.lucide-plus)").nth(0)
        self.dropdown_select_type = self.page.locator("div span:has-text('Select type')")
        self.select_legal_entity = self.page.get_by_role("option", name="Legal Entity")

        # form locators
        self.txt_name = self.page.get_by_placeholder("Enter Legal Entity name")
        self.txt_description = self.page.get_by_placeholder("Description")
        self.txt_company_address = self.page.get_by_placeholder("Full company address")

        # Countries dropdown
        self.txt_country = self.page.locator("button span:has-text('Select a country')")
        self.select_country_name = self.page.locator("span:has-text('India (IN)')")

        # Industries dropdown
        self.txt_industries = self.page.locator("span:has-text('Select options')")
        self.select_industry_name = self.page.locator("span:has-text('(Select All)')")
        self.close_industry_name = self.page.locator("div[data-value='Close']")

        # Region dropdown
        self.txt_region = self.page.locator("span:has-text('Select region')")
        self.select_region_name = self.page.locator("span:has-text('APAC')")

        # Regulations dropdown
        self.txt_regulation = self.page.locator("span:has-text('Select regulations')")
        self.select_regulation_name = self.page.locator("span:has-text('(Select All)')")
        self.close_regulation_name = self.page.locator("div[data-value='Close']")

        # Select DPO dropdown
        self.txt_dpo = self.page.locator("//span[normalize-space()='Select']")
        self.select_dop_name = self.page.locator("div[role='option']").nth(0)

        # Risk matrix and data principal category tab
        self.txt_risk_matrix = self.page.get_by_role("tab",name="Risk Matrix")
        self.txt_matrix_name = self.page.get_by_placeholder("e.g., GDPR Compliance Matrix")
        self.txt_data_principal_category = self.page.get_by_role("tab",name="Data Principal Category")
        self.parent_checkboxes = self.page.locator(".z-20")
        self.checkboxes_text = self.page.locator(".text-sm.font-medium.text-gray-900")
        self.child_checkboxes = self.page.locator("div.group button[role='checkbox']")


        # Create legal entity button
        self.btn_create_legal_entity = self.page.locator("button:has-text('Create Legal Entity')")
        self.btn_continue = self.page.locator("button:has-text('Continue')")
        self.success_msg =self.page.locator("text=Legal entity created")

        # Business unit locators
        self.legal_entities = self.page.locator("div.border-blue-200 h3")
        self.plus_btn = self.page.locator("div.border-blue-200 button:has(svg.lucide-plus)")
        self.plus_btn_title = self.page.locator(".text-center h2")
        self.select_business_unit = self.page.locator("div span:has-text('Business Unit')")
        self.business_unit_name = self.page.get_by_placeholder("Enter Business Unit name")
        self.business_unit_description = self.page.get_by_placeholder("description")
        self.create_business_unit_button = self.page.locator("button:has-text('Create Business Unit')")
        self.confirmation_msg = self.page.get_by_text("Business unit created successfully")

        # Department locators
        self.select_department = self.page.locator("div span:has-text('Department')")
        self.department_name = self.page.get_by_placeholder("Enter Department name")
        self.department_description = self.page.get_by_placeholder("description")
        self.create_department_button = self.page.locator("button:has-text('Create Department')")
        self.department_confirmation_msg = self.page.get_by_text("Department created successfully!")

        # product locators
        self.select_product = self.page.locator("div span:has-text('Product')")
        self.product_name = self.page.get_by_placeholder("Enter Product name")
        self.product_description = self.page.get_by_placeholder("description")
        self.create_product_button = self.page.locator("button:has-text('Create Product')")
        self.product_confirmation_msg = self.page.get_by_text("Product created successfully!")

        # service locators
        self.select_service = self.page.locator("div span:has-text('Service')")
        self.service_name = self.page.get_by_placeholder("Enter Service name")
        self.service_description = self.page.get_by_placeholder("description")
        self.create_service_button = self.page.locator("button:has-text('Create Service')")
        self.service_confirmation_msg = self.page.get_by_text("Service created successfully!")

        # business process locators
        self.select_business_process = self.page.locator("div span:has-text('Business Process')")
        self.business_process_name = self.page.get_by_placeholder("Enter Business Process name")
        self.business_process_description = self.page.get_by_placeholder("description")
        self.create_business_process_button = self.page.locator("button:has-text('Create Business Process')")
        self.business_process_confirmation_msg = self.page.get_by_text("Business process created successfully!")





    def get_org_structure_text(self):
        # Return the organization structure setting text.
        try:
            return self.txt_org_setting
        except Exception as e:
            print(f" Exception while fetching organization setting text: {e}")
            return None

    def click_profile_confi(self):
        # Click the profile configuration.
        try:
            self.txt_profile_configuration.click()
        except Exception as e:
            print(f" Exception while click profile configuration: {e}")
            raise

    def click_organization_structure(self):
        # Click the organization structure.
        try:
            self.txt_org_structure.click()
        except Exception as e:
            print(f" Exception while click organization structure: {e}")
            raise

    def click_structure_tab(self):
        # Click the structure tab.
        try:
            self.btn_structure_tab.click()
        except Exception as e:
            print(f" Exception while click structure tab: {e}")
            raise

    def click_plus_symbol(self):
        # Click the plus symbol .
        try:
            self.btn_plus_symbol.click()
        except Exception as e:
            print(f" Exception while click plus symbol: {e}")
            raise

    def click_select_type_dropdown(self):
        # Click the select type dropdown .
        try:
            self.dropdown_select_type.click()
        except Exception as e:
            print(f" Exception while click select type dropdown : {e}")
            raise

    def click_select_legal_entity(self):
        # Click the select legal entity .
        try:
            self.select_legal_entity.click()
        except Exception as e:
            print(f" Exception while selecting legal entity : {e}")
            raise


    def fill_org_structure_form(self, name: str, description: str, comp_address: str):
        # fill all required details
        self.txt_name.fill(name)
        self.txt_description.fill(description)
        self.txt_company_address.fill(comp_address)

        # click and select country
        self.txt_country.click()
        self.select_country_name.click()

        # click and select industries
        self.txt_industries.click()
        self.select_industry_name.click()
        self.close_industry_name.click()

        # click and select region
        self.txt_region.click()
        self.select_region_name.click()

        # click and select regulation
        self.txt_regulation.click()
        self.select_regulation_name.click()
        self.close_regulation_name.click()

        # click and select
        self.txt_dpo.click()
        self.select_dop_name.click()

        # click and select risk matrix and data principal category
        self.txt_risk_matrix.click()
        self.txt_matrix_name.fill("Matrix 1")
        time.sleep(3)
        self.txt_data_principal_category.click()
        self.parent_checkboxes.nth(1).click()
        self.checkboxes_text.nth(1).click()
        self.child_checkboxes.nth(0).click()
        self.child_checkboxes.nth(1).click()
        self.child_checkboxes.nth(2).click()


    def click_create_legal_entity_button(self):
        # Click the create legal entity button.
        try:
            self.btn_create_legal_entity.click()
        except Exception as e:
            print(f" Exception while clicking create legal entity button : {e}")
            raise

    def click_continue_button(self):
        # Click the continue button.
        try:
            self.btn_continue.click()
        except Exception as e:
            print(f" Exception while clicking continue button : {e}")
            raise

    def get_success_message(self):
        # Return the success message.
        try:
            return self.success_msg
        except Exception as e:
            print(f" Exception while verify success message : {e}")
            return None

    def count_legal_entity(self, org_name:str):
        try:
            count = self.legal_entities.count()
            for i in range(count):
                text = self.legal_entities.nth(i).inner_text()
                if text == org_name:
                    self.plus_btn.nth(i).click()

        except Exception as e:
            print(f"Error while count the legal entity : {e}")
            return None

    def get_plus_btn_title(self):
        # Return the plus button title.
        try:
            return self.plus_btn_title
        except Exception as e:
            print(f" Exception while fetching plus button title: {e}")
            return None

    def business_unit_fill(self,name:str,description:str):
        try:
            self.dropdown_select_type.click()
            self.select_business_unit.click()
            self.business_unit_name.fill(name)
            self.business_unit_description.fill(description)
            self.create_business_unit_button.click()
        except Exception as e:
            print(f" Exception while fetching business unit: {e}")
            return None


    def busniness_unit_confirmation_msg(self):
        # Return the confirmation message.
        try:
            return self.confirmation_msg
        except Exception as e:
            print(f" Exception while fetching the confirmation message: {e}")
            return None


    def department_fill(self,name:str,description:str):
        try:
            self.dropdown_select_type.click()
            self.select_department.click()
            self.department_name.fill(name)
            self.department_description.fill(description)
            self.create_department_button.click()
        except Exception as e:
            print(f" Exception while filling department text: {e}")
            return None

    def department_confirmation_message(self):
        try:
            return self.department_confirmation_msg
        except Exception as e:
            print(f" Exception while filling department confirmation message: {e}")
            return None


    def product_fill(self,name:str,description:str):
        try:
            self.dropdown_select_type.click()
            self.select_product.click()
            self.product_name.fill(name)
            self.product_description.fill(description)
            self.create_product_button.click()
        except Exception as e:
            print(f" Exception while filling product text: {e}")
            return None

    def product_confirmation_message(self):
        try:
            return self.product_confirmation_msg
        except Exception as e:
            print(f" Exception while fetching product confirmation message: {e}")
            return None

    def service_fill(self,name:str,description:str):
        try:
            self.dropdown_select_type.click()
            self.select_service.click()
            self.service_name.fill(name)
            self.service_description.fill(description)
            self.create_service_button.click()
        except Exception as e:
            print(f" Exception while filling service form: {e}")
            return None

    def service_confirmation_message(self):
        try:
            return self.service_confirmation_msg
        except Exception as e:
            print(f" Exception while fetching service confirmation message: {e}")
            return None


    def business_process_fill(self,name:str,description:str):
        try:
            self.dropdown_select_type.click()
            self.select_business_process.click()
            self.business_process_name.fill(name)
            self.business_process_description.fill(description)
            self.create_business_process_button.click()
        except Exception as e:
            print(f" Exception while filling business process form: {e}")
            return None

    def business_process_confirmation_message(self):
        try:
            return self.business_process_confirmation_msg
        except Exception as e:
            print(f" Exception while fetching business process confirmation message: {e}")
            return None