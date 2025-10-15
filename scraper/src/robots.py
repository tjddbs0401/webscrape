import requests
from urllib.robotparser import RobotFileParser

def check_robots(base_url: str, user_agent: str = "webscrape-intern-bot") -> bool:
    robots_url = base_url.rstrip("/") + "/robots.txt"
    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
    except requests.RequestException:
        print("⚠️ Could not read robots.txt")
        return True
    allowed = rp.can_fetch(user_agent, base_url)
    print(f"robots.txt allows scraping: {allowed}")
    return allowed
