from selenium.webdriver.common.by import By
from framework.web_elements.browser_web_element import BrowserWebElement


class ProductPage:

    element_description = BrowserWebElement(By.CSS_SELECTOR, ".item-cell .item-title")
    add_product_button = BrowserWebElement(By.CSS_SELECTOR, ".product-buy-box  .btn-primary")
    product_price = BrowserWebElement(By.CSS_SELECTOR, ".product-pane .price-current strong")


on_product_page = ProductPage()