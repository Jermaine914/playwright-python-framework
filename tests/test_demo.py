from playwright.sync_api import Page

def test_example_domain_title(page: Page):
    page.goto("https://example.com")
    assert "Example Domain" in page.title()

def test_python_org_search(page: Page):
    # This test gets its own brand-new browser tab and context automatically!
    page.goto("https://www.python.org/")
    assert "Python" in page.title()
