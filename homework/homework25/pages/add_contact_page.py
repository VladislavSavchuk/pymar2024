"""This module contains the class for the add contact page"""
import time

from selenium.webdriver.support import expected_conditions as EC
from homework.homework25.page_locators.add_contact_page import (
    AddContactLocators)
from homework.homework25.page_locators.update_contact_page import (
    EditContactLocators)
from homework.homework25.pages.base_page import BasePage


class AddContactPage(BasePage):
    """
    Class representing the add contact page of the application.
    Inherits from BasePage to provide common page functionalities.
    """
    add_contact_btn = AddContactLocators.add_contact_btn
    submit_btn = AddContactLocators.submit_btn
    cancel_btn = AddContactLocators.cancel_btn
    contact_form_fields = {
        'first_name': AddContactLocators.first_name_input,
        'last_name': AddContactLocators.last_name_input,
        'birthdate': AddContactLocators.birthdate_input,
        'email': AddContactLocators.email_input,
        'phone': AddContactLocators.phone_input,
        'street1': AddContactLocators.street1_input,
        'street2': AddContactLocators.street2_input,
        'city': AddContactLocators.city_input,
        'state': AddContactLocators.state_input,
        'postal_code': AddContactLocators.postal_code_input,
        'country': AddContactLocators.country_input,
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
        self.click_element(AddContactLocators.add_contact_btn)

        for field, value in contact_data.items():
            locator = getattr(AddContactLocators, f'{field}_input')
            self.enter_text(locator, value)

        self.click_element(AddContactLocators.submit_btn)

        self.wait.until(EC.presence_of_element_located(
            EditContactLocators.contact_row))
