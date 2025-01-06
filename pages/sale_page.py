from pages.base_page import BasePage


class SalePage(BasePage):
    URL = "https://magento.softwaretestingboard.com/sale.html"

    def __init__(self, page):
        super().__init__(page)
        self.title = self.page.locator("h1.page-title")
        self.side_bar_menu = self.page.locator("div.sidebar.sidebar-main")
        self.promo_image = self.page.locator("div.blocks-promo")
