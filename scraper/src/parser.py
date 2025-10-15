# parser.py
from bs4 import BeautifulSoup
import requests
import time
from .types import BookItem

BASE_URL = "https://books.toscrape.com/"

def parse_books(html: str, delay_ms: int = 700) -> list[BookItem]:
    """Parse a listing page and fetch each book's detail page for its category."""
    soup = BeautifulSoup(html, "html.parser")
    items = []

    for article in soup.select("article.product_pod"):
        title = article.h3.a["title"]
        rel_url = article.h3.a["href"]

        # Build full URL
        if "catalogue/" not in rel_url:
            rel_url = "catalogue/" + rel_url
        book_url = BASE_URL + rel_url.replace("../", "")

        price = article.select_one(".price_color").text.strip()
        rating = article.p["class"][1] if article.p and len(article.p["class"]) > 1 else "Unknown"
        availability = article.select_one(".availability").text.strip()

        try:
            time.sleep(delay_ms / 1000)
            resp = requests.get(book_url, headers={"User-Agent": "webscrape-intern-bot/1.0"})
            resp.raise_for_status()
            detail_html = resp.content.decode("utf-8", "ignore")

            detail_soup = BeautifulSoup(detail_html, "html.parser")
            breadcrumb = detail_soup.select_one(".breadcrumb li:nth-of-type(3)")
            category = breadcrumb.text.strip() if breadcrumb else "Unknown"

        except Exception as e:
            print(f"⚠️ Error fetching category for {title}: {e}")
            category = "Unknown"

        items.append(BookItem(
            title=title,
            price=price,
            availability=availability,
            rating=rating,
            category=category,
            url=book_url,
        ))

    return items
