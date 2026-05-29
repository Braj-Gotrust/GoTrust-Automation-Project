import re

from pages.login_page import LoginPage
from pages.ccm_page import CcmPage
from playwright.sync_api import expect
from config import Config


def test_ucm_1(page):
    # TEST DATA
    dpo_email = Config.dpo_email
    dpo_password = Config.dpo_password

    domain_name = Config.domain_name
    domain_url = Config.domain_url
    cookie_policy_link= Config.cookie_policy_link
    legal_entity_name = Config.legal_entity_name

    category_name = Config.category_name
    category_description = Config.category_description

    service_name = Config.services_name
    service_description = Config.services_description

    cookie_key_name = Config.cookie_key_name
    cookie_key_description = Config.cookie_key_description

    file_path = Config.file_path

    login_page = LoginPage(page)
    login_page.login(dpo_email, dpo_password)

    ccm = CcmPage(page)

    if True:


        # verify ccm button
        expect(ccm.ccm_btn).to_be_visible(timeout=15000)

        # click on ccm
        ccm.click_ccm_btn()

        # verify ccm title
        expect(ccm.get_ccm_title()).to_be_visible(timeout=15000)

        # click on banner builder tab
        ccm.click_banner_builder_tab()

        # STEP:1 - Basic Information
        # fill domain details
        ccm.fill_domain_details(domain_name, domain_url, cookie_policy_link)
        expect(ccm.get_create_domain_confi_msg()).to_be_visible(timeout=15000)

        # STEP:2 - Website Scan
        ccm.click_scan_now_btn()
        ccm.click_next_btn()

        # STEP:3 - Categorize Cookie
        # category and service tab
        ccm.click_category_and_service_tab()

        # add category
        ccm.fill_category_details(category_name, category_description)
        expect(ccm.get_add_category_confi_msg()).to_be_visible(timeout=15000)

        # select category name
        ccm.select_category(category_name)
        ccm.fill_service_details(service_name, service_description)
        expect(ccm.get_add_service_confi_msg()).to_be_visible(timeout=15000)

        # unique cookies tab
        ccm.click_unique_cookies_tab()
        ccm.fill_cookie_details(cookie_key_name, cookie_key_description, category_name, service_name)
        expect(ccm.get_add_cookie_confi_msg()).to_be_visible(timeout=15000)

        # next button
        ccm.click_next_btn()

        # STEP:4 - User Consent Renewal
        ccm.take_user_consent_renewal()

        # STEP:5 - Customize Banner
        ccm.upload_logo(file_path)
        expect(ccm.get_logo_upload_confi_msg()).to_have_attribute("src", re.compile(r"data:image"))
        ccm.select_checkbox()
        ccm.click_reset_banner_btn()
        expect(ccm.get_reset_confi_msg()).to_be_visible(timeout=15000)
        ccm.customize_banner(file_path)

        # next button
        ccm.click_next_btn()

        # STEP:6 - Language Support
        ccm.change_language()
        expect(ccm.get_change_language_confi_msg()).to_be_visible(timeout=15000)

        # next button
        ccm.click_next_btn()

        # STEP:7 - Consent Code
        ccm.click_banner_preview_btn()





        page.wait_for_timeout(5000)

    else:
        # Invalid login validation
        expect(login_page.txt_error_message).to_be_visible(timeout=5000)