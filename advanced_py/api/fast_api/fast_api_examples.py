# Python FastAPI Example
# To run this example:
# 1. Install the required packages: pip install -r requirements.txt
# 2. Run the server: uvicorn fast_api_examples:app --reload
# 3. Open your browser and go to http://127.0.0.1:8000/

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
