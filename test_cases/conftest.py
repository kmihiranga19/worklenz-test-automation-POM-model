import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    browser = webdriver.Firefox()
    browser.maximize_window()
    return browser
