from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "title": "Hello Krishnamurari yadav :)",
        "message": "We have succesffuly launch  FastAPI application!",
        "status": "Running smoothly"
    }
