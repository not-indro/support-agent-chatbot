import json
import time
from playwright.sync_api import sync_playwright

DOC_URLS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}


def scrape_documentation(url, platform):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print(f"Scraping {platform} documentation: {url}")
        retries = 3
        for attempt in range(retries):
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=60000)  
                break  
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt == retries - 1:
                    print(f"Failed to load {url} after {retries} attempts.")
                    browser.close()
                    return []
                time.sleep(5)

        page.wait_for_selector("body", state="attached", timeout=60000)


        if platform == "segment":
            links = page.eval_on_selector_all(
                "a[href^='/docs/']",  
                "elements => elements.map(el => 'https://segment.com' + el.getAttribute('href'))"
            )
        elif platform == "mparticle":
            links = page.eval_on_selector_all(
                "a[href^='/']",  
                "elements => elements.map(el => 'https://docs.mparticle.com' + el.getAttribute('href'))"
            )
        elif platform == "lytics":
            links = page.eval_on_selector_all(
                "a[href^='/']",  
                "elements => elements.map(el => 'https://docs.lytics.com' + el.getAttribute('href'))"
            )
        elif platform == "zeotap":
            links = page.eval_on_selector_all(
                "a[href^='/']",  
                "elements => elements.map(el => 'https://docs.zeotap.com' + el.getAttribute('href'))"
            )
        links = list(set(links))


        docs = []
        for link in links:
            print(f"Scraping page: {link}")
            try:
                page.goto(link, wait_until="domcontentloaded", timeout=60000)
                page.wait_for_selector("body", state="attached", timeout=60000)

                # Extract the page content
                if platform == "segment":
                    content = page.eval_on_selector(
                        "main",  
                        "element => element.innerText"
                    )
                elif platform == "mparticle":
                    content = page.eval_on_selector(
                        "body",
                        "element => element.innerText"
                    )
                elif platform == "lytics":
                    content = page.eval_on_selector(
                        "body",
                        "element => element.innerText"
                    )
                elif platform == "zeotap":
                    content = page.eval_on_selector(
                        "body",  
                        "element => element.innerText"
                    )
                docs.append(content)
            except Exception as e:
                print(f"Error scraping {link}: {e}")
                continue

        browser.close()
        return docs

def save_docs_to_json():
    docs = {}
    for platform, url in DOC_URLS.items():
        print(f"Scraping {platform} documentation...")
        docs[platform] = scrape_documentation(url, platform)
    
    with open("cdp_docs.json", "w") as f:
        json.dump(docs, f, indent=4)

if __name__ == "__main__":
    save_docs_to_json()