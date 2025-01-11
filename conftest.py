import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose the language")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    language = request.config.getoption("language")
    options.add_argument(f"lang={language}")
    browser = Chrome(options=options)
    yield browser
    browser.quit()
