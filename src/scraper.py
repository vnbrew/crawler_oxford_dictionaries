from urllib.parse import urljoin
import requests as _requests
import bs4 as _bs4
from typing import List, Dict
import constant as define

def _get_page(url: str) -> _bs4.BeautifulSoup:
    headers = _requests.utils.default_headers()
    headers={
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    }
    page = _requests.get(url, headers=headers)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def get_all_word_url_from_oxford(url: str) -> Dict:
    urls = dict()
    page = _get_page(url)
    raw_urls = page.find(class_="top-g").find_all("li")
    for url in raw_urls:
        word = url.a.get_text()
        url = urljoin(define.base_url, url.a["href"])
        if(word == "mission" and url == "https://www.oxfordlearnersdictionaries.com/definition/english/impossible" ):
            url = "https://www.oxfordlearnersdictionaries.com/definition/english/" + word
        if(word == "more" and url == "https://www.oxfordlearnersdictionaries.com/definition/english/many" ):
            url = "https://www.oxfordlearnersdictionaries.com/definition/english/more_1"
        if(word == "most" and url == "https://www.oxfordlearnersdictionaries.com/definition/english/many" ):
            url = "https://www.oxfordlearnersdictionaries.com/definition/english/most_1"
        if(word == "much" and url == "https://www.oxfordlearnersdictionaries.com/definition/english/many" ):
            url = "https://www.oxfordlearnersdictionaries.com/definition/english/much_1"
        urls[word] = url
    return urls