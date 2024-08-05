"""This module contains the class for the edit contact page"""

from selenium.webdriver.support import expected_conditions as EC
from homework.homework25.page_locators.update_contact_page import (
    EditContactLocators)
from homework.homework25.pages.base_page import BasePage


class EditContactPage(BasePage):
    """
    Class representing the edit contact page of the application.
    Inherits from BasePage to provide common page functionalities.
    """
    contact_deleted = EditContactLocators.contact_deleted
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
        self.click_element(EditContactLocators.contact_row)
        self.click_element(EditContactLocators.edit_contact_btn)

        # Wait until form is populated (JavaScript condition is true)
        self.wait.until(
            lambda driver: driver.execute_script(
                "return document.querySelector('#firstName').value !== '';")
        )

        for field, value in updated_data.items():
            locator = getattr(EditContactLocators, f'{field}_form')
            self.enter_text(locator, value)

        self.click_element(EditContactLocators.submit_btn)

        # Wait until form is populated (JavaScript condition is true)
        self.wait.until(
            lambda driver: driver.execute_script(
                "return document.querySelector('#firstName').innerHTML !== '';")
        )

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
            EditContactLocators.email_form).text == email
        assert self.find_element(
            EditContactLocators.city_form).text == city
        assert self.find_element(
            EditContactLocators.postal_code_form).text == postal_code


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
        contact_row = self.find_element(EditContactLocators.contact_row)
        contact_name = contact_row.text

        self.click_element(EditContactLocators.contact_row)

        self.click_element(EditContactLocators.delete_contact_btn)

        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

        return contact_name
