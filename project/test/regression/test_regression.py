import pytest
from project.pages.ItemPage import on_item_page
from project.pages.LoginPage import on_login_page
from project.pages.MainPage import on_main_page
from project.pages.SideMenuCart import on_side_menu_cart
from project.pages.CategoryPage import on_category_page

SEARCH_TEXT = 'tea'
SINGLE_PRODUCT = 1
MULTIPLE_PRODUCTS = 5
FIRST = 1
SECOND = 2
RELEVANT = 1
COUNTRIES = [17, 5, 16]
LANG_PHRASE = ["Café", "Kaffee", "Kawa"]


class TestRegressionSuite:
    def user_login_into_account(self, set_browser_type_and_env, create_driver, close_cookies, filter_type):
        on_login_page.login()
        assert on_login_page.successful_login_modal_appear() == True

    def test_user_check_search_results(self, set_browser_type_and_env, create_driver, close_cookies):
        assert SEARCH_TEXT in on_main_page.type_and_return_search_result(SEARCH_TEXT, FIRST)

    @pytest.mark.parametrize("filter_type", ("Low-high", "High-low"))
    def test_user_sort_items(self, set_browser_type_and_env, create_driver, close_cookies, filter_type):
        on_main_page.click_category(SECOND)
        on_main_page.click_sub_category(FIRST)
        if filter_type == "Low-high":
            on_category_page.filter_Low_High.click()
            assert on_category_page.get_item_price(FIRST) <= on_category_page.get_item_price(SECOND)
        else:
            on_category_page.filter_High_Low.click()
            assert on_category_page.get_item_price(FIRST) >= on_category_page.get_item_price(SECOND)

    @pytest.mark.parametrize("number_of_items", (SINGLE_PRODUCT, MULTIPLE_PRODUCTS))
    def test_user_add_single_and_multiple_product_to_bucket(self, set_browser_type_and_env, create_driver,
                                                            close_cookies,
                                                            number_of_items):
        on_main_page.click_category(SECOND)
        on_main_page.click_sub_category(FIRST)
        on_main_page.click_active_item(SECOND)
        on_item_page.change_item_entity_to(number_of_items)
        item_name = on_item_page.get_item_name()
        item_price = on_item_page.get_item_price()
        on_item_page.click_add_item_to_card()
        on_item_page.click_go_to_cart()
        assert item_name == on_side_menu_cart.get_product_name()
        assert item_price == on_side_menu_cart.get_product_price()
        on_side_menu_cart.delete_first_item()
        assert on_side_menu_cart.verify_cart_is_empty() == True

    def test_logged_in_user_add_product_leave_and_come_back(self, set_browser_type_and_env, create_driver,
                                                            close_cookies):
        on_login_page.login()
        on_main_page.click_category(SECOND)
        on_main_page.click_sub_category(SECOND)
        on_main_page.click_active_item(SECOND)
        on_item_page.change_item_entity_to(SINGLE_PRODUCT)
        item_name = on_item_page.get_item_name()
        item_price = on_item_page.get_item_price()
        on_item_page.click_add_item_to_card()
        on_item_page.click_go_to_cart()
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

    def test_user_cant_add_out_of_stock_item(self, set_browser_type_and_env, create_driver, close_cookies):
        on_main_page.click_category(SECOND)
        on_main_page.click_sub_category(SECOND)
        on_category_page.out_of_stock_item.click()
        assert on_item_page.out_of_stock_label.is_element_present() == True
        assert on_item_page.out_of_stock_button.is_enabled() == False

    @pytest.mark.parametrize("country,language_phrase", zip(COUNTRIES, LANG_PHRASE))
    def test_user_can_switch_language(self, set_browser_type_and_env, create_driver, close_cookies, country,
                                      language_phrase):
        on_main_page.country_flag.click()
        on_main_page.choose_language(country).click()
        on_main_page.apply_lang_button.click()
        assert  on_main_page.category(SECOND).get_text() == language_phrase.upper()
