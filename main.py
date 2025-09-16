from fastapi import FastAPI
from random import randint


app = FastAPI()
@app.get("/")
def root():
    return {"number": randint(1, 10)}

@app.get("/random")
def get_random_number():
    """Return a random integer between 1 and 10."""
    return {"number": randint(1, 10)}
