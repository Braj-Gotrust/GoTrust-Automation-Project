from faker import Faker
import random
import string


class RandomDataUtil:
    def __init__(self):
        self.faker = Faker()

    def get_first_name(self) -> str:
        return self.faker.first_name()

    def get_last_name(self) -> str:
        return self.faker.last_name()

    def get_full_name(self) -> str:
        return self.faker.name()

    def get_email(self) -> str:
        return self.faker.email()

    def get_phone_number(self) -> str:
        return self.faker.phone_number()

    def get_username(self) -> str:
        return self.faker.user_name()

    def get_password(self, length: int = 10) -> str:
        return self.faker.password(length=length)

    def get_random_country(self) -> str:
        return self.faker.country()

    def get_random_state(self) -> str:
        return self.faker.state()

    def get_random_city(self) -> str:
        return self.faker.city()

    def get_random_pin(self) -> str:
        return self.faker.postcode()

    def get_random_address(self) -> str:
        return self.faker.street_address()

    def get_random_alphanumeric(self, length: int) -> str:
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def get_random_numeric(self, length: int) -> str:
        return ''.join(random.choice(string.digits) for _ in range(length))

    def get_random_uuid(self) -> str:
        return str(self.faker.uuid4())



    # Legal Entity Name
    def get_legal_entity_name(self) -> str:
        return f"LegalEntity_{self.faker.company()}_{random.randint(100, 999)}"

    # Description
    def get_description(self) -> str:
        return f"{self.faker.catch_phrase()} - {self.faker.sentence(nb_words=10)}"

    # Business Unit Name
    def get_business_unit_name(self) -> str:
        return f"BusinessUnit_{self.faker.bs().split()[0].capitalize()}_{random.randint(100, 999)}"

    # Department Name
    def get_department_name(self) -> str:
        departments = [
            "HR", "Finance", "IT", "Marketing",
            "Sales", "Operations", "Compliance"
        ]
        return f"Department_{random.choice(departments)}_{random.randint(100, 999)}"

    # Product Name
    def get_product_name(self) -> str:
        return f"Product_{self.faker.word().capitalize()}_{random.randint(1000, 9999)}"

    # Service Name
    def get_service_name(self) -> str:
        return f"Service_{self.faker.catch_phrase().replace(' ', '_')}_{random.randint(100, 999)}"

    # Business Process Name
    def get_business_process_name(self) -> str:
        processes = [
            "Employee_Onboarding",
            "Invoice_Processing",
            "Risk_Assessment",
            "Customer_Support",
            "Vendor_Management",
            "Data_Collection"
        ]
        return f"Process_{random.choice(processes)}_{random.randint(100, 999)}"
