import pytest

from project.pages.CartPage import on_cart_page
from project.pages.MainPage import on_main_page
from project.pages.ProductPage import on_product_page
from project.pages.ProductSideModal import on_product_side_modal

SEARCH_ITEM = "laptop"

class TestSmokeSuite:

    @pytest.mark.parametrize("search_item", ("laptop", "charger"))
    def test_user_check_search_results(self, set_browser_type_and_env, create_driver,close_cookies_and_adds,search_item):
        on_main_page.search_bar.type(search_item)
        on_main_page.search_icon.click()
        assert search_item in on_main_page.first_search_item_title_text()

    def test_user_add_item_to_cart(self, set_browser_type_and_env, create_driver, close_cookies_and_adds):
        on_main_page.search_bar.type(SEARCH_ITEM)
        on_main_page.search_icon.click()
        first_item_name = on_main_page.first_search_item_title_text()
        on_main_page.first_search_item_title().click()
        on_product_page.add_product_button.click()
        on_product_side_modal.dismiss_protection.click()
        on_product_side_modal.view_cart_modal_button.click()
        assert first_item_name == on_cart_page.cart_product_title.get_text().lower()






