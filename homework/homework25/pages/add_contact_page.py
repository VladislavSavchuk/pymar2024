"""This module contains the class for the add contact page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework.homework25.page_locators.add_contact_page import (
    AddContactLocators)


class AddContactPage:
    """ Class for the add contact page """
    def __init__(self, browser):
        self.browser = browser

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

    def click_add_contact(self):
        button_add_contact = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.add_contact_btn)))
        button_add_contact.click()

    def fill_contact_form(self, contact_data):
        wait = WebDriverWait(self.browser, 10)
        for field, value in contact_data.items():
            input_field = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, self.contact_form_fields[field])
            ))
            input_field.send_keys(value)

    def submit_form(self):
        submit_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.submit_btn))
        )
        submit_button.click()

    def click_cancel(self):
        cancel_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.cancel_btn))
        )
        cancel_button.click()
