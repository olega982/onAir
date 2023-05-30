from framework.base_page import BasePage
from framework.web_elements.browser_web_element import BrowserWebElement
from selenium.webdriver.common.by import By

USER_EMAIL = "qyyfu@mailto.plus"
USER_PASSWORD = "user69"


class LoginPage(BasePage):
    user_panel = BrowserWebElement(By.CSS_SELECTOR, ".userPanel_customer")
    logout_button = BrowserWebElement(By.XPATH, "//nav/p")
    email_field = BrowserWebElement(By.CSS_SELECTOR, "[placeholder='Email']")
    password_field = BrowserWebElement(By.CSS_SELECTOR, "[placeholder='Password']")
    login_modal_button = BrowserWebElement(By.CSS_SELECTOR, ".modalLoginForm__btn")
    head_banner = BrowserWebElement(By.CSS_SELECTOR, "#sliderPromo")

    @classmethod
    def login(self):
        print("Bodum Awesome test!!")
        self.user_panel.click()
        self.email_field.send_keys(USER_EMAIL)
        self.password_field.send_keys(USER_PASSWORD)
        self.login_modal_button.click()

    @classmethod
    def logout(self):
        self.user_panel.click()
        self.logout_button.click()
        self.head_banner.is_element_present()


on_login_page = LoginPage()
