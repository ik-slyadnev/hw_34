import allure

class BasePage:
    def __init__(self, page):
        self.page = page
        self.timeout = 10000  # в миллисекундах

    def open(self):
        self.page.goto(self.URL)
        self.page.wait_for_url(self.URL)

    def is_opened(self):
        self.page.wait_for_url(self.URL)

    def is_element_present(self, selector):
        """Проверка наличия элемента на странице"""
        return self.page.locator(selector).count() > 0

    def click_consent_button(self):
        """Клик по кнопке согласия"""
        self.page.get_by_role("button", name="AGREE", exact=True).click()

    def take_screenshot(self, name="screenshot"):
        allure.attach(
            self.page.screenshot(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
