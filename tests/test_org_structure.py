import time
import pytest
from pages.login_page import LoginPage
from pages.org_structure_page import OrgStructurePage
from utilities.data_reader_util import read_csv_data
from playwright.sync_api import expect
from config import Config


def test_organization_structure(page):

    # TEST DATA
    dpo_email = Config.dpo_email
    dpo_password = Config.dpo_password

    legal_entity_name = Config.legal_entity_name
    legal_entity_description = Config.legal_entity_description
    legal_entity_address = Config.legal_entity_address

    business_unit_name = Config.business_unit_name
    business_unit_description = Config.business_unit_description

    department_name = Config.department_name
    department_description= Config.department_description

    product_name = Config.product_name
    product_description = Config.product_description

    service_name = Config.service_name
    service_description = Config.service_description

    business_process_name = Config.business_process_name
    business_process_description = Config.business_process_description



    login_page = LoginPage(page)
    org_structure = OrgStructurePage(page)
    login_page.login(dpo_email, dpo_password)
    # time.sleep(1)

    if True:
        # Wait for dashboard load
        profile_btn = org_structure.txt_profile_configuration
        expect(profile_btn).to_be_visible(timeout=15000)

        # Open profile dropdown
        org_structure.click_profile_confi()

        # First click on the organization structure button
        org_structure.click_organization_structure()

        # Second click on the organization structure button
        org_structure.click_organization_structure()
        expect(org_structure.txt_org_setting).to_be_visible()

        # Click Structure tab
        org_structure.click_structure_tab()
        expect(org_structure.txt_structure_tab).to_be_visible()

        # click plus symbol
        org_structure.click_plus_symbol()

        # click select type dropdown
        org_structure.click_select_type_dropdown()

        # select legal entity
        org_structure.click_select_legal_entity()

        # Fill organization from
        org_structure.fill_org_structure_form(legal_entity_name,legal_entity_description,legal_entity_address)

        # click create legal entity button
        org_structure.click_create_legal_entity_button()

        # validate successful message
        if org_structure.btn_continue.is_visible():
            org_structure.click_continue_button()

        # Get successful message
        success_message = org_structure.get_success_message()
        expect(success_message).to_be_visible(timeout=10000)


        # count legal entity
        org_structure.count_legal_entity(legal_entity_name)
        plus_button_title = org_structure.get_plus_btn_title()
        expect(plus_button_title).to_be_visible(timeout=15000)

        # Business Unit
        org_structure.business_unit_fill(business_unit_name, business_unit_description)
        business_unit_confirmation_msg=org_structure.busniness_unit_confirmation_msg()
        expect(business_unit_confirmation_msg).to_be_visible(timeout=15000)


        # DEPARTMENT
        org_structure.count_legal_entity(legal_entity_name)   # plus button click
        org_structure.department_fill(department_name, department_description)
        department_confirmation_msg = org_structure.department_confirmation_message()
        expect(department_confirmation_msg).to_be_visible(timeout=15000)

        # PRODUCT
        org_structure.count_legal_entity(legal_entity_name)  # plus button click
        org_structure.product_fill(product_name, product_description)
        product_confirmation_msg = org_structure.product_confirmation_message()
        expect(product_confirmation_msg).to_be_visible(timeout=15000)

        # SERVICE
        org_structure.count_legal_entity(legal_entity_name)  # plus button click
        org_structure.service_fill(service_name, service_description)
        service_confirmation_msg = org_structure.service_confirmation_message()
        expect(service_confirmation_msg).to_be_visible(timeout=15000)

        # BUSINESS PROCESS
        org_structure.count_legal_entity(legal_entity_name)  # plus button click
        org_structure.business_process_fill(business_process_name, business_process_description)
        business_process_confirmation_msg = org_structure.business_process_confirmation_message()
        expect(business_process_confirmation_msg).to_be_visible(timeout=15000)





        page.wait_for_timeout(3000)

    else:
        # Invalid login validation
        expect(login_page.txt_error_message).to_be_visible(timeout=5000)


