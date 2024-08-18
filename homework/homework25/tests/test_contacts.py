"""This module contains the tests for the contacts web page"""

import logging
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from homework.homework25.pages.login_page import LoginPage
from homework.homework25.pages.add_contact_page import AddContactPage
from homework.homework25.pages.edit_contact_page \
    import EditContactPage, DeleteContactPage
from homework.homework25.resources.constants import EMAIL, PASSWORD

loger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def login(driver):
    """
    Fixture that performs login before each test.

    Parameters:
        driver (selenium.webdriver.Chrome):
        The WebDriver instance used for browser interactions.

    This fixture initializes the LoginPage and performs a login operation
    using predefined EMAIL and PASSWORD constants.
    """
    login_page = LoginPage(driver)
    login_page.complete_login(EMAIL, PASSWORD)


@pytest.mark.contacts_page
def test_add_contact(driver):
    """
    Test for adding a new contact to the contact list.

    Parameters:
        driver (selenium.webdriver.Chrome):
        The WebDriver instance used for browser interactions.

    This test navigates to the add contact page,
    adds a new contact using predefined
    contact data, and verifies that the contact
    has been added successfully.
    """
    loger.info("Start test Add a new contact")

    add_contact_page = AddContactPage(driver)
    contact_data = {
        'first_name': 'Gottfried',
        'last_name': 'Leibniz',
        'birthdate': '1999-01-01',
        'email': 'test@beispiel.de',
        'phone': '030303986300',
        'street1': '123 Main St',
        'street2': 'Wolfhound 1',
        'city': 'Henchmen',
        'state': 'MG',
        'postal_code': '80636',
        'country': 'Germany',
    }

    add_contact_page.add_contact(contact_data)
    edit_contact_page = EditContactPage(driver)
    contact_row = driver.find_element(*edit_contact_page.contact_row)
    assert contact_row is not None

    loger.info("Add a new contact - PASSED")


@pytest.mark.contacts_page
def test_edit_contact(driver):
    """
    Test for editing an existing contact.

    Parameters:
        driver (selenium.webdriver.Chrome):
        The WebDriver instance used for browser interactions.

    This test navigates to the edit contact page,
    updates the contact information
    with predefined updated data, and verifies that the contact
    has been updated successfully.
    """
    loger.info("Start test Edit a contact")

    edit_contact_page = EditContactPage(driver)
    updated_data = {
        'email': 'newtestmail@beispiel.de',
        'city': 'Dortmund',
        'postal_code': '44123',
    }

    edit_contact_page.edit_contact(updated_data)
    edit_contact_page.verify_contact_updated(
        'newtestmail@beispiel.de', 'Dortmund', '44123')

    loger.info("Edit a contact - PASSED")


@pytest.mark.contacts_page
def test_delete_contact(driver):
    """
    Test for deleting an existing contact.

    Parameters:
        driver (selenium.webdriver.Chrome):
        The WebDriver instance used for browser interactions.

    This test navigates to the delete contact page,
    deletes an existing contact,
    and verifies that the contact has been removed from the contact list.
    """
    loger.info("Start test Delete a contact")

    delete_contact_page = DeleteContactPage(driver)
    contact_name = delete_contact_page.delete_contact()

    contact_deleted = True
    try:
        edit_contact_page = EditContactPage(driver)
        delete_contact_page.wait.until(
            EC.presence_of_element_located(edit_contact_page.contact_deleted))
        contact_deleted = False
    except TimeoutException:
        pass

    assert contact_deleted, \
        f"Contact '{contact_name}' was not deleted successfully."

    loger.info("Delete a contact - PASSED")
