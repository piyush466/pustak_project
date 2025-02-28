import pytest

from test_cases.baseclass import BaseClass
from uihelper.helper_file import UI_Helper


class Test_Product_Page(BaseClass):

    def test_01_user_can_search_product(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        self.pro_page.search_book("Health book")
        self.uihelp.assertion(self.uihelp.get_text(self.pro_page.VALIDATE_WITH_THE_BOOK_CSS), "Only InStock Books")

    # def test_02_user_can_add_product_into_cart(self):
    #     self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
    #     self.pro_page.add_product_into_cart()
    #     # self.uihelp.assertion(self.pro_page.title_case, "The World Book Health And Medical Annual 1993")

    @pytest.mark.run(order=1)
    def test_02_user_can_add_product_in_cart(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        self.pro_page.search_book("Health book")
        self.pro_page.multiple_product_add_cart()
        self.uihelp.assertion(self.uihelp.get_text(self.pro_page.VERIFY_TEXT_OF_CART_CSS), "My Cart (3)")

    @pytest.mark.run(order=2)
    def test_03_user_can_remove_the_code_from_cart(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        self.pro_page.search_book("Health book")
        self.pro_page.remove_all_products()
        print(self.uihelp.get_text(self.pro_page.VERIFY_TEXT_OF_CART_CSS))
        self.uihelp.assertion(self.uihelp.get_text(self.pro_page.VERIFY_TEXT_OF_CART_CSS), "My Cart (0)")

    #Verify category filter
    def test_04_user_can_add_the_filter(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        self.pro_page.search_book("Health book")
        self.pro_page.add_filter()
        self.uihelp.assertion(self.pro_page.author, f'By {"Dr V K Sharma"}')

    #verify the sublinks
    def test_05__check_sublinks_are_working_or_not(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        self.pro_page.sub_links()
        self.uihelp.assertion(self.pro_page.capture_list, self.pro_page.after_click_on_link)













