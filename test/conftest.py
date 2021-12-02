import pytest
from selenium import webdriver

base_url = 'https://www.facebook.com'


@pytest.fixture(scope='session')
def driver():
    _driver = webdriver.Chrome()
    _driver.get(base_url)
    yield _driver
    print("Done with browser, quitting it")
    _driver.quit()