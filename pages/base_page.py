import math

from selenium.common import NoSuchElementException, NoAlertPresentException
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

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
