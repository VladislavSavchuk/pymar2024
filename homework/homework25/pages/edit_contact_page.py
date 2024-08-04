"""This module contains the class for the edit contact page"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from homework.homework25.page_locators.update_contact_page import (
    EditContactLocators)
from homework.homework25.pages.base_page import BasePage


class EditContactPage(BasePage):
    """
    Class representing the edit contact page of the application.
    Inherits from BasePage to provide common page functionalities.
    """
    contact_row = EditContactLocators.contact_row
    edit_contact_btn = EditContactLocators.edit_contact_btn
    delete_contact_btn = EditContactLocators.delete_contact_btn
    submit_btn = EditContactLocators.submit_btn
    return_to_contacts_btn = EditContactLocators.return_to_contacts_btn
    contact_form_fields = {
        'email': EditContactLocators.email_form,
        'city': EditContactLocators.city_form,
        'postal_code': EditContactLocators.postal_code_form
    }

    def edit_contact(self, updated_data):
        """
        Edits the contact information by clicking on the contact row,
        navigating to the edit form, filling in the updated data,
        and submitting the changes.

        Parameters:
            updated_data (dict): A dictionary where keys correspond
            to contact form fields and values are the updated data.

        Raises:
            TimeoutException: If elements are not interactable or
            the contact is not updated within the timeout period.
        """
        self.click_element(
            (By.XPATH, EditContactLocators.contact_row))
        self.click_element(
            (By.CSS_SELECTOR, EditContactLocators.edit_contact_btn))
        time.sleep(1)

        for field, value in updated_data.items():
            locator = (By.CSS_SELECTOR,
                       getattr(EditContactLocators, f'{field}_form'))
            self.enter_text(locator, value)

        self.click_element(
            (By.CSS_SELECTOR, EditContactLocators.submit_btn))
        time.sleep(1)

    def verify_contact_updated(self, email, city, postal_code):
        """
        Verifies that the contact information has been updated correctly
         by checking the displayed details.

        Parameters:
            email (str): The expected email address of the updated contact.
            city (str): The expected city of the updated contact.
            postal_code (str): The expected postal code of
            the updated contact.

        Raises:
            AssertionError: If the displayed contact details
            do not match the expected values.
        """
        assert self.find_element(
            (By.CSS_SELECTOR, '[id="email"]')).text == email
        assert self.find_element(
            (By.CSS_SELECTOR, '[id="city"]')).text == city
        assert self.find_element(
            (By.CSS_SELECTOR, '[id="postalCode"]')).text == postal_code


class DeleteContactPage(BasePage):
    """
    Class representing the delete contact page of the application.
    Inherits from BasePage to provide common page functionalities.
    """
    def delete_contact(self):
        """
        Deletes a contact by clicking on the contact row,
        confirming the deletion in the alert, and returning
        the name of the deleted contact.

        Returns:
            str: The name of the contact that was deleted.

        Raises:
            TimeoutException: If the contact is not deleted
            within the timeout period.
        """
        contact_row = self.find_element(
            (By.XPATH, EditContactLocators.contact_row))
        contact_name = contact_row.text

        self.click_element(
            (By.XPATH, EditContactLocators.contact_row))

        self.click_element(
            (By.CSS_SELECTOR, EditContactLocators.delete_contact_btn))

        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

        return contact_name
