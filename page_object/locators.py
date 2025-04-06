from selenium.webdriver.common.by import By


class Locators:

    #Login Page
    LOGIN_BTN_CSS = (By.CSS_SELECTOR, "button[class='undefined icon']")
    ENTER_USERNAME_CSS = (By.CSS_SELECTOR, "input.MuiInputBase-input")
    CLICK_ON_PROCEED_XPATH = (By.XPATH, "(//button[@type='submit'])[3]")
    ENTER_PASSWORD_XPATH = (By.XPATH, "//input[@type='password']")
    CLICK_LOGIN_BTN_CSS = (By.CSS_SELECTOR, "button.WLoginNavbar_loginButton__M7mhW")
    VERIFY_AFTER_LOGIN_XPATH = (By.XPATH, "//span[text()='Hi! Reader']")
    INVALID_MSG_AFTER_ENTER_WRONG_CREDS_CSS = (By.CSS_SELECTOR, "#notistack-snackbar")
    IF_USER_ENTER_WRONG_EMAIL_XPATH = (By.XPATH, "//p[text()='Enter valid email']")

    #My profile Page Locators
    CLICK_ON_HI_READER_ID = (By.ID, "loginBtn")
    CLICK_ON_MY_PROFILE_XPATH = (By.XPATH, "//*[text()=' My Profile']")
    NAVIGATE_PAGE_TEXT_CSS = (By.CSS_SELECTOR, "[class*='Myprofile_inputTitle']")
    ENTER_FNAME_BY_ID = (By.ID, "first_name")
    ENTER_LNAME_BY_ID = (By.ID, "last_name")
    CLICK_ON_UPDATE_XPATH = (By.XPATH, "//*[text()='Update']")
    VALIDATION_UPDATE_TEXT_XPATH = (By.XPATH, "//*[text()='Profile Updated Successfully']")
    # Manage Address page
    NAVIGATE_TO_MANAGE_ADDRESS_PAGE_XPATH = (By.XPATH, "//*[text()='Manage Address']")
    CLICK_ON_ADD_NEW_ADDRESS_XPATH = (By.XPATH, "(//*[text()=' Add New Address'])[1]")
    VERIFY_MANAGE_ADDRESS_PAGE_XPATH = (By.XPATH, "//b[text()='Manage Address']")
    # add new address
    CLICK_ADD_NEW_ADDRESS_XPATH = (By.XPATH, "(//*[text()=' Add New Address'])[1]")
    ENTER_NAME_BY_NAME = (By.NAME, "fullname")
    ENTER_PINCODE_BY_NAME = (By.NAME, "pincode")
    ENTER_ADDRESS_BY_NAME = (By.NAME, "address1")
    ENTER_LANDMARK_BY_NAME = (By.NAME, "landmark")
    ENTER_PHONE_NO_BY_NAME = (By.NAME, "phone_no")
    ENTER_WP_NO_BY_NAME = (By.NAME, "alt_phone_no")
    CLICK_ON_ADD_ADDRESS_XPATH = (By.XPATH, "//*[text()='Add Address']")
    VERIFY_ADDRESS_ADDEDE_SUCCESFUL_XPATH = (By.XPATH, "//*[text()='Address Added Successfully']")
    DELETE_BUTTON_XPATH = (By.XPATH, "(//*[text()=' Delete'])[1]")
    CLICK_ON_YES_XPATH = (By.XPATH, "//*[text()='Yes']")
    VERIFY_ADDRESS_DELETE_MESSAGE_XAPTH = (By.XPATH, "//*[text()='Address deleted succesfully']")
    EDIT_ADDRESS_BUTTON_XPATH = (By.XPATH, "//*[text()=' Edit']")
    SAVE_ADDRESS_BUTTON_XPATH = (By.XPATH, "//*[text()='Save Address']")
    VERIFY_EDITED_SUCCESS_MESSAGE_XPATH = (By.XPATH, "//*[text()='Address Edited Successfully']")

    #Checkout Page
    CLICK_ON_CHECKOUT_BUTTON_XPATH = (By.XPATH, "//button[text()='Proceed to Checkout ']")
    CLICK_ON_NO_XPATH = (By.XPATH, "(//button[@style='text-transform: capitalize;'])[2]")
    CLICK_ON_DELIVER_HERE_XPATH = (By.XPATH, "//span[text()='Deliver Here']")
    CLICK_ON_PROCEED_TO_PAYMENT_XPATH = (By.XPATH, "//span[text()='Proceed to payment options']")
    RADIO_BUTTON_CASH_DELIVERY_XPATH = (By.XPATH, "(//input[@id='flexRadioDefault2'])[2]")
    CLICK_CONFIRM_ORDER_XPATH = (By.XPATH, "//span[text()='Confirm Order']")
    ORDER_PLACE_MESSAGE_CLASS = (
    By.XPATH, "//b[@class='jsx-b3e1b6a7c9b96113 OrderThankYou_orderdiv__W9qvK d-flex align-items-center']")
    CLICK_ON_MY_ORDERS_XPATH = (By.XPATH, "(//*[text()='My Orders'])[1]")
    VERIFY_AFTER_LOGIN_XPATH = (By.XPATH, "//span[text()='Hi! Reader']")
    CLICK_ON_CANCEL_ORDER_XPATH = (By.XPATH, "(//*[text()='Cancel Order'])[1]")
    CLICK_ON_YES_ON_CANCEL_POP_UP_XPATH = (By.XPATH, "(//*[text()='Yes, cancel this order'])[1]")
    VERIFY_THE_TEXT_OF_CANCEL_XPATH = (By.XPATH, "(//*[text()='Order Cancelled Successfully.'])[1]")


    #Product_Page Locators
    SEARCH_PRODUCT_XPATH = (By.XPATH, "(//input[@id='gsearch'])[1]")
    CLICK_ON_SEARCH_BTN_XPATH = (By.XPATH, '(//button[@aria-label="searchButton"])[1]')
    VALIDATE_WITH_THE_BOOK_CSS = (By.CSS_SELECTOR, "[class='jsx-45b79a600e3d4efb clearButton']")
    CLICK_ON_BUY_NOW_XPATH = (By.XPATH, "(//*[text()='Buy Now'])[1]")
    CAPTURE_THE_BOOK_NAME = (By.CLASS_NAME, "CartPage_cartBookTitle__BCliw")
    # CLick on add to cart button
    CLICK_ON_ADD_TO_CART_BTN_XPATH = (
    By.XPATH, "//div[@class='jsx-313054587 md:h-[29.5rem] w-[100%] h-[30.5rem]  bg-white flex flex-col']/div[4]/button")
    CLICK_ON_CART_XPATH = (By.XPATH, "(//span[text()='Cart'])[1]")
    VERIFY_TEXT_OF_CART_CSS = (By.CSS_SELECTOR, "[class='px-3']")
    # click_n donate bookk
    CLICK_DONATE_BOOK_ID = (By.ID, "donateBookBtn")
    CLICK_OUR_PROUD_DONOR_ID = (By.ID, "proudDonerBtn")
    DONOR_TEXT_XPATH = (By.XPATH, "//*[text()='proud-donors']")

    #wishlist_page_locators
    ADD_PRODUCT_IN_WISHLIST_XPATH = (
    By.XPATH, "//*[contains(text(), 'Health Quest Book 6')]/parent::div/parent::div/div[2]/button")
    SELECT_THE_MY_WISHLIST_XPATH = (By.XPATH, "//*[contains(text(),'My Wishlist')]")
    CLICK_ON_VIEW_WSIHLIST = (By.XPATH, "//*[text()='View Wishlist']")
    CAPTURE_TEXT_FORM_WISHLIST = (By.XPATH, "//*[text()='Health Quest Book 6']")
    REMOVE_THE_WISHLIST_PRODUCT_XPATH = (By.XPATH, "//*[text()=' Remove']")
    VERIFY_REMOVE_MESSAGE_XPATH = (By.XPATH, "//*[text()='Book Successfully Removed from Wishlist']")



