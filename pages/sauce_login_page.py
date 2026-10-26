from playwright.sync_api import Page

class SauceLoginPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators using user-facing selectors
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")

    def navigate(self):
        """Navigate to the SauceDemo login page."""
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        """Perform the login action."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
