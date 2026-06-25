
from playwright.sync_api import Page, expect
from config import Config
import random

from conftest import page


class templateBuilderPage:

    def __init__(self, page: Page):

        self.page = page

        # TEMPLATE BUILDER 
        self.template_builder_menu = page.locator("span:text-is('Template Builder')")

        self.create_builder = page.get_by_text("Create Template")

        # BASIC DETAILS  

        self.select_options = page.locator("span:text-is('Select options')"  )

        self.checkboxes = page.locator("div.mr-2.flex.h-4.w-4.items-center.justify-center.rounded-sm")

        self.template_name = page.locator("input[placeholder='Enter unique Name']" )

        self.description_input = page.get_by_placeholder("Enter a brief description of the template" )
        
        self.template_category = self.page.locator("span:text-is('Select category')")
        
        self.select_dropdown = page.locator('[role="option"]').nth(0)

        self.create_template_button = page.get_by_role( "button", name="Create Template" )

        self.add_new_question = page.get_by_role( "button", name="Add New Question")

        # QUESTION STEP
        self.select_category = page.get_by_text("Select category")

        self.select_control = page.get_by_text("Select a control" )

        # PARENT QUESTION 

        self.question = page.locator("input[placeholder='Enter your question']" )

        self.question_description = page.get_by_placeholder("Provide additional context for this question")

        self.toggle_button = page.locator( "button[role='switch']" ).nth(0)

        # parent add option button
        self.parent_add_option_button = page.get_by_role("button", name="Add Option"  ).nth(0)

        # parent option inputs
        self.parent_option_inputs = page.locator( "input[placeholder='Option label']")

        # CHILD QUESTION #

        self.second_toggle = page.locator("button[role='switch']" ).nth(1)

        self.add_child_question_button = page.get_by_text( "Add Child Question")

        self.childquestion = page.locator("input[placeholder='Enter your child question']")

        self.childdescription = page.locator( "textarea[placeholder='Provide additional context for this quetion']")

        self.parent_answer_dropdown = page.locator("div:has-text('Select parent answer')").last

        # child add option button
        self.child_add_option_button = page.get_by_role( "button", name="Add Option" ).nth(1)

        # child option inputs
        self.child_option_inputs = page.locator("input[placeholder='Option']" )

          # SAVE BUTTON 

        self.add_question = page.get_by_role( "button",  name="Add Question" )

        self.save_template = page.get_by_role( "button", name="Save Template")

        # toggle button
        self.toggle_button = page.locator("button[role='switch']").nth(0)
        
        self.confirm_publish_button = page.get_by_role( "button", name="Confirm & Publish" )
        
    # =========================================================
    # OPEN TEMPLATE BUILDER
    # =========================================================

    def open_template_builder(self):
        try:

            self.template_builder_menu.click()
            self.template_builder_menu.click()

            self.create_builder.click()
        except Exception as e:
            print(f"Error in basic_details_step: {e}")
            raise

    # ======================= # BASIC DETAILS STEP# =========================

    def basic_details_step(self):

        self.select_options.click()

        # select first checkbox
        self.checkboxes.nth(0).click()

        self.template_name.fill(
            Config.template_name
        )

        self.description_input.fill(
            Config.template_description
        )

        self.template_category.click()
        self.select_dropdown.click()
        
        self.create_template_button.click()

        self.add_new_question.click()

    # ========================# RANDOM DROPDOWN # ==============================

    def select_random_dropdown_option(self, dropdown):
        try:
            dropdown.click(force=True)

            options = self.page.locator(
                "[role='option']"
            )

            options.first.wait_for(state="visible")

            count = options.count()

            random_index = random.randint(  0, count - 1 )

            options.nth(random_index).click(force=True)
            
        except Exception as e:
               print(f"Error in select_random_dropdown_option: {e}")
               raise

    # ==================== # CONTROL STEP# ===========================

    def create_question_step(self):
        try:
            self.select_random_dropdown_option(
                self.select_category
            )

            self.select_random_dropdown_option(
                self.select_control
            )
        except Exception as e:
            print(f"Error in create_question_step: {e}")
            raise

    # ========================= # PARENT QUESTION# ==========================
    def create_parent_question(self):
        try:
            self.question.fill(
                Config.parent_question
            )

            self.question_description.fill(
                Config.parent_description
            )

            self.toggle_button.click(force=True)
        except Exception as e:
            print(f"Error in create_parent_question: {e}")
            raise

    # ========================== # QUESTION TYPE # ===========================

    def select_question_type(self, index=0):

        try:
            question_types = [

                (
                    "Select",
                    self.page.get_by_role(
                        "button",
                        name="Select"
                    ).nth(index)
                ),

                (
                    "Multi Select",
                    self.page.get_by_role(
                        "button",
                        name="Multi Select"
                    ).nth(index)
                ),

                (
                    "Text Area",
                    self.page.get_by_role(
                        "button",
                        name="Text Area"
                    ).nth(index)
                )
            ]

            button_name, selected_type = random.choice(
                question_types
            )

            selected_type.click(force=True)

            return button_name

        except Exception as e:
            print(f"Error in select_question_type: {e}")
            raise
    # =========================== # PARENT OPTIONS # ===========================

    def fill_parent_options(self, button_name):
        try:
            if button_name != "Text Area":

                self.parent_add_option_button.click()
                self.parent_add_option_button.click()

                self.parent_option_inputs.nth(0).fill(
                    Config.option_label_1
                )

                self.parent_option_inputs.nth(1).fill(
                    Config.option_label_2
                )

            else:
                # Parent is Text Area, so no child question required

                self.add_question.click(force=True)

                success_message = self.page.get_by_text(
                    "Question created successfully"
                )
                expect(success_message).to_be_visible(timeout=15000)

                self.save_template.click(force=True)

                success_message = self.page.get_by_text(
                    "Template saved"
                )
                expect(success_message).to_be_visible(timeout=15000)

                # Publish template
                self.toggle_button.click(force=True)

                self.confirm_publish_button.click(force=True)
        except Exception as e:
            print(f"Error in fill_parent_options: {e}")
            raise
    # ======================== # CHILD QUESTION # =========================

    def child_question(self):
        try:
            self.second_toggle.click(force=True)

            self.add_child_question_button.click()

            self.childquestion.fill(
                Config.child_question_1
            )

            self.childdescription.fill(
                Config.child_description
            )

            # open dropdown
            self.parent_answer_dropdown.click(
                force=True
            )

            self.page.wait_for_timeout(1000)

            # dropdown options
            options = self.page.locator(
                "[data-radix-collection-item]"
            )

            expect(options.first).to_be_visible()

            count = options.count()

            random_index = random.randint(
                0,
                count - 1
            )

            options.nth(random_index).click(force=True)
        
        except Exception as e:
            print(f"Error in child_question: {e}")
            raise

    # =======================  # CHILD OPTIONS  # ===========================

    def fill_child_options(self, button_name):

        try:
           if button_name != "Text Area":

                self.child_add_option_button.click()

                self.child_add_option_button.click()

                self.child_option_inputs.nth(0).fill(
                    Config.child_option_label_1
                )

                self.child_option_inputs.nth(1).fill(
                    Config.child_option_label_2
                )
        except Exception as e:
            print(f"Error in fill_child_options: {e}")
            raise
    # =====================  # SAVE & publish TEMPLATE  # =======================
    def save_submit_template(self):
        try: 
            
            # click add question
            self.add_question.scroll_into_view_if_needed()

            self.add_question.click(force=True)

            # success message
            success_message = self.page.get_by_text(
                "Question created successfully"
            )

            expect(success_message).to_be_visible(
                timeout=15000
            )

            # click save template
            self.save_template.scroll_into_view_if_needed()

            self.save_template.click(force=True)

            self.toggle_button.click(force=True)
            self.confirm_publish_button.click(force=True)
        except Exception as e:
            print(f"Error in save_submit_template: {e}")
            raise