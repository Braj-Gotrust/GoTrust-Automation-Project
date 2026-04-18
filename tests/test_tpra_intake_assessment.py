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
    legal_entity_name = Config.legal_entity_name
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

    reviewer_2_email = Config.reviewer_2_email
    reviewer_2_password = Config.reviewer_2_password

    processing_activity_name = Config.processing_activity_name
    processing_activity_description = Config.processing_activity_description


    is_future = True
    month_year = Config.month_and_year
    date = Config.date







    login_page = LoginPage(page)
    #login_page.login(dpo_email, dpo_password)
    #login_page.login(collaborator_email, collaborator_password)
    #login_page.login(assignee_email, assignee_password)
    login_page.login(reviewer_1_email, reviewer_1_password)
    #login_page.login(reviewer_2_email, reviewer_2_password)

    ropa = RopaPage(page)
    tpra = TpraPage(page)

    logout_page = LogoutPage(page)


    if True:
        '''
        # verify TPRA button
        expect(tpra.tpra_btn).to_be_visible(timeout=15000)

        # click on ropa
        tpra.click_tpra_btn()

        # verify TPRA title
        expect(tpra.get_tpra_title()).to_be_visible(timeout=15000)

        # fill vendor details
        # tpra.fill_vendor_details(vendor_name, vendor_email, vendor_address, vendor_admin_name, vendor_phone_number, legal_entity_name)
        # expect(tpra.get_vendor_add_confi_msg()).to_be_visible(timeout=15000)

        # select vendor assessment name under the "TPRA Dashboard"
        tpra.select_vendor_name_assessment(vendor_name)
        tpra.fill_vendor_assessment_details(vendor_assessment_description, legal_entity_name, spoc_name, assignee_name, reviewer_name)
        expect(tpra.get_vendor_assessment_confi_msg()).to_be_visible(timeout=15000)

        # select vendor assessment under the vendor 'vendor assessment name'
        tpra.select_vendor_assessment()
        tpra.click_save_and_next_btn()

        # collaborator add
        tpra.select_collaborator(collaborator_name)
        expect(tpra.get_collaborator_add_confi_msg()).to_be_visible(timeout=15000)

        # DPO SIGN OUT
        logout_page.signout()

        # COLLABORATOR SIGN IN
        login_page.login(collaborator_email, collaborator_password)

        # click on ropa
        tpra.click_tpra_btn()
        # select vendor assessment name under the "TPRA Dashboard"
        tpra.select_vendor_name_assessment(vendor_name)
        # select vendor assessment under the 'vendor assessment name'
        tpra.select_vendor_assessment()
        # questions and answers
        tpra.questions_and_answers()
        expect(tpra.get_save_msg()).to_be_visible(timeout=15000)

        # COLLABORATOR SIGN OUT
        logout_page.signout()


        # ASSIGNEE SIGN IN
        login_page.login(assignee_email, assignee_password)

        # click on ropa
        tpra.click_tpra_btn()
        # select vendor assessment name under the "TPRA Dashboard"
        tpra.select_vendor_name_assessment(vendor_name)
        # select vendor assessment under the 'vendor assessment name'
        tpra.select_vendor_assessment()
        # save and submit for review button
        tpra.click_save_btn()
        tpra.click_submit_for_review_btn()

        # ASSIGNEE SIGN OUT
        logout_page.signout()

        # REVIEWER SIGN IN
        login_page.login(reviewer_1_email, reviewer_1_password)
        '''

        # click on ropa
        tpra.click_tpra_btn()
        # select vendor assessment name under the "TPRA Dashboard"
        tpra.select_vendor_name_assessment(vendor_name)
        # select vendor assessment under the 'vendor assessment name'
        tpra.select_vendor_assessment()
        # reviewer review all questions and answers
        tpra.review_questions_and_answers()









        page.wait_for_timeout(5000)


    else:
        # Invalid login validation
        expect(login_page.txt_error_message).to_be_visible(timeout=5000)
