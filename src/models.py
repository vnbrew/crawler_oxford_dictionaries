import database as _database
import sqlalchemy as _sql
import sqlalchemy.orm as _orm

class DictUrl(_database.Base):
    __tablename__ = "dict_urls"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    url_id = _sql.Column(_sql.String, unique=True, index=True)
    word = _sql.Column(_sql.String, index=True)
    url = _sql.Column(_sql.String, index=True)
    token = _sql.Column(_sql.String, index=True)
    status_code = _sql.Column(_sql.Integer, default=0)
    error_message = _sql.Column(_sql.String, nullable=True, default="")
    from_website = _sql.Column(_sql.String, nullable=True, default="")