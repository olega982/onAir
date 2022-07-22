from framework.web_elements.browser_web_element import BrowserWebElement
from selenium.webdriver.common.by import By


class SideMenuCart:
    first_product_name = BrowserWebElement(By.CSS_SELECTOR, ".cartProductCategory")
    first_product_crossed_price = BrowserWebElement(By.CSS_SELECTOR, ".cartProductPrice span:nth-child(1)")
    first_product_real_price = BrowserWebElement(By.CSS_SELECTOR, ".cartProductPrice span:nth-child(2)")
    close_icon = BrowserWebElement(By.CSS_SELECTOR, ".cartClose")
    first_product_delete_icon = BrowserWebElement(By.CSS_SELECTOR, ".btnDelete")
    delete_item_confirm = BrowserWebElement(By.CSS_SELECTOR, ".blackTransparent")
    empty_cart_text = BrowserWebElement(By.CSS_SELECTOR, ".cartNoItems__text")

    @classmethod
    def get_product_name(self): return self.first_product_name.get_text()

    @classmethod
    def get_product_price(self):
        if self.first_product_real_price.is_element_present():
            return self.first_product_real_price.get_text()
        return self.first_product_crossed_price.get_text()

    @classmethod
    def close_cart(self): self.close_icon.click()

    @classmethod
    def delete_first_item(self):
        self.first_product_delete_icon.click()
        self.delete_item_confirm.click()

    @classmethod
    def verify_cart_is_empty(self): return self.empty_cart_text.is_element_present()


on_side_menu_cart = SideMenuCart()
