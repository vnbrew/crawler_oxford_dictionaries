import json as _json
from typing import Dict
import constant as define

def get_all_urls() -> Dict:
    with open(define.urls_oxfordlearnersdictionaries_file_name) as urls_file:
        data = _json.load(urls_file)

    return data["urls"]
