from test_cases import test_login01
from test_cases.baseclass import BaseClass


class TestWishListPage(BaseClass):

    def test_01_user_can_add_product_in_wishlist(self):
        self.login.do_login(test_login01.username, test_login01.password)
        self.pro_page.search_book("Health book")
        self.wishl.wishlist_product_add()
        self.uihelp.assertion(self.wishl.text_show, True)


    def test_02_user_can_remove_the_product_from_wishlist(self):
        self.login.do_login(test_login01.username, test_login01.password)
        self.pro_page.search_book("Health book")
        self.wishl.remove_product_from_wishlist()
        self.uihelp.assertion(self.wishl.verify_remove_message, "Book Successfully Removed from Wishlist")
