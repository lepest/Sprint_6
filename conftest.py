import pytest

from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    web_driver = webdriver.Firefox()
    yield web_driver
    web_driver.quit()

