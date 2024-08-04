
import pytest
from selenium import webdriver
from homework.homework25.resources.constants import URL


class Basepage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self, url):
        self.driver.get(url)

    def find_element(self, selector):
        return self.driver.find_element(*selector)

    def find_elements(self, selector):
        return self.driver.find_elements(*selector)
