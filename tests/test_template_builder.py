
from pages.login_page import LoginPage
from pages.template_builder_page import templateBuilderPage
from config import Config


def test_open_template_builder(page):

    # login
    login_page = LoginPage(page)

    login_page.login(Config.dpo_email, Config.dpo_password)

    # template builder
    template_builder = templateBuilderPage(page)

    template_builder.open_template_builder()

    template_builder.basic_details_step()

    template_builder.create_question_step()

    template_builder.create_parent_question()

    # parent type
    button_name = template_builder.select_question_type(0)

    template_builder.fill_parent_options(
        button_name
    )

    # child question
    template_builder.child_question()

    # child type
    button_name = template_builder.select_question_type(1)

    template_builder.fill_child_options(
        button_name
    )

    # save template
    template_builder.save_submit_template()