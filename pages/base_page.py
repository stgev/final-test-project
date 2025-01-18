from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, browser: WebDriver, url: str, timeout: int = 10):
        self.browser, self.url = browser, url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, by: str, value: str) -> bool:
        try:
            self.browser.find_element(by, value)
        except NoSuchElementException:
            return False
        return True

    def open(self) -> None:
        self.browser.get(self.url)
