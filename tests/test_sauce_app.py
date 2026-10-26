import pytest
from playwright.sync_api import Page, expect
from pages.sauce_inventory_page import SauceInventoryPage
from pages.sauce_login_page import SauceLoginPage

def test_inventory_loads_after_login(authenticated_sauce_page: Page):
    inventory_page = SauceInventoryPage(authenticated_sauce_page)
    expect(inventory_page.page_title).to_be_visible()
    assert inventory_page.get_item_count() > 0

# --- NEW PARAMETERIZED TEST ---
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
        ("standard_user", "wrong_password", "Username and password do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
)
def test_invalid_login_scenarios(page: Page, username: str, password: str, expected_error: str):
    login_page = SauceLoginPage(page)
    login_page.navigate()
    
    # Attempt login with the parameterized inputs
    login_page.login(username, password)
    
    # Assert that the correct error message appears
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(expected_error)
