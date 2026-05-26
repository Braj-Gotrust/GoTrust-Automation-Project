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
    preference_center_title_name = Config.preference_center_title_name
    source_name = "Form"
    file_path = Config.file_path

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

        # select consent template
        ucm.page_extend()
        ucm.select_consent_template(consent_template_name)
        expect(ucm.get_consent_template_title()).to_be_visible(timeout=15000)
        time.sleep(3)

        # ###============step 1 - Basic Info============================
        ucm.unique_data_identifier_txt.first.click()
        ucm.select_pii_label_in_list(pii_label_name)
        # click on continue button
        ucm.click_continue_btn()

        # ###============step 2 - Processing Purpose============================
        ucm.click_continue_btn()
        time.sleep(3)

        # ###============step 3 - Privacy Notice============================
        if ucm.exist_btn.is_visible():
            ucm.exist_btn.click()
            # select privacy notice
            ucm.select_privacy_notice(privacy_notice_name)
        ucm.click_continue_btn()

        ###============step 4 - Sources or consent form============================
        ucm.click_continue_btn()
        time.sleep(3)

        ###============step 5 - Preference Center============================
        ucm.enter_preference_center_title(preference_center_title_name)
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        ucm.click_reset_btn()
        expect(ucm.get_reset_confirmation_attribute().nth(0)).to_be_visible(timeout=15000)

        ucm.click_full_screen_btn()
        ucm.click_cross_btn()
        # again upload logo
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))

        # mobile view under the user input tab
        ucm.click_switch_btn()
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        ucm.click_reset_btn()
        expect(ucm.get_reset_confirmation_attribute().nth(0)).to_be_visible(timeout=15000)

        ucm.click_full_screen_btn()
        ucm.click_cross_btn()
        # again upload logo
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))


        # VERIFY INPUT TAB under the mobile view
        time.sleep(1)
        ucm.click_verify_input_tab()
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        ucm.click_reset_btn()
        expect(ucm.get_reset_confirmation_attribute().nth(0)).to_be_visible(timeout=15000)

        ucm.click_full_screen_btn()
        ucm.click_cross_btn()
        # again upload logo
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        # swap button order
        ucm.click_swap_button_order()

        # laptop view under the VERIFY INPUT TAB
        ucm.click_switch_btn()
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        ucm.click_reset_btn()
        expect(ucm.get_reset_confirmation_attribute().nth(0)).to_be_visible(timeout=15000)

        ucm.click_full_screen_btn()
        ucm.click_cross_btn()
        # again upload logo
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        # swap button order
        ucm.click_swap_button_order()

        # preference center tab under the laptop view
        ucm.click_preference_center_tab()
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        ucm.click_reset_btn()
        expect(ucm.get_reset_confirmation_attribute().nth(0)).to_be_visible(timeout=15000)
        # again upload logo
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))

        # preference center page tab under the preference center tab
        ucm.click_preference_center_page_tab()

        # mobile view under the PREFERENCE CENTER
        ucm.click_switch_btn()
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))
        ucm.click_reset_btn()
        expect(ucm.get_reset_confirmation_attribute().nth(0)).to_be_visible(timeout=15000)
        # again upload logo
        ucm.upload_logo(file_path)
        expect(ucm.get_logo_upload_confi_attribute()).to_have_attribute("src", re.compile(
            r"https://storage-pp.gotrust.tech/gt-logo-bucket/uploads"))

        # preference center page tab under the preference center tab
        ucm.click_preference_center_page_tab()
        time.sleep(3)
        ucm.click_continue_btn()
        time.sleep(1)

        # ###============step 6 - Language============================
        ucm.change_language()
        expect(ucm.get_change_language_confi_msg()).to_be_visible(timeout=15000)
        ucm.click_continue_btn()

        # ###============step 7 - Code Snippets============================
        ucm.click_code_snippets_page_tab()
        ucm.click_download_btn()
        expect(ucm.get_download_title_txt()).to_be_visible(timeout=15000)
        ucm.click_download_cross_btn()
        ucm.click_continue_btn()

        # ###============step 8 - Workflow============================
        ucm.click_save_btn()
        # verify ucm title
        expect(ucm.get_ucm_title()).to_be_visible(timeout=15000)
        print("\nPreference center customization successfully")















        page.wait_for_timeout(5000)

    else:
        # Invalid login validation
        expect(login_page.txt_error_message).to_be_visible(timeout=5000)

