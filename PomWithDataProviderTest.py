from selenium import webdriver
import time
import unittest
from ddt import ddt, data, unpack
from PomLoginPage import LoginPage
from PomInventoryPage import InventoryPage
from PomInventoryItemPage import InventoryItemPage
from PomShoppingCartPage import ShoppingCartPage


@ddt
class TestDDTDataUnpack(unittest.TestCase):

    @data(("standard_user", "secret_sauce", "TEST CASE 1: Successful path scenario with \"standard_user\" account."),
          ("problem_user", "secret_sauce", "TEST CASE 2: Successful path scenario with \"problem_user\" account."),
          ("invalid_user", "secret_sauce", "TEST CASE 3: Unsuccessful login attempt (invalid user)."),
          ("standard_user", "invalid_password", "TEST CASE 4: Unsuccessful login attempt (invalid pass)."),
          ("invalid_user", "invalid_password", "TEST CASE 5: Unsuccessful login attempt (invalid user and pass)."))
    @unpack
    def test_with_ddt_data_unpack(self, username, password, message):
        # Create web driver and go to the page
        driver = webdriver.Chrome(executable_path="c:\\selenium browser drivers\\chromedriver.exe")
        driver.get("https://www.saucedemo.com/")
        print("\n------------------------------------------------------------")
        print(message)
        print("---> TEST CASE STARTED: username: \"" + username + "\" password: \"" + password + "\"\n")

        # Step 1: Login with standard user
        loginPage = LoginPage(driver, maximize=True)
        time.sleep(1)
        if loginPage.login_to_site(username, password):
            # Step 2: List the items by price from low to high
            inventoryPage = InventoryPage(driver)
            time.sleep(1)
            inventoryPage.order_items_by_price_low2high()
            time.sleep(1)

            # Step 3: Select first item via header link
            inventoryPage.goto_item_page_by_link(1)
            time.sleep(1)

            # Step 4: Add the item to the shopping cart
            inventoryItemPage = InventoryItemPage(driver)
            time.sleep(1)
            inventoryItemPage.add_or_remove_item()
            time.sleep(1)

            # Step 5: Go back to the inventory page
            inventoryItemPage.back_to_inventory_page()
            time.sleep(1)
            # Select first item via image link
            inventoryPage.goto_item_page_by_image(1)
            time.sleep(1)

            # Step 6: Add the item to the cart
            inventoryItemPage.add_or_remove_item()
            time.sleep(1)

            # Step 7: Go to the cart page
            inventoryItemPage.go_to_cart_page()
            time.sleep(1)

            # Step 8: Check and verify the items in cart
            shoppingCartPage = ShoppingCartPage(driver)
            time.sleep(1)

            if shoppingCartPage.count_items(2):
                # Step 9: Proceed checkout page
                time.sleep(1)
                shoppingCartPage.check_out()
                time.sleep(1)

                # Step 10: Complete and logout
                shoppingCartPage.fill_form_and_continue("Cahit", "Çokal", "00000")
                time.sleep(1)
                shoppingCartPage.finish_shopping()
                time.sleep(1)
            else:
                print("ERROR: No item in cart! Proceed to logout...")
            # Logout
            shoppingCartPage.open_left_up_menu()
            time.sleep(1)
            shoppingCartPage.log_out()
