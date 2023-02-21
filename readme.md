# setup

```sh
git clone git@github.com:vnbrew/crawler_oxford_dictionaries.git
cd crawler_oxford_dictionaries
python3 -m venv .env
source .env/bin/activate
pip3 install -r requirements.txt
pip3 install -U pip setuptools wheel
pip3 install -U spacy
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
```

# Run api
```sh
cd src
uvicorn main:app --reload
```


# Api docs
```sh
http://127.0.0.1:8000/docs
```