import time, random, requests

def fetch_page(url: str, delay_ms: int = 700) -> str:
    time.sleep(random.uniform(delay_ms/1000, (delay_ms+500)/1000))
    headers = {"User-Agent": "webscrape-intern-bot/1.0"}
    response = requests.get(url, headers=headers)
    html = response.content.decode("utf-8", "ignore")
    return html
