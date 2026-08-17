import re

from pages.login_page import LoginPage
from pages.ucm_page import UcmPage
from playwright.sync_api import expect
from config import Config



def test_ucm_2(page):
    # TEST DATA
    dpo_email = Config.dpo_email
    dpo_password = Config.dpo_password

    legal_entity_name = Config.legal_entity_name
    privacy_notice_name = Config.privacy_notice_name

    login_page = LoginPage(page)
    login_page.login(dpo_email, dpo_password)

    ucm = UcmPage(page)

    if True:

        # click on task overview button
        ucm.click_task_overview_btn()

        # verify privacy notice title
        expect(ucm.get_privacy_notice_title()).to_be_visible(timeout=15000)

        # click on privacy notice tab
        ucm.privacy_notice.click()
        # create privacy notice
        ucm.create_privacy_notice(legal_entity_name, privacy_notice_name)
        expect(ucm.get_privacy_notice_save_confi_msg()).to_be_visible(timeout=15000)





        page.wait_for_timeout(5000)

    else:
        # Invalid login validation
        expect(login_page.txt_error_message).to_be_visible(timeout=5000)

