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




