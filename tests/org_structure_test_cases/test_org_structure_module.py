import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.org_structure_page import OrgStructurePage
from config import Config
from utilities.random_data_util import RandomDataUtil


@pytest.fixture(scope="function")
def setup_org_structure(page):

    login_page = LoginPage(page)
    org_structure = OrgStructurePage(page)

    # Login
    login_page.login(Config.dpo_email, Config.dpo_password)

    # Navigate to Organization Structure
    expect(org_structure.txt_profile_configuration).to_be_visible(timeout=15000)

    org_structure.click_profile_confi()
    org_structure.click_organization_structure()
    org_structure.click_organization_structure()

    expect(org_structure.txt_org_setting).to_be_visible(timeout=10000)

    return page, org_structure


# ==============================
# TEST : Structure Tab
# ==============================

def test_click_structure_tab(setup_org_structure):

    page, org_structure = setup_org_structure

    org_structure.click_structure_tab()

    expect(org_structure.txt_structure_tab).to_be_visible(timeout=10000)


# ==============================
# TEST : Plus Symbol
# ==============================

def test_click_plus_symbol(setup_org_structure):

    page, org_structure = setup_org_structure

    org_structure.click_structure_tab()
    org_structure.click_plus_symbol()

    expect(org_structure.dropdown_select_type).to_be_visible(timeout=10000)


# ==============================
# TEST : Select Legal Entity
# ==============================

def test_select_legal_entity_txt(setup_org_structure):

    page, org_structure = setup_org_structure

    org_structure.click_structure_tab()
    org_structure.click_plus_symbol()
    org_structure.click_select_type_dropdown()
    org_structure.click_select_legal_entity()

    expect(org_structure.txt_name).to_be_visible(timeout=10000)


# ==============================
# TEST : Fill Legal Entity Form
# ==============================

def test_fill_name_desc_add_org_structure_form(setup_org_structure):

    page, org_structure = setup_org_structure

    org_structure.click_structure_tab()
    org_structure.click_plus_symbol()
    org_structure.click_select_type_dropdown()
    org_structure.click_select_legal_entity()

    random_data = RandomDataUtil()
    org_structure.fill_name_des_add_in_org_structure_form(

        random_data.get_legal_entity_name(),
        random_data.get_description(),
        random_data.get_random_address()



        # Config.legal_entity_name,
        # Config.legal_entity_description,
        # Config.legal_entity_address
    )

    expect(org_structure.btn_create_legal_entity).to_be_visible(timeout=10000)


# ==============================
# TEST : select country name in the organization structure
# ==============================

def test_select_country_in_org_structure_form(setup_org_structure):

    page, org_structure = setup_org_structure

    org_structure.click_structure_tab()
    org_structure.click_plus_symbol()
    org_structure.click_select_type_dropdown()
    org_structure.click_select_legal_entity()

    random_data = RandomDataUtil()
    org_structure.select_county_in_org_structure_form(

        random_data.get_legal_entity_name(),
        random_data.get_description(),
        random_data.get_random_address()
    )
    expect(org_structure.select_country_name).to_be_visible(timeout=10000)


# ==============================
# TEST : Create Legal Entity
# ==============================

def test_create_legal_entity(setup_org_structure):

    page, org_structure = setup_org_structure

    org_structure.click_structure_tab()
    org_structure.click_plus_symbol()
    org_structure.click_select_type_dropdown()
    org_structure.click_select_legal_entity()

    org_structure.fill_org_structure_form(
        Config.legal_entity_name,
        Config.legal_entity_description,
        Config.legal_entity_address
    )

    org_structure.click_create_legal_entity_button()

    if org_structure.btn_continue.is_visible():
        org_structure.click_continue_button()

    success_message = org_structure.get_success_message()

    expect(success_message).to_be_visible(timeout=15000)


# ==============================
# TEST : Create Business Unit
# ==============================

def test_create_business_unit(setup_org_structure):

    page, org_structure = setup_org_structure

    org_structure.count_legal_entity(Config.legal_entity_name)

    expect(org_structure.get_plus_btn_title()).to_be_visible(timeout=10000)

    org_structure.business_unit_fill(
        Config.business_unit_name,
        Config.business_unit_description
    )

    expect(
        org_structure.busniness_unit_confirmation_msg()
    ).to_be_visible(timeout=15000)


# ==============================
# TEST : Create Department
# ==============================

def test_create_department(setup_org_structure):

    page, org_structure = setup_org_structure

    org_structure.count_legal_entity(Config.legal_entity_name)

    org_structure.department_fill(
        Config.department_name,
        Config.department_description
    )

    expect(
        org_structure.department_confirmation_message()
    ).to_be_visible(timeout=15000)


# ==============================
# TEST : Create Product
# ==============================

def test_create_product(setup_org_structure):

    page, org_structure = setup_org_structure

    org_structure.count_legal_entity(Config.legal_entity_name)

    org_structure.product_fill(
        Config.product_name,
        Config.product_description
    )

    expect(
        org_structure.product_confirmation_message()
    ).to_be_visible(timeout=15000)


# ==============================
# TEST : Create Service
# ==============================

def test_create_service(setup_org_structure):

    page, org_structure = setup_org_structure

    org_structure.count_legal_entity(Config.legal_entity_name)

    org_structure.service_fill(
        Config.service_name,
        Config.service_description
    )

    expect(
        org_structure.service_confirmation_message()
    ).to_be_visible(timeout=15000)


# ==============================
# TEST : Create Business Process
# ==============================

def test_create_business_process(setup_org_structure):

    page, org_structure = setup_org_structure

    org_structure.count_legal_entity(Config.legal_entity_name)

    org_structure.business_process_fill(
        Config.business_process_name,
        Config.business_process_description
    )

    expect(
        org_structure.business_process_confirmation_message()
    ).to_be_visible(timeout=15000)