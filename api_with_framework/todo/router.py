from fastapi import APIRouter, HTTPException, status
from typing import List
from . import database as db 
from .models import TodoItem,CreateItem


router = APIRouter()

@router.get('/todos', response_model= List[TodoItem])
def get_todo():
    "Get all todo"
    return db.get_all_todo()

@router.post("/todo", response_model= TodoItem, status_code= status.HTTP_201_CREATED)
def create_new_todo(todo_data:CreateItem):
    return db.create_todo(todo_data) 

#getting the item by id 
@router.get("/todo{todo_id}", response_model=TodoItem)
def get_single_todo(todo_id: int):
    todo =   db.get_todo_by_id(todo_id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo Not Found")
    return todo 


#update
@router.put("/todo{todo_id}", response_model=TodoItem)
def update_existing_todo(todo_id:int, todo_data:CreateItem):
    todo = db.update_todo(todo_id,todo_data)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not Found")
    return todo


@router.delete("/todo{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_todo(todo_id:int):
    if not db.delete_todo(todo_id):
        raise HTTPException(status_code=status.HTTP_404_NOt_FOUND, details="todo Not Found")
    return 




    