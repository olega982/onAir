from selenium.webdriver.common.by import By
from framework.web_elements.browser_web_element import BrowserWebElement


class MainPage:
    search_bar = BrowserWebElement(By.CSS_SELECTOR, ".header2021-search-inner [type='search']")
    search_icon = BrowserWebElement(By.CSS_SELECTOR, ".ico-search")
    items_description = BrowserWebElement(By.CSS_SELECTOR, ".item-cell .item-title")
    first_item_price = BrowserWebElement(By.CSS_SELECTOR, ".item-cell .price-current")
    cookies_accept_all = BrowserWebElement(By.CSS_SELECTOR, ".osano-cm-accept-all")
    modal_banner_close = BrowserWebElement(By.CSS_SELECTOR, "[data-dismiss='modal']")

    def type_into_searchbar(self,search_item):
        self.search_bar.send_keys(search_item)
    def first_search_item_title(self):
        return self.items_description.find_elements()[0]
    def first_search_item_title_text(self):
        return self.first_search_item_title().text.lower()

on_main_page = MainPage()