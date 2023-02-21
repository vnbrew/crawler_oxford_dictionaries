import pydantic as _pydantic
from typing import List

class UrlInfoCreate(_pydantic.BaseModel):
    url: str
    pass

class DictUrlCreate(_pydantic.BaseModel):
    word: str
    url: str
    from_website: str
    pass

class DictUrl(_pydantic.BaseModel):
    id: int
    word_id: str
    token: str
    word: str
    url: str
    from_website: str
    status_code: int
    error_message: str
    class Config:
        orm_mode = True