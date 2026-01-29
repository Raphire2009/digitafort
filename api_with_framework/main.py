from fastapi import FastAPI

#todo 
#init the fastapi

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "World"}



