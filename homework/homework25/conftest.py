
import pytest
from selenium import webdriver
from homework.homework25.resources.constants import URL


@pytest.fixture()
def driver():
    """
    Fixture function that opens a browser and navigates to a specified URL
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.get(URL)
    yield browser
    browser.quit()
