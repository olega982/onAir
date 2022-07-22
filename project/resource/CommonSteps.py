import pytest
from framework.browser.browser_factory import DriverFactory
from framework.browser.driver_factory import DriverManager

# pytest -v -s --browser_name=chrome smoke.py
# pytest -v -s --language=en smoke.py
from framework.browser.env_factory import EnvManager
from project.pages.MainPage import on_main_page

CREDENTIALS = 'login, password'
FIRST_USER_CREDENTIALS = ('gokey36920@aikusy.com', 'Newpassw0rd')
SECOND_USER_CREDENTIALS = ('mehar43380@abincol.com', 'Newpassw0rd')


class CommonSteps:
    @staticmethod
    def destroy_driver():
        print("\ndestroy browser..\nclear env..")
        DriverFactory.clear_browser_type()
        EnvManager.clear_env_type()
        DriverManager.quit()


    @staticmethod
    def create_driver():
        EnvManager.set_type("qa")
        DriverFactory.set_type("chrome")
        driver = DriverManager.get_driver()
        driver.get(EnvManager.get_type())


    @staticmethod
    def close_cookies():
        if on_main_page.cookie_warning.is_element_present():
            on_main_page.close_warning()
