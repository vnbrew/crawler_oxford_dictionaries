from fastapi import FastAPI, Response
import urls_service as _service

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Oxford Dictionaries"}

@app.get("/urls")
async def all_urls():
    return _service.get_all_urls()
