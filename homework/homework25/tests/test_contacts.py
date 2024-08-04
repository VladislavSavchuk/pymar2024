"""
This module contains the tests for the contacts web page
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
import logging
from homework.homework25.pages.login_page import LoginPage
from homework.homework25.pages.add_contact_page import AddContactPage
from homework.homework25.pages.edit_contact_page import EditContactPage
from homework.homework25.resources.constants import EMAIL, PASSWORD
from homework.homework25.conftest import driver

loger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def complete_login(driver):
    """
    Logs in to the web page.

    Parameters:
        open_browser (selenium.webdriver.Chrome):
        The browser fixture to open the login page.
        :param driver:
    """
    browser = driver
    login_page = LoginPage(browser)
    login_page.enter_email(EMAIL)
    login_page.enter_password(PASSWORD)
    login_page.submit_login()
    login_page.wait_for_login()


def test_add_contact(driver):
    """
    Adds a new contact to the contact list.

    Parameters:
        open_browser (selenium.webdriver.Chrome):
        The browser fixture to open the login page.
    """
    loger.info("Start test Add a new contact")
    browser = driver
    add_contact_page = AddContactPage(browser)
    add_contact_page.click_add_contact()

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
    add_contact_page.fill_contact_form(contact_data)
    add_contact_page.submit_form()

    contact_row = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, EditContactPage.contact_row))
    )

    assert contact_row is not None
    loger.info("Add a new contact - PASSED")


def test_edit_contact(driver):
    """
    Edits details of a contact on a web page.

    Parameters:
        open_browser (selenium.webdriver.Chrome):
        The browser fixture to open the login page.
    """
    loger.info("Start test Edit a contact")
    browser = driver
    edit_contact_page = EditContactPage(browser)
    edit_contact_page.click_contact_row()
    edit_contact_page.click_edit_contact()

    updated_data = {
        'email': 'newtestmail@beispiel.de',
        'city': 'Dortmund',
        'postal_code': '44123',
    }
    edit_contact_page.fill_edit_form(updated_data)
    edit_contact_page.submit_form()

    email = (browser.find_element
             (By.CSS_SELECTOR, '[id="email"]').text)
    city = (browser.find_element
            (By.CSS_SELECTOR, '[id="city"]').text)
    postal_code = (browser.find_element
                   (By.CSS_SELECTOR, '[id="postalCode"]').text)
    assert email == 'newtestmail@beispiel.de'
    assert city == 'Dortmund'
    assert postal_code == '44123'

    loger.info("Edit a contact - PASSED")


def test_delete_contact(driver):
    """
    Deletes a contact on a web page.

    Parameters:
        open_browser (selenium.webdriver.Chrome):
        The browser fixture to open the login page.
    """
    loger.info("Start test Delete a contact")
    browser = driver
    edit_contact_page = EditContactPage(browser)

    contact_row = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, EditContactPage.contact_row))
    )
    contact_name = contact_row.text

    edit_contact_page.click_contact_row()
    edit_contact_page.click_delete_contact()
    edit_contact_page.accept_alert()

    contact_deleted = True
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//*[contains(text(), '{contact_name}')]"))
        )
        contact_deleted = False
        loger.error("Contact '%s' was not deleted successfully.",
                    contact_name)
    except TimeoutException:
        pass

    assert contact_deleted, \
        f"Contact '{contact_name}' was not deleted successfully."

    loger.info("Delete a contact - PASSED")
