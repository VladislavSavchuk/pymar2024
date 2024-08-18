"""This module contains the class for the login page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from homework.homework25.pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Class representing the login page of the application.
    Inherits from BasePage to provide common page functionalities.
    """
    def __init__(self, driver):
        """
        Initializes the LoginPage with the provided WebDriver instance
        and sets up the locators for the login page elements.
        """
        super().__init__(driver)
        self.input_email = (By.CSS_SELECTOR, "#email")
        self.input_password = (By.CSS_SELECTOR, "#password")
        self.submit_btn = (By.CSS_SELECTOR, "#submit")
        self.contact_header = (By.XPATH, '//*[contains(text(), "Contact List")]')

    def complete_login(self, email, password):
        """
        Completes the login process by entering the provided email
        and password, and submitting the login form.

        Parameters:
            email (str): The email address to use for login.
            password (str): The password associated with the email address.

        Raises:
            TimeoutException: If the login process does not complete
            within the timeout period.
        """
        self.enter_text(self.input_email, email)
        self.enter_text(self.input_password, password)

        self.click_element(self.submit_btn)

        self.wait.until(EC.presence_of_element_located(self.contact_header))
