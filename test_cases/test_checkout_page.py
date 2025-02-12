import pytest
from pytest_dependency import depends

from test_cases.baseclass import BaseClass
from uihelper.helper_file import UI_Helper


class Test_Checkout_page(BaseClass):


    def test_01_user_can_do_the_checkout(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        self.pro_page.search_book("Health book")
        self.pro_page.multiple_product_add_cart()
        self.checkout.goto_checkout()
        assert  "Order placed" in self.checkout.confirm_text





