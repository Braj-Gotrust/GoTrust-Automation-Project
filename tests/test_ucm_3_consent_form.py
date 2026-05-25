import re
import time

from pages.login_page import LoginPage
from pages.ucm_page import UcmPage
from playwright.sync_api import expect
from config import Config



def test_ucm_1(page):
    # TEST DATA
    dpo_email = Config.dpo_email
    dpo_password = Config.dpo_password

    consent_template_name = Config.consent_template_name
    pii_label_name = Config.pii_label_name
    legal_entity_name = Config.legal_entity_name
    privacy_notice_name = Config.privacy_notice_name
    source_name = "Form"
    file_path = Config.file_path
    processing_purpose_name = Config.processing_purpose_name

    login_page = LoginPage(page)
    login_page.login(dpo_email, dpo_password)

    ucm = UcmPage(page)

    if True:

        # click on ucm lab
        ucm.click_ucm_lab_btn()

        # verify consent collection builder button is visible
        expect(ucm.consent_collection_builder_btn).to_be_visible(timeout=15000)

        # click on consent collection builder button    
        ucm.click_consent_collection_builder_btn()

        # verify ucm title
        expect(ucm.get_ucm_title()).to_be_visible(timeout=15000)

        # ###============step 1 - Basic Info============================
        # # create consent template
        ucm.click_create_consent_template(consent_template_name, legal_entity_name, pii_label_name)

        # click on continue button
        ucm.click_continue_btn()
        expect(ucm.get_record_create_confirmation_msg()).to_be_visible(timeout=15000)

        ###============step 2 - Processing Purpose============================
        ucm.add_processing_purpose(processing_purpose_name, pii_label_name)
        expect(ucm.get_record_create_confirmation_msg()).to_be_visible(timeout=15000)

        # click on continue button
        ucm.click_continue_btn()

        ###============step 3 - Privacy Notice============================
        ucm.click_exist_btn()
        ucm.select_privacy_notice(privacy_notice_name)
        ucm.click_continue_btn()

        ##============step 4 - Sources or consent form============================
        ucm.select_source(source_name)
        ucm.fill_consent_form_title_and_description()
        ucm.click_next_btn()
        expect(ucm.get_record_create_confirmation_msg()).to_be_visible(timeout=15000)
        ucm.click_customize_form_txt()
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        ucm.click_reset_btn()
        expect(ucm.get_reset_confirmation_attribute().nth(0)).to_be_visible(timeout=15000)
        # again upload logo
        ucm.upload_logo(file_path)
        # mobile view
        ucm.click_switch_btn()
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        ucm.click_reset_btn()
        expect(ucm.get_reset_confirmation_attribute().nth(0)).to_be_visible(timeout=15000)
        # again upload logo
        ucm.upload_logo(file_path)

        ucm.click_continue_btn()










        page.wait_for_timeout(5000)

    else:
        # Invalid login validation
        expect(login_page.txt_error_message).to_be_visible(timeout=5000)

