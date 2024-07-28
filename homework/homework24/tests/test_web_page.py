"""This module tests the creation, updating and deletion of a contact"""


import time
import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework.homework24.page_locators.login_page \
    import LoginPageLocators
from homework.homework24.page_locators.add_contact_page \
    import AddContactLocators
from homework.homework24.page_locators.update_contact_details_page \
    import EditContactLocators


URL = 'https://thinking-tester-contact-list.herokuapp.com/'
EMAIL = 'xesed@mailto.plus'
PASSWORD = 'qwerty1'


@pytest.fixture()
def open_browser():
    """
    Fixture function that opens a browser and navigates to a specified URL
    """
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(URL)
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def login(open_browser):
    """
    Logs in to the web page.

    Parameters:
        open_browser (selenium.webdriver.Chrome):
        The browser fixture to open the login page.
    """
    browser = open_browser
    wait = WebDriverWait(browser, 10)

    email_field = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, LoginPageLocators.input_email)))
    email_field.send_keys(EMAIL)

    password_field = browser.find_element(
        By.CSS_SELECTOR, LoginPageLocators.input_password)
    password_field.send_keys(PASSWORD)

    button_submit = browser.find_element(
        By.CSS_SELECTOR, LoginPageLocators.submit_btn)
    button_submit.click()

    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[contains(text(), "Contact List")]')))


def test_add_contact(open_browser):
    """
    Adds a new contact to the contact list.

    Parameters:
        open_browser (selenium.webdriver.Chrome):
        The browser fixture to open the login page.
    """
    browser = open_browser
    wait = WebDriverWait(browser, 10)

    button_add_contact = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, AddContactLocators.add_contact_btn)))
    button_add_contact.click()

    # Prepare data for a new contact
    contact_data = {
        AddContactLocators.first_name_input: 'Gottfried',
        AddContactLocators.last_name_input: 'Leibniz',
        AddContactLocators.birthdate_input: '1999-01-01',
        AddContactLocators.email_input: 'test@beispiel.de',
        AddContactLocators.phone_input: '030303986300',
        AddContactLocators.street1_input: '123 Main St',
        AddContactLocators.street2_input: 'Wolfhound 1',
        AddContactLocators.city_input: 'Henchmen',
        AddContactLocators.state_input: 'MG',
        AddContactLocators.postal_code_input: '80636',
        AddContactLocators.country_input: 'Germany',
    }

    # Fill in the form fields and wait until each field is available
    for locator, value in contact_data.items():
        input_field = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, locator)))
        input_field.send_keys(value)

    submit_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, AddContactLocators.submit_btn)))
    submit_button.click()

    contact_row = wait.until(EC.presence_of_element_located(
        (By.XPATH, EditContactLocators.contact_row)))

    # Verify that the contact was added
    assert contact_row is not None


def test_edit_contact(open_browser):
    """
    Edits details of a contact on a web page.

    Parameters:
        open_browser (selenium.webdriver.Chrome):
        The browser fixture to open the login page.
    """
    browser = open_browser
    wait = WebDriverWait(browser, 10)

    contact_row = wait.until(EC.element_to_be_clickable(
        (By.XPATH, EditContactLocators.contact_row)))
    contact_row.click()

    button_edit = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, EditContactLocators.edit_contact_btn)))
    button_edit.click()
    time.sleep(1)

    # Prepare updated data for a contact
    updated_data = {
        EditContactLocators.email_form: 'newtestmail@beispiel.de',
        EditContactLocators.city_form: 'Dortmund',
        EditContactLocators.postal_code_form: '44123',
    }

    # Fill in the form fields and wait until each field is available
    for locator, value in updated_data.items():
        input_field = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, locator)))
        input_field.clear()
        input_field.send_keys(value)

    submit_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, EditContactLocators.submit_btn)))
    submit_button.click()
    time.sleep(1)

    # Verify that the contact was edited
    email = browser.find_element(
        By.CSS_SELECTOR, '[id="email"]').text
    city = browser.find_element(
        By.CSS_SELECTOR, '[id="city"]').text
    postal_code = browser.find_element(
        By.CSS_SELECTOR, '[id="postalCode"]').text
    assert email == 'newtestmail@beispiel.de'
    assert city == 'Dortmund'
    assert postal_code == '44123'


def test_delete_contact(open_browser):
    """
    Deletes a contact on a web page.

    Parameters:
        open_browser (selenium.webdriver.Chrome):
        The browser fixture to open the login page.
    """
    browser = open_browser
    wait = WebDriverWait(browser, 10)

    contact_row = wait.until(EC.presence_of_element_located(
        (By.XPATH, EditContactLocators.contact_row)))
    # Save the name of the contact before deleting it
    contact_name = contact_row.text
    contact_row.click()

    button_delete = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, EditContactLocators.delete_contact_btn)))
    button_delete.click()

    alert = wait.until(EC.alert_is_present())
    alert.accept()

    contact_deleted = True
    try:
        wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//*[contains(text(), '{contact_name}')]")))
        contact_deleted = False
    except TimeoutException:
        pass

    # Verify that the contact was deleted
    assert contact_deleted, \
        f"Contact '{contact_name}' was not deleted successfully."
