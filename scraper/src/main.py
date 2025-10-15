import json, argparse, shutil, os
from .fetcher import fetch_page
from .parser import parse_books
from .pagination import next_page_url
from .robots import check_robots


def crawl(start_url: str, max_pages: int = 3, delay_ms: int = 700, dry_run: bool = False):
    if not check_robots(start_url):
        print("🚫 Not allowed by robots.txt")
        return

    url = start_url
    all_items = []
    for page in range(max_pages):
        print(f"Fetching: {url}")
        html = fetch_page(url, delay_ms)
        items = parse_books(html)
        print(f"→ Found {len(items)} books on page {page+1}")
        all_items.extend(items)

        next_url = next_page_url(html, url)
        if not next_url:
            break
        url = next_url

    if not dry_run:
        with open("scraper/data/items.jsonl", "w", encoding="utf-8") as f:
            for item in all_items:
                f.write(json.dumps(item.__dict__) + "\n")
        print(f"✅ Saved {len(all_items)} items to scraper/data/items.jsonl")
        
        os.makedirs("ui/public/data", exist_ok=True)
        shutil.copy2("scraper/data/items.jsonl", "ui/public/data/items.jsonl")
        print("🔄 Synced to ui/public/data/items.jsonl")
    else:
        print("Dry run: skipping save")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", default="https://books.toscrape.com/")
    parser.add_argument("--max-pages", type=int, default=3)
    parser.add_argument("--delay-ms", type=int, default=700)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    crawl(args.start, args.max_pages, args.delay_ms, args.dry_run)
