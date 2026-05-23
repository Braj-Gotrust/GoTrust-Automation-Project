import re

from pages.login_page import LoginPage
from pages.ccm_page import CcmPage
from pages.ucm_page import UcmPage
from playwright.sync_api import expect
from config import Config



def test_ucm_1(page):
    # TEST DATA
    dpo_email = Config.dpo_email
    dpo_password = Config.dpo_password

    pii_label_name = Config.pii_label_name
    processing_category_name = Config.processing_category_name
    processing_activity_name_1 = Config.processing_activity_name_1
    processing_activity_name_2 = Config.processing_activity_name_2
    processing_purpose_name = Config.processing_purpose_name

    login_page = LoginPage(page)
    login_page.login(dpo_email, dpo_password)

    ucm = UcmPage(page)

    if True:

        # click on ucm lab
        ucm.click_ucm_lab_btn()

        # verify pii label inventory button
        expect(ucm.pii_label_inventory_txt).to_be_visible(timeout=15000)

        # click on pii label inventory button
        ucm.click_pii_label_inventory_btn()

        # verify ucm title
        expect(ucm.get_ucm_title()).to_be_visible(timeout=15000)

        # Pii Label tab
        ucm.fill_search_box(pii_label_name)
        expect(ucm.all_pii_label).to_be_visible(timeout=15000)
        ucm.select_pii_label_in_table(pii_label_name)
        ucm.click_save_btn()
        expect(ucm.get_pii_label_update_confi_msg()).to_be_visible(timeout=15000)


        # Processing Category tab
        ucm.processing_category_tab_action_1(processing_category_name)
        expect(ucm.get_add_processing_category_confi_msg()).to_be_visible(timeout=15000)
        ucm.processing_category_tab_action_2(processing_category_name,processing_activity_name_1)
        expect(ucm.get_add_processing_activity_confi_msg_1()).to_be_visible(timeout=15000)


        # Processing Activities Tab
        ucm.processing_activity_tab_action_1(processing_activity_name_2, processing_category_name)
        expect(ucm.get_add_processing_activity_confi_msg_2()).to_be_visible(timeout=15000)


        # Processing Purpose Tab
        ucm.processing_purpose_tab_action_1(processing_purpose_name, processing_activity_name_1)
        expect(ucm.get_add_processing_purpose_confi_msg()).to_be_visible(timeout=15000)






        page.wait_for_timeout(5000)

    else:
        # Invalid login validation
        expect(login_page.txt_error_message).to_be_visible(timeout=5000)

