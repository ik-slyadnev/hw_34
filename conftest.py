import pytest
from playwright.sync_api import Page
from pages.account_page import AccountPage
from pages.collections_page import CollectionsPage
from pages.sale_page import SalePage


@pytest.fixture
def account_page(page: Page):
    return AccountPage(page)


@pytest.fixture
def collections_page(page: Page):
    return CollectionsPage(page)


@pytest.fixture
def sale_page(page: Page):
    return SalePage(page)
