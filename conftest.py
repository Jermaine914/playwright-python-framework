import pytest
from playwright.sync_api import Page
from pages.sauce_login_page import SauceLoginPage

@pytest.fixture
def authenticated_sauce_page(page: Page) -> Page:
    """Fixture that logs into SauceDemo and returns the authenticated page."""
    login_page = SauceLoginPage(page)
    login_page.navigate()
    # SauceDemo provides standard test users: 'standard_user' and 'secret_sauce'
    login_page.login("standard_user", "secret_sauce")
    
    # Yield hands control back to the test once setup is finished
    yield page
