# setup

```sh
git clone git@github.com:vnbrew/crawler_oxford_dictionaries.git
cd crawler_oxford_dictionaries
python3 -m venv .env
source .env/bin/activate
pip3 install -r requirements.txt
```

# Run api
```sh
cd src
uvicorn main:app --reload
```