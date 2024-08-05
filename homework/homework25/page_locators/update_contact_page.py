""" Module for locator storage """

from selenium.webdriver.common.by import By


class EditContactLocators:
    """ The class contains locators to edit a contact """
    # contact row
    contact_row = (By.XPATH, '//*[@class="contactTable"]/tr[1]')
    contact_deleted = (By.XPATH, "//*[contains(text(), '{contact_name}')]")
    # buttons
    edit_contact_btn = (By.CSS_SELECTOR, "#edit-contact")
    delete_contact_btn = (By.CSS_SELECTOR, "#delete")
    return_to_contacts_btn = (By.CSS_SELECTOR, "#return")
    submit_btn = (By.CSS_SELECTOR, "#submit")
    cancel_btn = (By.CSS_SELECTOR, "#cancel")
    # forms
    first_name_form = (By.CSS_SELECTOR, "#firstName")
    last_name_form = (By.CSS_SELECTOR, "#lastName")
    birthdate_form = (By.CSS_SELECTOR, "#birthdate")
    email_form = (By.CSS_SELECTOR, "#email")
    phone_form = (By.CSS_SELECTOR, "#phone")
    street1_form = (By.CSS_SELECTOR, "#street1")
    street2_form = (By.CSS_SELECTOR, "#street2")
    city_form = (By.CSS_SELECTOR, "#city")
    state_form = (By.CSS_SELECTOR, "#stateProvince")
    postal_code_form = (By.CSS_SELECTOR, "#postalCode")
    country_form = (By.CSS_SELECTOR, "#country")
