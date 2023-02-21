import scraper as _scraper
import constant as define
import json as _json

def create_urls_dict():
    urls = dict()
    urls["urls"] = _scraper.url_of_all_word(define.oxfordlearnersdictionaries_url)
    return urls

if __name__ == "__main__":
    urls = create_urls_dict()
    with open(define.urls_oxfordlearnersdictionaries_file_name, mode="w") as urls_file:
        _json.dump(urls, urls_file, ensure_ascii=False)
