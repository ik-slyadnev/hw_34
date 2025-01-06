import allure
from playwright.sync_api import expect


@allure.epic("Collections Page")
@allure.feature("Products Display")
class TestCollectionsPage:

    @allure.title("Products are displayed on collections page")
    def test_products_display(self, collections_page):
        with allure.step("Open collections page"):
            collections_page.open()
            collections_page.click_consent_button()

        with allure.step("Count products"):
            products_count = collections_page.get_products_count()

        with allure.step("Verify products presence"):
            assert products_count > 0, "На странице нет товаров"

    @allure.title("Sort dropdown is present")
    def test_sort_dropdown_presence(self, collections_page):
        with allure.step("Open collections page"):
            collections_page.open()
            collections_page.click_consent_button()

        with allure.step("Verify sort dropdown visibility"):
            expect(collections_page.sorter).to_be_visible()

    @allure.title("Page title is correct")
    def test_page_title(self, collections_page):
        with allure.step("Open collections page"):
            collections_page.open()
            collections_page.click_consent_button()

        with allure.step("Verify page title"):
            expect(collections_page.title).to_have_text("Eco Friendly")
