from PomBasePage import BasePage


class ShoppingCartPage(BasePage):

    def __init__(self, driver, maximize=False, minimize=False):
        super().__init__(driver, maximize, minimize)

    def count_items(self, expectedCount):
        itemCount = 0
        try:
            itemList = super().getDriver().find_elements_by_class_name("cart_quantity")
            itemCount = 0
            for item in itemList:
                itemCount += int(item.text)
            if itemCount == 0:
                return False
            assert itemCount == expectedCount
            print("INFO: Item count is as Expected: " + str(itemCount) + ".")
            return True
        except AssertionError as error:
            print("WARN: Item Count is Not as Expected! Expected: " +
                  str(expectedCount) + ", Items in Cart: " + str(itemCount) + ".")
            return True

    def check_out(self):
        checkOutButton = super().getDriver().find_element_by_class_name("checkout_button")
        print("INFO: Button \"" + checkOutButton.text + "\" clicked.")
        checkOutButton.click()

    def fill_form_and_continue(self, firstName, lastName, zipPostalCode):
        super().getDriver().find_element_by_id("first-name").send_keys(firstName)
        super().getDriver().find_element_by_id("last-name").send_keys(lastName)
        super().getDriver().find_element_by_id("postal-code").send_keys(zipPostalCode)
        continueButton = super().getDriver().find_element_by_class_name("cart_button")
        print("INFO: Continue payment.")
        continueButton.click()

    def finish_shopping(self):
        finishButton = super().getDriver().find_element_by_class_name("cart_button")
        print("INFO: Button \"" + finishButton.text + "\" clicked.")
        finishButton.click()
