import database as _database
import sqlalchemy as _sql
import sqlalchemy.orm as _orm

class Url(_database.Base):
    __tablename__ = "urls"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    url_id = _sql.Column(_sql.String, unique=True, index=True)
    url = _sql.Column(_sql.String, unique=True, index=True)
    token = _sql.Column(_sql.String, index=True)
    word = _sql.Column(_sql.String, index=True)
    status_code = _sql.Column(_sql.Integer, default=0)
    error_message = _sql.Column(_sql.String, nullable=True, default="")
    from_website = _sql.Column(_sql.String, nullable=True, default="")

    words = _orm.relationship("Word", back_populates="owner")


class Word(_database.Base):
    __tablename__ = "words"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    pron_br = _sql.Column(_sql.String, nullable=True, default="")
    pron_br_audio = _sql.Column(_sql.String, nullable=True, default="")
    pron_am = _sql.Column(_sql.String, nullable=True, default="")
    pron_am_audio = _sql.Column(_sql.String, nullable=True, default="")
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("urls.url_id"))

    owner = _orm.relationship("Url", back_populates="words")