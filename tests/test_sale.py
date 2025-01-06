import allure
from playwright.sync_api import expect


@allure.epic("Sale Page")
@allure.feature("Sale Page Elements")
class TestSalePage:

    @allure.title("Sale page title is correct")
    def test_page_title(self, sale_page):
        with allure.step("Open sale page"):
            sale_page.open()
            sale_page.click_consent_button()

        with allure.step("Verify page title"):
            expect(sale_page.title).to_have_text("Sale")

    @allure.title("Side bar menu is visible")
    def test_view_side_bar(self, sale_page):
        with allure.step("Open sale page"):
            sale_page.open()
            sale_page.click_consent_button()

        with allure.step("Verify side bar visibility"):
            expect(sale_page.side_bar_menu).to_be_visible()

    @allure.title("Promo section is visible")
    def test_view_promo(self, sale_page):
        with allure.step("Open sale page"):
            sale_page.open()
            sale_page.click_consent_button()

        with allure.step("Verify promo section visibility"):
            expect(sale_page.promo_image).to_be_visible()
