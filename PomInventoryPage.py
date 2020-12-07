from selenium.webdriver.support.ui import Select
from PomBasePage import BasePage


class InventoryPage(BasePage):

    def __init__(self, driver, maximize=False, minimize=False):
        super().__init__(driver, maximize, minimize)

    def order_items_by_price_low2high(self):
        select = Select(super().getDriver().find_element_by_xpath('//*[@id="inventory_filter_container"]/select'))
        select.select_by_value("lohi")
        print("INFO: Items sorted by price, from low to high.")

    def order_items_by_price_high2low(self):
        select = Select(super().getDriver().find_element_by_xpath('//*[@id="inventory_filter_container"]/select'))
        select.select_by_value("hilo")
        print("INFO: Items sorted by price, from high to low.")

    def order_items_by_name_a2z(self):
        select = Select(super().getDriver().find_element_by_xpath('//*[@id="inventory_filter_container"]/select'))
        select.select_by_value("az")
        print("INFO: Items sorted by name, from A to Z.")

    def order_items_by_name_z2a(self):
        select = Select(super().getDriver().find_element_by_xpath('//*[@id="inventory_filter_container"]/select'))
        select.select_by_value("za")
        print("INFO: Items sorted by name, from Z to A.")

    def goto_item_page_by_link(self, itemNumber):
        super().getDriver().find_elements_by_xpath("//div[2]/div/div[2]/div/div[" +
                                                   str(itemNumber) + "]/div[2]/a")[0].click()
        print("INFO: Item number " + str(itemNumber) + " is selected via link.")

    def goto_item_page_by_image(self, itemNumber):
        super().getDriver().find_elements_by_xpath("//div[2]/div/div[2]/div/div[" +
                                                   str(itemNumber) + "]/div[1]/a/img")[0].click()
        print("INFO: Item number " + str(itemNumber) + " is selected via image.")
