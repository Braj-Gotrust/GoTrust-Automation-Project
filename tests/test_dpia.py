from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.dpia_page import DpiaPage
from playwright.sync_api import expect
from config import Config


def test_dpia(page):
    # TEST DATA
    dpo_email = Config.dpo_email
    dpo_password = Config.dpo_password

    dpia_assessment_name = Config.dpia_assessment_name
    dpia_assessment_description = Config.dpia_assessment_description
    legal_entity_name = Config.legal_entity_name

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

    dpia = DpiaPage(page)

    logout_page = LogoutPage(page)

    if True:


        # verify TPRA button
        expect(dpia.dpia_btn).to_be_visible(timeout=15000)

        # click on ropa
        dpia.click_dpia_btn()

        # verify TPRA title
        expect(dpia.get_dpia_title()).to_be_visible(timeout=15000)

        # fill vendor details
        dpia.fill_dpia_details(dpia_assessment_name, dpia_assessment_description, legal_entity_name, assignee_name, reviewer_name)
        expect(dpia.get_create_assessment_msg()).to_be_visible(timeout=15000)

        # select dpia assessment name
        dpia.select_assessment_start_and_continue(dpia_assessment_name)
        # add collaborator
        dpia.select_collaborator(collaborator_email)
        expect(dpia.get_collaborator_add_confi_msg()).to_be_visible(timeout=15000)
        dpia.close.first.click()

        # DPO SING OUT
        logout_page.signout()

        # COLLABORATOR SIGN IN
        login_page.login(collaborator_email, collaborator_password)


        # click on ropa
        dpia.click_dpia_btn()
        # select dpia assessment name
        dpia.select_assessment_start_and_continue(dpia_assessment_name)
        # assessment question answers
        dpia.collaborator_assessment_answers()
        dpia.get_submit_for_review_btn()

        # COLLABORATOR SING OUT
        logout_page.signout()

        # ASSIGNEE SIGN IN
        login_page.login(assignee_email, assignee_password)


        # click on ropa
        dpia.click_dpia_btn()
        # select dpia assessment name
        dpia.select_assessment_start_and_continue(dpia_assessment_name)
        # assessment question answers
        dpia.give_assessment_and_submit_for_review()

        # ASSIGNEE SIGN OUT
        logout_page.signout()

        # REVIEWER SIGN IN
        login_page.login(reviewer_1_email, reviewer_1_password)

        # click on DPIA
        dpia.click_dpia_btn()
        # select dpia assessment name
        dpia.select_assessment_and_review(dpia_assessment_name)

        # review assessment and change request
        dpia.assessment_review_and_change_request()

        # REVIEWER SIGN OUT
        logout_page.signout()

        # ASSIGNEE SIGN IN (AGAIN SIGN IN AFTER CHANGE REQUEST)
        login_page.login(assignee_email, assignee_password)

        # click on ropa
        dpia.click_dpia_btn()
        # select dpia assessment name
        dpia.select_assessment_and_edit(dpia_assessment_name)
        # assessment question answers
        dpia.give_assessment_and_submit_for_review()

        # ASSIGNEE SIGN OUT
        logout_page.signout()

        # REVIEWER SIGN IN (AGAIN SIGN IN AFTER CHANGE REQUEST)
        login_page.login(reviewer_1_email, reviewer_1_password)

        # click on ropa
        dpia.click_dpia_btn()
        # select dpia assessment name
        dpia.select_assessment_and_review(dpia_assessment_name)

        # review assessment and change request
        dpia.assessment_review_and_submit()

        page.wait_for_timeout(5000)

    else:
        # Invalid login validation
        expect(login_page.txt_error_message).to_be_visible(timeout=5000)