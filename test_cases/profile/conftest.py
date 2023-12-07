import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    browser = webdriver.Chrome()
    browser.maximize_window()
    return browser
