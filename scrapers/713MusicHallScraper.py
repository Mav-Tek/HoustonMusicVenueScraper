from playwright.sync_api import sync_playwright
from datetime import datetime
import os

def scrape_713musichall():
    # Ensure output directory exists
    output_dir = os.path.join(os.path.dirname(__file__), "../data")
    os.makedirs(output_dir, exist_ok=True)

    # File to save HTML
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"713musichall_{timestamp}.html")

    url = "https://www.713musichall.com/shows"

    with sync_playwright() as p:
        # Launch Chromium in headless mode (you can set headless=False to watch)
        browser = p.chromium.launch(headless=True)

        # Spoof a realistic browser environment
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/115.0.0.0 Safari/537.36",
            viewport={"width": 1366, "height": 768},
            locale="en-US",
        )

        page = context.new_page()

        print(f"Loading {url}...")
        page.goto(url, wait_until="networkidle")

        # Wait for JS to finish rendering
        page.wait_for_timeout(3000)  # wait 3 seconds

        # Get the rendered HTML
        html_content = page.content()

        # Save to file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"Saved HTML to {filename}")

        browser.close()


if __name__ == "__main__":
    scrape_713musichall()
