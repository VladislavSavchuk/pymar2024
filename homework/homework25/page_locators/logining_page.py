"""Module for locator storage"""

from selenium.webdriver.common.by import By


class LoginPageLocators:
    """ The class contains locators to login page """
    # login form
    input_email = (By.CSS_SELECTOR, "#email")
    input_password = (By.CSS_SELECTOR, "#password")
    # buttons
    submit_btn = (By.CSS_SELECTOR, "#submit")
    # contact header
    contacts_header = (By.XPATH, '//*[contains(text(), "Contact List")]')
