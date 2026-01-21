from typing import List,Dict
from .models import TodoItem



[]
good:Dict[int, str]= {
    1:  "ggo",
    2: "hhh"
}


fake_db:Dict[int, TodoItem] = {
    1: TodoItem(id=1, title="learn how to cook", description="boil water first"),
    2: TodoItem(id=2, title="learn how to drive", description="on the car first", completed=True)
}

next_id = 3





def get_all_todo()->List[TodoItem]:
    return List()