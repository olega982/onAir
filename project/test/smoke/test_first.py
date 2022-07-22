import pytest
from project.pages.ItemPage import on_item_page
from project.pages.LoginPage import on_login_page
from project.pages.MainPage import on_main_page
from project.pages.SideMenuCart import on_side_menu_cart
from project.pages.SubcategoryItems import on_subcategory_items_page

SEARCH_TEXT = 'tea'
SINGLE_PRODUCT = 1
MULTIPLE_PRODUCTS = 5
FIRST = 1
SECOND = 2


class TestSuiteFirst:
    @pytest.mark.skip
    def test_user_check_search_results(self, set_browser_type_and_env, create_driver, close_cookies):
        assert SEARCH_TEXT in on_main_page.type_and_return_search_result(SEARCH_TEXT, FIRST)

    @pytest.mark.skip
    @pytest.mark.parametrize("number_of_items", (SINGLE_PRODUCT, MULTIPLE_PRODUCTS))
    def test_user_add_single_and_multiple_product_to_bucket(self, set_browser_type_and_env, create_driver,
                                                            close_cookies,
                                                            number_of_items):
        on_main_page.click_category(SECOND)
        on_main_page.click_sub_category(FIRST)
        on_main_page.hover_over_item(SECOND)
        on_main_page.click_add_to_cart(SECOND)
        on_item_page.change_item_entity_to(number_of_items)
        item_name = on_item_page.grab_item_name()
        item_price = on_item_page.grab_item_price()
        on_item_page.click_add_item_to_card()
        on_subcategory_items_page.click_go_to_cart()
        assert item_name == on_side_menu_cart.get_product_name()
        assert item_price == on_side_menu_cart.get_product_price()
        on_side_menu_cart.delete_first_item()
        on_side_menu_cart.verify_cart_is_empty()

    # @pytest.mark.skip
    def test_logged_in_user_add_product_leave_and_come_back(self, set_browser_type_and_env, create_driver,
                                                            close_cookies):
        on_login_page.login()
        on_main_page.click_category(SECOND)
        on_main_page.click_sub_category(SECOND)
        on_main_page.hover_over_item(SECOND)
        on_main_page.click_add_to_cart(SECOND)
        on_item_page.change_item_entity_to(SINGLE_PRODUCT)
        item_name = on_item_page.grab_item_name()
        item_price = on_item_page.grab_item_price()
        on_item_page.click_add_item_to_card()
        on_subcategory_items_page.click_go_to_cart()
        assert item_name == on_side_menu_cart.get_product_name()
        assert item_price == on_side_menu_cart.get_product_price()
        on_side_menu_cart.close_cart()
        on_login_page.logout()
        on_login_page.login()
        on_main_page.open_cart()
        assert item_name == on_side_menu_cart.get_product_name()
        assert item_price == on_side_menu_cart.get_product_price()
        on_side_menu_cart.delete_first_item()
        assert on_side_menu_cart.verify_cart_is_empty() == True
