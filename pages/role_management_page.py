from playwright.sync_api import Page, expect
from config import Config

 
class RoleManagementPage:
 
    def __init__(self, page: Page):
 
        self.page = page
#locate to role management page
        # Sidebar Menus
        self.access_management_menu = page.locator( "span:text-is('Access Management')")
 
        self.role_management_menu = page.locator( "span:text-is('Role Management')")
 
        # Page Title
        self.role_management_title = page.locator("text='Role Management'").nth(1)
        
#create a role
        #  add role
        self.add_role_btn =page.get_by_role("button", name="Add Role")
 
         # Role Name Input
        self.role_name_input = page.locator("input[placeholder='Enter role name']")
 
        # Module Head Dropdown
        self.module_head_dropdown = page.locator( "span:text-is('select')"
        )
        # Current dropdown value
        self.current_option = page.locator("div.min-w-0.flex-1.truncate.text-left span").nth(0)
 
        # Yes Option
        self.yes_option = page.locator( "span:text-is('Yes')")
        # No Option
        self.no_option = page.locator( "span:text-is('No')")
        
        # All Checkboxes
        self.checkboxes = page.locator("[role='checkbox']")
 
        #save button
        self.save_button = page.get_by_role('button', name='Save')
        
        # message success
        self.success_message = page.locator("text='Role added successfully'")
        
#view the role management page
        #see view button
        self.view_eye_button = page.get_by_alt_text( "eye icon").nth(0)
        #cancel view
        self.cancel_view = page.get_by_text('Cancel')
        
#edit the role management page
        #edit button
        self.edit_button = page.get_by_alt_text('Table Action Icon').nth(0)
         
         #submit all edit
        self.submit_button = page.get_by_text('Submit')       
        
# add a user to role management
        
        self.add_user_button = page.locator("button:has(svg.lucide-user-plus)").nth(0)
        
        #assign user
        self.assign_user_button = page.get_by_text("Assign User", exact=True)
        self.checkboxes = page.locator("button[role='checkbox']")
        self.update_user = page.get_by_text('Update' , exact=True)
        
        
        
        
    def open_role_management(self):
        try:
            # Click Access Management
            self.access_management_menu.click()
    
            # Wait for submenu
            expect(self.role_management_menu).to_be_visible(timeout=50000)
    
            # Click Role Management
            self.role_management_menu.click()
            self.role_management_menu.click()
        except Exception as e:
            print(f"Error in open_role_management: {e}")
            raise
            
 
    def create_role(self, role_name):
        try:
            #click on add role button
            self.add_role_btn.click()        
    
            # Fill Role Name
            self.role_name_input.fill(role_name)
    
            # Open Dropdown
            self.module_head_dropdown.click()
    
            # Select No
            self.no_option.click()
    
        # Click All Checkboxes
            count = self.checkboxes.count()
    
            for i in range(count):
    
                checkbox = self.checkboxes.nth(i)
    
                checked = checkbox.get_attribute("aria-checked")
    
                if checked != "true":
    
                    checkbox.click()
                    
            #Click on save
            self.save_button.click()
            
            #success message
            expect(self.success_message)
        except Exception as e:
            print(f"Error in create_role: {e}")
            raise
        
    def view_role(self):
        try:
            #click on view button
            self.view_eye_button.click()
            
            #click on cancel view
            self.cancel_view.click()
        except Exception as e:
            print(f"Error in view_role: {e}")
            raise
        
    def edit_role(self):
        try:
            # Click Edit Button
            self.edit_button.click()
    
            # Wait for popup/form
            self.page.wait_for_timeout(2000)
    
            # Read current Yes/No value
            current_value = self.current_option.text_content().strip()
    
    
            # Open Yes/No dropdown
            self.current_option.click()
    
            # Toggle dropdown value
            if current_value == "No":
    
                expect(self.yes_option).to_be_visible(timeout=10000)
    
                self.yes_option.click()
    
            elif current_value == "Yes":
    
                expect(self.no_option).to_be_visible(timeout=10000)
    
                self.no_option.click()
            # deslect the first checkbox
            first_checkbox = self.checkboxes.nth(1)
    
            first_checkbox.click()
                
            # Submit changes
            self.submit_button.click()
        except Exception as e:
            print(f"Error in edit_role: {e}")
            raise
    def add_user(self):
        try:
            #click on add user button
            self.add_user_button.click()
            
            
            #click on assign user button
            self.assign_user_button.click()
            
            # Click first 5 users
            for i in range(5):
    
                checkbox = self.checkboxes.nth(i)
    
                checked = checkbox.get_attribute("aria-checked")
    
                if checked != "true":
    
                    checkbox.click()    
            
            #click on update user button
            self.update_user.click()
            
        except Exception as e:
            print(f"Error in add_user: {e}")
            raise