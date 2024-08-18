"""This module contains the class for the add contact page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from homework.homework25.pages.base_page import BasePage


class AddContactPage(BasePage):
    """
    Class representing the add contact page of the application.
    Inherits from BasePage to provide common page functionalities.
    """

    def __init__(self, driver):
        """
        Initializes the AddContactPage with the provided WebDriver instance
        and sets up the locators for the Add Contact page elements.
        """
        super().__init__(driver)
        self.contact_row = (By.XPATH, '//*[@class="contactTable"]/tr[1]')
        self.add_contact_btn = (By.CSS_SELECTOR, "#add-contact")
        self.submit_btn = (By.CSS_SELECTOR, "#submit")
        self.cancel_btn = (By.CSS_SELECTOR, "#cancel")
        self.contact_form_fields = {
            'first_name': (By.CSS_SELECTOR, "#firstName"),
            'last_name': (By.CSS_SELECTOR, "#lastName"),
            'birthdate': (By.CSS_SELECTOR, "#birthdate"),
            'email': (By.CSS_SELECTOR, "#email"),
            'phone': (By.CSS_SELECTOR, "#phone"),
            'street1': (By.CSS_SELECTOR, "#street1"),
            'street2': (By.CSS_SELECTOR, "#street2"),
            'city': (By.CSS_SELECTOR, "#city"),
            'state': (By.CSS_SELECTOR, "#stateProvince"),
            'postal_code': (By.CSS_SELECTOR, "#postalCode"),
            'country': (By.CSS_SELECTOR, "#country"),
        }

    def add_contact(self, contact_data):
        """
        Adds a new contact to the contact list by filling in
        the contact form and submitting it.

        Parameters:
            contact_data (dict): A dictionary where keys correspond
            to contact form fields and values are the data to be entered.

        Raises:
            TimeoutException: If the contact is not added
            within the timeout period.
        """
        self.click_element(self.add_contact_btn)

        for field, value in contact_data.items():
            locator = self.contact_form_fields.get(field)
            if locator:
                self.enter_text(locator, value)
            else:
                raise ValueError(f"Locator for field '{field}' not found.")

        self.click_element(self.submit_btn)

        self.wait.until(EC.presence_of_element_located(self.contact_row))
