from pages.base_page import BasePage


class AccountPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/create/"

    def __init__(self, page):
        super().__init__(page)
        self.firstname = self.page.locator("#firstname")
        self.lastname = self.page.locator("#lastname")
        self.email = self.page.locator("#email_address")
        self.password = self.page.locator("#password")
        self.confirm_password = self.page.locator("#password-confirmation")
        self.create_button = self.page.locator("button.action.submit.primary")
        self.success = self.page.locator("div.message-success")
        self.password_error = self.page.locator("#password-error")
        self.email_error = self.page.locator("#email_address-error")

    def create_account(self, firstname, lastname, email, password):
        self.firstname.fill(firstname)
        self.lastname.fill(lastname)
        self.email.fill(email)
        self.password.fill(password)
        self.confirm_password.fill(password)
        self.create_button.click()
