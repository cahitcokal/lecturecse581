from PomBasePage import BasePage


class InventoryItemPage(BasePage):

    def __init__(self, driver, maximize=False, minimize=False):
        super().__init__(driver, maximize, minimize)

    def add_or_remove_item(self):
        addRemoveButton = super().getDriver().find_element_by_class_name("btn_inventory")
        buttonTextBeforeClick = addRemoveButton.text
        print("INFO: Button \"" + buttonTextBeforeClick + "\" clicked.")
        addRemoveButton.click()
        if addRemoveButton.text == buttonTextBeforeClick:
            print("WARN: Item was not added to Cart!")

    def back_to_inventory_page(self):
        backButton = super().getDriver().find_element_by_class_name("inventory_details_back_button")
        print("INFO: Button \"" + backButton.text + "\" clicked.")
        backButton.click()
