"""This module contains the class for the login page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from homework.homework25.page_locators.logining_page \
    import LoginPageLocators
from homework.homework25.pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Class representing the login page of the application.
    Inherits from BasePage to provide common page functionalities.
    """
    input_email = LoginPageLocators.input_email
    input_password = LoginPageLocators.input_password
    submit_btn = LoginPageLocators.submit_btn

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
        self.enter_text(
            (By.CSS_SELECTOR, LoginPageLocators.input_email), email)
        self.enter_text(
            (By.CSS_SELECTOR, LoginPageLocators.input_password), password)

        self.click_element(
            (By.CSS_SELECTOR, LoginPageLocators.submit_btn))

        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[contains(text(), "Contact List")]')))
