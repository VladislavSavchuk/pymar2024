"""This module contains the class for the login page"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework.homework25.page_locators.logining_page \
    import LoginPageLocators


class LoginPage:
    """ Class for the login page """
    def __init__(self, browser):
        self.browser = browser

    input_email = LoginPageLocators.input_email
    input_password = LoginPageLocators.input_password
    submit_btn = LoginPageLocators.submit_btn

    def enter_email(self, email):
        email_field = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, self.input_email))
        )
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = (self.browser.find_element
                          (By.CSS_SELECTOR, self.input_password))
        password_field.send_keys(password)

    def submit_login(self):
        button_submit = (self.browser.find_element
                         (By.CSS_SELECTOR, self.submit_btn))
        button_submit.click()

    def wait_for_login(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[contains(text(), "Contact List")]'))
        )
