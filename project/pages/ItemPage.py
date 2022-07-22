from framework.web_elements.browser_web_element import BrowserWebElement
from selenium.webdriver.common.by import By


class ItemPage:
    item_name = BrowserWebElement(By.CSS_SELECTOR, ".productPage__stickyForm>div:first-child>div:first-child")
    item_add_to_cart_button = BrowserWebElement(By.XPATH, "(//button[contains(text(),'Add to Cart')])[1]")
    item_price_without_discount = BrowserWebElement(By.XPATH, "(//form//span[contains(text(),'£')])[1]")
    item_price_with_discount = BrowserWebElement(By.XPATH, "(//form//span[contains(text(),'£')])[2]")
    item_entity_field = BrowserWebElement(By.CSS_SELECTOR, "[title='quantity input']")

    @classmethod
    def grab_item_name(self):
        return self.item_name.get_text()

    @classmethod
    def grab_item_price(self):
        if self.item_price_with_discount.is_element_present():
            return self.item_price_with_discount.get_text()
        return self.item_price_without_discount.get_text()

    @classmethod
    def click_add_item_to_card(self):
        self.item_add_to_cart_button.click()

    @classmethod
    def change_item_entity_to(self, entity):
        self.item_entity_field.clear_field()
        self.item_entity_field.send_simply(entity)


on_item_page = ItemPage()
