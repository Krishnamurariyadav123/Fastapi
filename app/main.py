from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

@app.get("/")
def index():
    return {"title": "Hello Krishnamurai  :)"}

Instrumentator().instrument(app).expose(app)
