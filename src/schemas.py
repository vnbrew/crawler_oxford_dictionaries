import pydantic as _pydantic
from typing import List

class UrlInfoCreate(_pydantic.BaseModel):
    url: str
    pass

class UrlCreate(_pydantic.BaseModel):
    word: str
    url: str
    from_website: str
    pass

class Url(_pydantic.BaseModel):
    id: int
    url_id: str
    url: str
    token: str
    word: str
    from_website: str
    status_code: int
    error_message: str
    class Config:
        orm_mode = True