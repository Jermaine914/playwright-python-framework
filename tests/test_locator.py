from playwright.sync_api import Page, expect
from pages.python_home_page import PythonHomePage

def test_search_via_page_object(page: Page):
    # Initialize the page object
    home_page = PythonHomePage(page)
    
    # Use the page object's methods
    home_page.navigate()
    home_page.search("pytest")
    
    # Assert the results heading is visible
    heading = page.get_by_role("heading", name="Results")
    expect(heading).to_be_visible()
