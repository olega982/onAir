from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    __browser_type = None

    @staticmethod
    def set_type(browser_type):
        if DriverFactory.__browser_type is None:
            DriverFactory.__browser_type = browser_type
        return DriverFactory.__browser_type

    @staticmethod
    def get_type():
        return DriverFactory.__browser_type

    @staticmethod
    def clear_browser_type():
        if DriverFactory.__browser_type is not None:
            DriverFactory.__browser_type = None

    @staticmethod
    def crete_driver():
        driver = None
        if DriverFactory.get_type() == "chrome":
            print("\nStart browser Chrome for smoke..")
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
        elif DriverFactory.get_type() == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return driver
