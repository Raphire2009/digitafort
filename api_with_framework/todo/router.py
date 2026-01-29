from fastapi import APIRouter, HTTPException, status
from typing import List
from . import database as db 
from .models import TodoItem,CreateItem


router = APIRouter()

@router.get('/todos', respense_model= List[TodoItem])
def get_todo():
    "Get all todo"
    return db.get_all_todo()

@router.post("/todo", respense_model= TodoItem, status_code= status.HTTP_201_CREATED)
def create_new_todo(todo_data:CreateItem):
    return db.create_todo(todo_data) 
    
    