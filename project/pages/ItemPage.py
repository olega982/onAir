from framework.web_elements.browser_web_element import BrowserWebElement
from selenium.webdriver.common.by import By


class ItemPage:
    item_name = BrowserWebElement(By.CSS_SELECTOR, ".b9dbeadb")
    item_add_to_cart_button = BrowserWebElement(By.XPATH, "(//button[contains(text(),'Add to Cart')])[1]")
    item_price_without_discount = BrowserWebElement(By.CSS_SELECTOR, "._2bb36aba span:nth-child(1)")
    item_price_with_discount = BrowserWebElement(By.CSS_SELECTOR, "._2bb36aba span:nth-child(2)")
    item_prices = BrowserWebElement(By.CSS_SELECTOR, "._2bb36aba span")
    item_entity_field = BrowserWebElement(By.CSS_SELECTOR, "[title='quantity input']")
    go_to_cart = BrowserWebElement(By.XPATH, "(//button[contains(text(),'Go to Cart')])[1]")

    @classmethod
    def click_go_to_cart(self):
        self.go_to_cart.click()

    @classmethod
    def get_item_name(self):
        return self.item_name.get_text()

    @classmethod
    def get_item_price(self):
        if len(self.item_prices.find_elements()) > 1:
            return self.item_prices.find_elements()[1].text
        return self.item_prices.find_elements()[0].text


    @classmethod
    def click_add_item_to_card(self):
        self.item_add_to_cart_button.click()

    @classmethod
    def change_item_entity_to(self, entity):
        self.item_entity_field.clear_field()
        self.item_entity_field.send_simply(entity)


on_item_page = ItemPage()
