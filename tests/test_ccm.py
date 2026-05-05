from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from pages.dpia_page import DpiaPage
from pages.ccm_page import CcmPage
from playwright.sync_api import expect
from config import Config


def test_ccm(page):
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

        # fill domain details
        ccm.fill_domain_details(domain_name, domain_url, cookie_policy_link)
        expect(ccm.get_create_domain_confi_msg()).to_be_visible(timeout=15000)
        ccm.click_scan_now_btn()
        ccm.click_next_btn()

        # click on category and service tab
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

        # compliance tab
        ccm.click_compliance_tab()
        ccm.fill_observation_details()
        expect(ccm.get_add_observation_confi_msg()).to_be_visible(timeout=15000)
        # add duty
        ccm.fill_duty_details()
        expect(ccm.get_add_duty_confi_msg()).to_be_visible(timeout=15000)
        # add action
        ccm.fill_action_details()
        expect(ccm.get_add_action_confi_msg()).to_be_visible(timeout=15000)

        # recommendations tab
        ccm.click_recommendations_tab()












        page.wait_for_timeout(5000)

    else:
        # Invalid login validation
        expect(login_page.txt_error_message).to_be_visible(timeout=5000)