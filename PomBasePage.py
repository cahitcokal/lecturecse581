from selenium import webdriver


class BasePage:

    def __init__(self, driver: webdriver, maximize, minimize):
        self.__driver = driver
        if maximize:
            self.__driver.maximize_window()
        if minimize:
            self.__driver.minimize_window()

    def getDriver(self):
        return self.__driver

    def close(self):
        self.__driver.close()

    def get_url(self):
        return self.__driver.current_url

    def check_url(self, urlToCheck, pageName, message):
        assert self.get_url() == urlToCheck, "Not " + pageName + " Page! " + message

    def open_left_up_menu(self):
        self.__driver.find_element_by_xpath("//*[@id=\"menu_button_container\"]/div/div[3]/div/button").click()
        print("INFO: Left menu opened.")

    def close_left_up_menu(self):
        self.__driver.find_element_by_xpath("//*[@id=\"menu_button_container\"]/div/div[2]/div[2]/div/button").click()
        print("INFO: Left menu closed.")

    def go_to_cart_page(self):
        self.__driver.find_element_by_xpath("//*[@id=\"shopping_cart_container\"]/a").click()
        print("INFO: Cart icon clicked. Navigated to cart page.")

    def log_out(self):
        self.__driver.find_element_by_xpath("//*[@id=\"logout_sidebar_link\"]").click()
        print("INFO: Logout menu item clicked.")

