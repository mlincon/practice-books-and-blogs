#### Source

https://www.twilio.com/blog/graphql-api-python-flask-ariadne

#### Struture

Generated via `tree -I '__pycache__'`

```
.
├── readme.md
└── todo
    ├── api
    │   ├── __init__.py
    │   ├── models.py
    │   ├── mutations.py
    │   └── queries.py
    ├── db_init.py
    ├── __init__.py
    ├── main.py
    ├── requirements.txt
    ├── schema.graphql
    └── todo.db
```

#### Start

To start first create environment variable for Flask:

```bash
export FLASK_APP=main.py
flask run
```

To open GraphQL Playground, go to `http://127.0.0.1:5000/graphql`

#### Queries

Fetch all:

```graphql
query fetchAllTodos {
  todos {
    success
    errors
    todos {
      description
      completed
      id
    }
  }
}
```

Fetch one item:

```graphql
query fetchTodo {
  todo(todoId: "1") {
    success
    errors
    todo {
      id
      completed
      description
      dueDate
    }
  }
}
```

#### Mutations

Create entry

```graphql
mutation newTodo {
  createTodo(description: "Go to the dentist", dueDate: "24-10-2020") {
    success
    errors
    todo {
      id
      completed
      description
    }
  }
}
```

Mark Done

```graphql
mutation markDone {
  markDone(todoId: "1") {
    success
    errors
    todo {
      id
      completed
      description
      dueDate
    }
  }
}
```

Delete item

```graphql
mutation {
  deleteTodo(todoId: "1") {
    success
    errors
  }
}
```

Update due date

```graphql
mutation updateDueDate {
  updateDueDate(todoId: "2", newDate: "25-10-2020") {
    success
    errors
  }
}
```
