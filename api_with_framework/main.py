from fastapi import FastAPI
from todo.router import router as todo_router 


app = FastAPI(
    title = "Todo App",
    description = "Simple app",
    version = "1.0.0"
)


app.include_router(todo_router, prefix="/api", tags=["todos"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API! Check out the docs at /docs"}



