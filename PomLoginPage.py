from PomBasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver, maximize=False, minimize=False):
        super().__init__(driver, maximize, minimize)

    def login_to_site(self, userName, password, errorMessage="Invalid Login!"):
        super().getDriver().find_element_by_id("user-name").send_keys(userName)
        super().getDriver().find_element_by_id("password").send_keys(password)
        loginButton = super().getDriver().find_element_by_id("login-button")
        print("INFO: Username: " + userName + ", Password: " + password + " entered...Logging in...")
        loginButton.click()
        try:
            super().check_url("https://www.saucedemo.com/inventory.html", "Inventory Page", errorMessage)
            print("INFO: Logged in successfully.")
            return True
        except AssertionError as error:
            print("ERROR: " + str(error))
            return False

