from playwright.sync_api import Page

class SauceInventoryPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators on the products page
        self.page_title = page.get_by_text("Products")
        self.inventory_items = page.locator(".inventory_item")

    def get_item_count(self) -> int:
        """Return the number of product items displayed."""
        return self.inventory_items.count()
