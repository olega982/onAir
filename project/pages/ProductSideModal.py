from selenium.webdriver.common.by import By
from framework.web_elements.browser_web_element import BrowserWebElement


class ProductSideModal:
    dismiss_protection = BrowserWebElement(By.CSS_SELECTOR, "[data-dismiss='modal']")
    view_cart_modal_button = BrowserWebElement(By.CSS_SELECTOR, "[title='View Cart']")

on_product_side_modal = ProductSideModal()