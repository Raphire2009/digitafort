from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

#todo
#a class for the todoitem model which show our data 
# second one for the user to create  a new data



class TodoItem(BaseModel):
    id: int 
    title: str  = Field(min_length=1, max_length=100)
    description :Optional[str] = None
    completed : bool = False


class CreateItem(BaseModel):
    title : str = Field(min_length=1, max_length=100)
    description : Optional[str] = None

