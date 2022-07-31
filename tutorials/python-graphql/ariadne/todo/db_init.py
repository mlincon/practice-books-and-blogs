from main import db

db.create_all()


from datetime import datetime
from api.models import Todo

today = datetime.today().date()
todo = Todo(description="Run a marathon", due_date=today, completed=False)

print(f"Check: {todo.to_dict()}")

db.session.add(todo)
db.session.commit()
