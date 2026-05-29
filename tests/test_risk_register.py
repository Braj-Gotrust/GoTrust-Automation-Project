from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.ropa_page import RopaPage
from pages.tpra_page import TpraPage
from playwright.sync_api import expect
from config import Config


def test_tpra_intake_assessment(page):
    # TEST DATA
    dpo_email = Config.dpo_email
    dpo_password = Config.dpo_password

    vendor_name = Config.vendor_name
    vendor_email = Config.vendor_email
    vendor_address = Config.vendor_address
    vendor_admin_name = Config.vendor_admin_name
    vendor_phone_number = Config.vendor_phone_number
    #legal_entity_name = Config.legal_entity_name
    legal_entity_name = "GoTrust"
    vendor_assessment_description = Config.vendor_assessment_description
    spoc_name = Config.reviewer_2_name
    assignee_name = Config.assignee_name
    reviewer_name = Config.reviewer_1_name
    collaborator_name = Config.collaborator_name

    collaborator_email = Config.collaborator_email
    collaborator_password = Config.collaborator_password

    assignee_email = Config.assignee_email
    assignee_password = Config.assignee_password

    reviewer_1_email = Config.reviewer_1_email
    reviewer_1_password = Config.reviewer_1_password



    login_page = LoginPage(page)
    login_page.login(dpo_email, dpo_password)
    #login_page.login(collaborator_email, collaborator_password)
    #login_page.login(assignee_email, assignee_password)
    #login_page.login(reviewer_1_email, reviewer_1_password)
    #login_page.login(reviewer_2_email, reviewer_2_password)

    tpra = TpraPage(page)

    logout_page = LogoutPage(page)


    if True:

        # verify TPRA button
        expect(tpra.tpra_btn).to_be_visible(timeout=15000)

        # click on ropa
        tpra.click_tpra_btn()

        # verify TPRA title
        expect(tpra.get_tpra_title()).to_be_visible(timeout=15000)

        # fill vendor details
        tpra.fill_vendor_details(vendor_name, vendor_email, vendor_address, vendor_admin_name, vendor_phone_number, legal_entity_name)
        expect(tpra.get_vendor_add_confi_msg()).to_be_visible(timeout=15000)

        # select vendor assessment name under the "TPRA Dashboard"
        tpra.select_vendor_name_assessment(vendor_name)
        tpra.fill_vendor_assessment_details(vendor_assessment_description, legal_entity_name, spoc_name, assignee_name, reviewer_name)
        expect(tpra.get_vendor_assessment_confi_msg()).to_be_visible(timeout=15000)

        # select vendor assessment under the vendor 'vendor assessment name'
        tpra.select_vendor_assessment()
        tpra.click_save_and_next_btn()