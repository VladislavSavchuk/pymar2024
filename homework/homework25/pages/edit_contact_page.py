"""This module contains the class for the edit contact page"""

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework.homework25.page_locators.update_contact_page import (
    EditContactLocators)


class EditContactPage:
    """ Class for the edit contact page """
    def __init__(self, browser):
        self.browser = browser

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

    def click_contact_row(self):
        contact_row = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.contact_row))
        )
        contact_row.click()

    def click_edit_contact(self):
        button_edit = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.edit_contact_btn)))
        button_edit.click()
        time.sleep(1)

    def fill_edit_form(self, updated_data):
        wait = WebDriverWait(self.browser, 10)
        for field, value in updated_data.items():
            input_field = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.contact_form_fields[field])
            ))
            input_field.clear()
            input_field.send_keys(value)

    def submit_form(self):
        submit_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.submit_btn))
        )
        submit_button.click()
        time.sleep(1)

    def click_delete_contact(self):
        button_delete = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.delete_contact_btn)))
        button_delete.click()

    def click_return_to_contacts(self):
        button_return = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, self.return_to_contacts_btn)))
        button_return.click()

    def accept_alert(self):
        alert = WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert.accept()
