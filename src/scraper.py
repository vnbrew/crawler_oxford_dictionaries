from urllib.parse import urljoin
import requests as _requests
import bs4 as _bs4
from typing import List
import constant as define

def _get_page(url: str) -> _bs4.BeautifulSoup:
    headers = _requests.utils.default_headers()
    headers={
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    page = _requests.get(url, headers=headers)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def url_of_all_word(url: str) -> List[str]:
    page = _get_page(url)
    raw_urls = page.find(class_="top-g").find_all("li")
    urls = [urljoin(define.base_url, url.a["href"]) for url in raw_urls]
    return urls