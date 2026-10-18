import os
from playwright.sync_api import sync_playwright

def capture_screenshots():
    cwd = os.getcwd()
    file_url = f"file://{cwd}/index.html"

    with sync_playwright() as p:
        # Desktop viewport
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        page.goto(file_url)
        page.wait_for_timeout(1000)

        # 1. Main Dashboard
        page.screenshot(path="assets/screenshots/dashboard.png", full_page=False)

        # 2. Habit Matrix
        matrix_element = page.locator("section:has-text('Weekly Habit Matrix')")
        if matrix_element.count() > 0:
            matrix_element.first.screenshot(path="assets/screenshots/habit-matrix.png")

        # 3. Analytics Sidebar
        analytics_element = page.locator("aside")
        if analytics_element.count() > 0:
            analytics_element.first.screenshot(path="assets/screenshots/weekly-analytics.png")

        browser.close()

        # Mobile Viewport
        browser_mobile = p.chromium.launch(headless=True)
        context_mobile = browser_mobile.new_context(viewport={"width": 390, "height": 844}, is_mobile=True)
        page_mobile = context_mobile.new_page()
        page_mobile.goto(file_url)
        page_mobile.wait_for_timeout(1000)

        # 4. Mobile View
        page_mobile.screenshot(path="assets/screenshots/mobile-view.png")
        browser_mobile.close()

if __name__ == "__main__":
    capture_screenshots()
