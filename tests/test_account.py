import allure
from utils.user_data import Users
from playwright.sync_api import expect


@allure.epic("Registration Functionality")
@allure.feature("Account Creation")
class TestRegistrationPage:

    @allure.title("Successful user registration with valid credentials")
    def test_valid_registration(self, account_page):
        with allure.step("Open registration page"):
            account_page.open()
            account_page.click_consent_button()

        with allure.step("Fill registration form with valid data"):
            account_page.create_account(
                firstname=Users.firstname,
                lastname=Users.lastname,
                email=Users.email,
                password=Users.password,
            )

        with allure.step("Verify success message"):
            expect(account_page.success).to_be_visible()

    @allure.title("Registration fails with short password")
    def test_short_password(self, account_page):
        with allure.step("Open registration page"):
            account_page.open()
            account_page.click_consent_button()

        with allure.step("Fill registration form with short password"):
            account_page.create_account(
                firstname=Users.firstname,
                lastname=Users.lastname,
                email=Users.email,
                password="lol",
            )

        with allure.step("Verify error message"):
            expect(account_page.password_error).to_have_text(
                "Minimum length of this field must be equal or greater "
                "than 8 symbols. Leading and trailing spaces will be "
                "ignored."
            )

    @allure.title("Registration fails with empty email")
    def test_empty_email(self, account_page):
        with allure.step("Open registration page"):
            account_page.open()
            account_page.click_consent_button()

        with allure.step("Fill registration form with empty email"):
            account_page.create_account(
                firstname=Users.firstname,
                lastname=Users.lastname,
                email=" ",
                password=Users.password,
            )

        with allure.step("Verify error message"):
            expect(account_page.email_error).to_have_text(
                "This is a required field."
            )
