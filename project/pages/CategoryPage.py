from framework.base_page import BasePage
from framework.web_elements.browser_web_element import BrowserWebElement
from selenium.webdriver.common.by import By


class CategoryPage(BasePage):
    filter_Low_High = BrowserWebElement(By.XPATH, "(//span[@class='sortItem__title'])[2]")
    filter_High_Low = BrowserWebElement(By.XPATH, "(//span[@class='sortItem__title'])[3]")
    out_of_stock_item = BrowserWebElement(By.XPATH, "//div[@class='simpleCard verticalCard']")

    def item_prices(self, x):
        return BrowserWebElement(By.XPATH, f"(//div[@class='dbda8320'])[{x}]/span")

    def get_item_price(self, item_number):
        prices = self.item_prices(item_number).find_elements()
        if len(prices) > 1:
            return self.get_float_price(self.item_prices(item_number).find_elements()[1], "£")
        return self.get_float_price(self.item_prices(item_number).find_elements()[0], "£")


on_category_page = CategoryPage()
