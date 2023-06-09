

from selenium.webdriver.common.by import By
from framework.web_elements.browser_web_element import BrowserWebElement

class CartPage:
    summary_price = BrowserWebElement(By.CSS_SELECTOR, ".summary-content-total strong")
    cart_product_title = BrowserWebElement(By.XPATH, "(//a[@class='item-title'])[1]")

on_cart_page = CartPage()