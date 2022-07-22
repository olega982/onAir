from framework.web_elements.browser_web_element import BrowserWebElement
from selenium.webdriver.common.by import By


class SubcategoryItems:
    go_to_cart = BrowserWebElement(By.XPATH, "(//button[contains(text(),'Go to Cart')])[1]")

    @classmethod
    def click_go_to_cart(self):
        self.go_to_cart.click()


on_subcategory_items_page = SubcategoryItems()
