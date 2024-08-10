"""Module for locator storage"""

from selenium.webdriver.common.by import By


class AddContactLocators:
    """The class contains locators to add a contact"""
    # buttons
    add_contact_btn = (By.CSS_SELECTOR, "#add-contact")
    submit_btn = (By.CSS_SELECTOR, "#submit")
    cancel_btn = (By.CSS_SELECTOR, "#cancel")
    # forms
    first_name_input = (By.CSS_SELECTOR, "#firstName")
    last_name_input = (By.CSS_SELECTOR, "#lastName")
    birthdate_input = (By.CSS_SELECTOR, "#birthdate")
    email_input = (By.CSS_SELECTOR, "#email")
    phone_input = (By.CSS_SELECTOR, "#phone")
    street1_input = (By.CSS_SELECTOR, "#street1")
    street2_input = (By.CSS_SELECTOR, "#street2")
    city_input = (By.CSS_SELECTOR, "#city")
    state_input = (By.CSS_SELECTOR, "#stateProvince")
    postal_code_input = (By.CSS_SELECTOR, "#postalCode")
    country_input = (By.CSS_SELECTOR, "#country")
