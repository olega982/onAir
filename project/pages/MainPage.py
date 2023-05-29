from framework.web_elements.browser_web_element import BrowserWebElement
from selenium.webdriver.common.by import By

CSS = By.CSS_SELECTOR
XP = By.XPATH


class MainPage:
    """Logic and specific Settings"""
    search = BrowserWebElement(By.XPATH, '//input[@placeholder="Search"]')
    search_after_click = BrowserWebElement(By.XPATH, '(//input[@class="searchTriggerCategory"])[2]')
    cart_icon = BrowserWebElement(By.CSS_SELECTOR, ".userPanel_cart")
    cookie_warning = BrowserWebElement(By.CSS_SELECTOR, "#CybotCookiebotDialogBodyLevelButtonLevelOptinDeclineAll")

    """Web element functions with flexible numbers"""
    @classmethod
    def sub_category(self, x): return BrowserWebElement(CSS, f'.megaMenuList__item:nth-child({x})')

    @classmethod
    def category(self, x): return BrowserWebElement(CSS, f'.menu>li:nth-child({x})')

    @classmethod
    def category_item(self, x): return BrowserWebElement(XP, f'(//a[@class="simpleCardAppearance"])[{x}]')

    @classmethod
    def search_result_text(self, x): return BrowserWebElement(XP, f'(//div[@class="suggestionItem__category"])[{x}]')

    @classmethod
    def item_active(self, x): return BrowserWebElement(XP, f'(//div[@class="simpleCard verticalCard hoverActive"])[{x}]')

    """POM functions"""
    @classmethod
    def type_and_return_search_result(self, text, search_result):
        self.search.click()
        self.keys = self.search_after_click.send_keys(text)
        return self.search_result_text(search_result).get_text().lower()

    @classmethod
    def click_category(self, number):  self.category(number).click()

    @classmethod
    def click_sub_category(self, number): self.sub_category(number).click()

    @classmethod
    def hover_over_item(self, number): self.category_item(number).hover()

    @classmethod
    def click_active_item(self, number):  self.item_active(number).click()

    @classmethod
    def open_cart(self): self.cart_icon.click()

    @classmethod
    def close_warning(self): self.cookie_warning.click()


on_main_page = MainPage()
