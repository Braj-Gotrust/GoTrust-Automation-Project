import re

from pages.login_page import LoginPage
from pages.ccm_page import CcmPage
from playwright.sync_api import expect
from config import Config


def test_ccm_2(page):
    # TEST DATA
    dpo_email = Config.dpo_email
    dpo_password = Config.dpo_password

    domain_name = Config.domain_name
    domain_url = Config.domain_url
    cookie_policy_link= Config.cookie_policy_link
    legal_entity_name = Config.legal_entity_name

    cookie_policy_title = Config.cookie_policy_title

    #category_name = Config.category_name
    category_name = "Essential"
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

        # click on ccm
        ccm.click_ccm_btn()

        # click all cookie policy tab
        ccm.click_all_cookie_policy_tab()

        # click on cookie policy tab
        ccm.click_cookie_policy_tab()

        # create cookie policy
        ccm.create_cookie_policy(domain_name, cookie_policy_title)
        expect(ccm.get_add_cookie_table_confi_msg()).to_be_visible(timeout=15000)
        ccm.click_save_change_btn()
        expect(ccm.get_cookie_policy_create_confi_msg()).to_be_visible(timeout=15000)
        ccm.click_close_btn()





        page.wait_for_timeout(5000)

    else:
        # Invalid login validation
        expect(login_page.txt_error_message).to_be_visible(timeout=5000)