from pages.base_page import BasePage


class CollectionsPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/collections/eco-friendly.html"

    def __init__(self, page):
        super().__init__(page)
        self.products = self.page.locator("li.product-item")
        self.sorter = self.page.locator("#sorter").first
        self.prices = self.page.locator("span.price")
        self.limiter = self.page.locator("#limiter")
        self.title = self.page.locator("h1.page-title")

    def get_products_count(self):
        return self.products.count()

    def sort_products(self, option):
        self.sorter.select_option(value=option)
