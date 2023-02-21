from fastapi import FastAPI, Response
import services as _services
from typing import List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas
import scraper as _scraper
import constant as _const
import spacy as _spacy
import argparse

app = FastAPI()

_services.create_database()

@app.get("/")
async def root():
    return {"message": "Hello Oxford Dictionaries"}

@app.get("/urls/", response_model=List[_schemas.Url])
def read_urls(
    skip: int = 0,
    limit: int = 100,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    urls = _services.get_urls(db=db, skip=skip, limit=limit)
    return urls

@app.post("/urls/", response_model=dict)
def create_urls(urlInfo: _schemas.UrlInfoCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    nlp = _spacy.load("en_core_web_md")
    raw_urls_oxford = _scraper.get_all_word_url_from_oxford(urlInfo.url)
    result = dict()
    exits = dict()
    for key, value in raw_urls_oxford.items():
        word = key
        url = value
        url_id=_const.oxfordlearnersdictionaries_key + "_"+word
        db_url = _services.get_url_by_id(db=db, id=url_id)
        if db_url:
            exits[word] = url
            continue
        token = str(nlp.vocab.strings[word])
        _services.insert_url(db=db, url_id=url_id, word=word, url=url, token=token, from_website=_const.base_url)
    result["exits"] = exits
    result["input"] = raw_urls_oxford
    return result


def parse_args():
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('filename')
    return parser.parse_args()

def do_url():
    print("do url")
    pass

def do_word():
    print("do word")
    pass

def main():
    args = parse_args()
    if(args.filename == "url"):
        do_url()
    if(args.filename == "word"):
        do_word()

if __name__ == '__main__':
    main()

