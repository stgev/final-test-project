from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, browser: WebDriver, url: str):
        self.browser, self.url = browser, url

    def open(self) -> None:
        self.browser.get(self.url)
