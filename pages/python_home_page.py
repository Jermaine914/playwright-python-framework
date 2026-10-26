from playwright.sync_api import Page

class PythonHomePage:
    def __init__(self, page: Page):
        self.page = page
        
        # Define your locators as attributes
        self.search_input = page.get_by_placeholder("Search")
        self.go_button = page.get_by_role("button", name="GO")

    def navigate(self):
        """Navigate to the home page."""
        self.page.goto("https://www.python.org/")

    def search(self, query: str):
        """Perform a search action."""
        self.search_input.fill(query)
        self.go_button.click()
