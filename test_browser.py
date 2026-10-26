def test_google_title(page):
    page.goto("https://google.com")
    assert "Google" in page.title()

