from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.ropa_page import RopaPage
from playwright.sync_api import expect
from config import Config


def test_ropa(page):
    # TEST DATA
    dpo_email = Config.dpo_email
    dpo_password = Config.dpo_password

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
    legal_entity_name = Config.legal_entity_name

    is_future = True
    month_year = Config.month_and_year
    date = Config.date
    assignee_name = Config.assignee_name
    select_level_1_reviewer = Config.reviewer_1_name
    select_level_2_reviewer = Config.reviewer_2_name
    collaborator_name = Config.collaborator_name



    login_page = LoginPage(page)
    login_page.login(dpo_email, dpo_password)
    #login_page.login(collaborator_email, collaborator_password)
    #login_page.login(assignee_email, assignee_password)
    #login_page.login(reviewer_1_email, reviewer_1_password)
    #login_page.login(reviewer_2_email, reviewer_2_password)

    ropa = RopaPage(page)

    logout_page = LogoutPage(page)


    if True:

        # verify ropa registry button
        expect(ropa.ropa_registry_btn).to_be_visible(timeout=15000)

        # click on ropa
        ropa.click_ropa_registry_btn()

        # verify ropa title
        expect(ropa.get_ropa_registry_title()).to_be_visible(timeout=15000)

        # click processing activity button
        ropa.click_processing_activity_btn()
        expect(ropa.get_ropa_form_title()).to_be_visible(timeout=15000)

        # fill processing activity form
        ropa.processing_activity_form(processing_activity_name,processing_activity_description,legal_entity_name)
        ropa.select_due_date(month_year,date,is_future)

        # select assignee
        ropa.select_assignee(assignee_name)

        # verify level 2 reviewer title
        expect(ropa.get_level_2_reviewer_title()).to_be_visible(timeout=15000)

        # Select level 1 reviewer
        ropa.select_level_1_reviewer(select_level_1_reviewer)

        # verify level 3 reviewer title
        expect(ropa.get_level_3_reviewer_title()).to_be_visible(timeout=15000)

        # Select level 2 reviewer
        ropa.select_level_2_reviewer(select_level_2_reviewer)

        # click on ropa and get title of ropa
        expect(ropa.click_and_get_title_ropa()).to_be_visible(timeout=15000)

        # click on add collaborator and get title of collaborator
        expect(ropa.click_and_get_collab_popup()).to_be_visible(timeout=15000)

        # select collaborator
        ropa.select_collaborator(collaborator_name)

        # click on collaborator submit and get confirmation message of collaborator
        expect(ropa.click_and_get_collab_confi_msg()).to_be_visible(timeout=15000)

        # selec role
        ropa.click_and_select_role()
        # click on update and message
        expect(ropa.click_update_btn_and_get_msg()).to_be_visible(timeout=15000)

        # data principal tagging section
        ropa.data_principal_tagging_section()
        # click on update data principal tagging and message
        expect(ropa.click_update_data_principal_tagging_btn_and_get_msg()).to_be_visible(timeout=15000)

        # pii tagging section
        ropa.pii_tagging_section()
        # click on update data principal tagging and message
        expect(ropa.click_update_pii_tagging_btn_and_get_msg()).to_be_visible(timeout=15000)

        # DPO SIGN OUT
        logout_page.signout()

        # LOGIN WITH COLLABORATOR ACCOUNT
        login_page.login(collaborator_email,collaborator_password)

        # click on ropa
        ropa.click_ropa_registry_btn()

        # verify ropa title
        expect(ropa.get_ropa_registry_title()).to_be_visible(timeout=15000)

        # select and edit ROPA
        ropa.select_and_edit_processing_activity(processing_activity_name)
        expect(ropa.get_edit_ropa_page_title()).to_be_visible(timeout=15000)

        # Legal basis section
        ropa.legal_basis_section()
        # click on update legal basis and message
        expect(ropa.click_update_legal_basis_btn_and_get_msg()).to_be_visible(timeout=15000)

        # collaborator submit for review and get confirmation message
        expect(ropa.click_collab_submit_for_review_btn_and_get_msg()).to_be_visible(timeout=15000)

        # COLLABORATOR SIGN OUT
        logout_page.signout()

        # ASSIGNEE SIGN IN
        login_page.login(assignee_email,assignee_password)

        # click on ropa
        ropa.click_ropa_registry_btn()

        # verify ropa title
        expect(ropa.get_ropa_registry_title()).to_be_visible(timeout=15000)

        # select and edit ROPA
        ropa.select_and_edit_processing_activity(processing_activity_name)
        expect(ropa.get_edit_ropa_page_title()).to_be_visible(timeout=15000)

        # assignee submit for review and get confirmation message
        expect(ropa.click_assignee_submit_for_review_btn_and_get_msg()).to_be_visible(timeout=15000)

        # ASSIGNEE SIGN OUT
        logout_page.signout()


        # REVIEWER 1 ACCOUNT LOGIN
        login_page.login(reviewer_1_email,reviewer_1_password)
        # click on ropa
        ropa.click_ropa_registry_btn()
        # verify ropa title
        expect(ropa.get_ropa_registry_title()).to_be_visible(timeout=15000)
        # select and edit ROPA
        ropa.select_and_edit_processing_activity(processing_activity_name)
        expect(ropa.get_edit_ropa_page_title()).to_be_visible(timeout=15000)

        # reviewer 1 acknowledge (submit) and get confirmation message
        expect(ropa.click_reviewer_acknowledge_btn_and_get_msg()).to_be_visible(timeout=15000)

        # REVIEWER 1 SIGN OUT
        logout_page.signout()

        # REVIEWER 2 SING IN
        login_page.login(reviewer_2_email,reviewer_2_password)
        # click on ropa
        ropa.click_ropa_registry_btn()
        # verify ropa title
        expect(ropa.get_ropa_registry_title()).to_be_visible(timeout=15000)
        # select and edit ROPA
        ropa.select_and_edit_processing_activity(processing_activity_name)
        expect(ropa.get_edit_ropa_page_title()).to_be_visible(timeout=15000)

        # reviewer 2 acknowledge (submit) and get confirmation message
        expect(ropa.click_reviewer_acknowledge_btn_and_get_msg()).to_be_visible(timeout=15000)





        page.wait_for_timeout(5000)

    else:
        # Invalid login validation
        expect(login_page.txt_error_message).to_be_visible(timeout=5000)


