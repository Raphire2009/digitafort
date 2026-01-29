from typing import List,Dict,Optional
from .models import TodoItem , CreateItem






fake_db:Dict[int, TodoItem] = {
    1: TodoItem(id=1, title="learn how to cook", description="boil water first"),
    2: TodoItem(id=2, title="learn how to drive", description="on the car first", completed=True)
}

next_id = 3





def get_all_todo()->List[TodoItem]:
    return List(fake_db.values())


def get_todo_by_id(id:int)->Optional[TodoItem]:
    return fake_db.get(id)

def create_todo(todo_data:CreateItem)->TodoItem:
    global next_id
    new_todo = TodoItem(id=next_id, **todo_data.dict())
    fake_db[next_id] = new_todo
    next_id += 1
    return new_todo
                 
def update_todo(todo_id :int, todo_data:CreateItem)->Optional[TodoItem]:
    if todo_id in fake_db :
        todo_item = fake_db[todo_id] 
        todo_item.title = todo_data.title
        todo_item.description = todo_data.description
        return todo_item
    return None

def delete_todo(todo_id: int)->bool:
    if todo_id in fake_db:
        del fake_db[todo_id]
        return True
    return False

