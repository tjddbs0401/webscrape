from urllib.parse import urljoin
from bs4 import BeautifulSoup

def next_page_url(html: str, current_url: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")
    next_link = soup.select_one("li.next a")
    if next_link:
        return urljoin(current_url, next_link["href"])
    return None
