# content of conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language")


@pytest.fixture(scope="module")
def browser(request):
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
