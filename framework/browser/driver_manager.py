from framework.browser.browser_factory import DriverFactory


class DriverManager:
    __driver = None

    @staticmethod
    def get_driver():
        if DriverManager.__driver is None:
            DriverManager.__driver = DriverFactory.crete_driver()
        return DriverManager.__driver

    @staticmethod
    def quit():
        if DriverManager.__driver is not None:
            DriverManager.__driver.quit()
            DriverManager.__driver = None
