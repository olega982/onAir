from framework.browser.driver_factory import DriverManager


class BasePage:
    DRIVER_WAIT_TIME = 5
    DEFAULT_WAIT_TIME = 1

    def __init__(self):
        self.browser = DriverManager.get_driver()
        self.browser.implicitly_wait(BasePage.DRIVER_WAIT_TIME)

    # def open(self, url):
    #     self.browser.get(url)
