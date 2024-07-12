from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {
        "message": [
            "Hello Krishnamurai  :)",
            "We succesfully launch the  FastAPI application!",
            "Have a Good Day."
        ]
    }