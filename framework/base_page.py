from selenium.webdriver.common.by import By
from framework.web_elements.browser_web_element import BrowserWebElement


class BasePage:
    successful_login_modal = BrowserWebElement(By.CSS_SELECTOR, ".Toastify__toast-body")
    country_flag = BrowserWebElement(By.CSS_SELECTOR, ".LanguageTrigger")
    apply_lang_button = BrowserWebElement(By.CSS_SELECTOR, ".lang_applyBtn")


    def choose_language(self, language):
        return BrowserWebElement(By.CSS_SELECTOR, f".countryPopup_countryContainer:nth-of-type({language})")

    def get_float_price(self, price, currency):
        return float(price.text.replace(f"{currency}", ""))

    def successful_login_modal_appear(self):
        return self.successful_login_modal.is_element_present()
