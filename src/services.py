import sqlalchemy.orm as _orm
import models as _models, schemas as _schemas, database as _database
import spacy as _spacy

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_urls(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.Url).offset(skip).limit(limit).all()

def get_url_by_id(db: _orm.Session, id: str):
    return db.query(_models.Url).filter(_models.Url.url_id == id).first()

def create_url(db: _orm.Session, dictUrl: _schemas.UrlCreate):
    nlp = _spacy.load("en_core_web_md")
    token = nlp.vocab.strings[dictUrl.word]
    db_url = _models.Url(word=dictUrl.word, url=dictUrl.url, token=token, from_website=dictUrl.from_website)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def insert_url(db: _orm.Session, url_id: str, word: str, url: str, token: str,from_website: str):
    db_url = _models.Url(url_id=url_id, word=word, url=url, token=token, from_website=from_website)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url
