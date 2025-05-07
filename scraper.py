import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

def get_news_article(query):
    url = f"https://www.google.com/search?q={query}+site:news.google.com"
    headers = {'User-Agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if "https" in href:
            return "Sample article content about " + query
    return "Couldn't fetch article. Please try a different topic."