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


def pytest_addoption(parser):
    """Добавляет параметр --browser_name для выбора браузера"""
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser:chrome or firefox")
    parser.addoption('--env', action='store', default='qa',
                     help="Choose environment")


@pytest.fixture(scope="session")
def set_browser_type_and_env(request):
    browser_name = request.config.getoption("browser_name")
    environment = request.config.getoption("env")
    EnvManager.set_type(environment)
    DriverFactory.set_type(browser_name)
    yield
    print("\ndestroy browser..\nclear env..")
    DriverFactory.clear_browser_type()
    EnvManager.clear_env_type()


@pytest.fixture(scope="function")
def create_driver():
    driver = DriverManager.get_driver()
    driver.get(EnvManager.get_type())
    # open(EnvManager.get_type())
    yield
    print("\nquit browser..")
    DriverManager.quit()


@pytest.fixture(scope="function")
def close_cookies():
    if on_main_page.cookie_warning.is_element_present():
        on_main_page.close_warning()
