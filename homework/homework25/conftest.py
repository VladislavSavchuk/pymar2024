"""This module contains the fixtures for the tests"""

import pytest
from selenium import webdriver
from homework.homework25.resources.constants import URL


@pytest.fixture()
def driver():
    """
    Fixture that provides a WebDriver instance for the tests.

    This fixture initializes the Chrome WebDriver with specified options,
    sets an implicit wait time, and navigates to the predefined URL.
    It ensures that the browser is opened before the test and properly
    closed after the test.

    Returns:
        selenium.webdriver.Chrome: The WebDriver instance used
        for browser interactions.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.get(URL)
    yield browser
    browser.quit()
