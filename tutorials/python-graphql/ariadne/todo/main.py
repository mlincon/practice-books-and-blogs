from ariadne import (
    ObjectType,
    graphql_sync,
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)
from ariadne.constants import PLAYGROUND_HTML
from flask import jsonify, request
from todo.api import app
from todo.api.mutations import (
    resolve_create_todo,
    resolve_delete_todo,
    resolve_mark_done,
    resolve_update_due_date,
)
from todo.api.queries import resolve_todo, resolve_todos

query = ObjectType("Query")

query.set_field("todos", resolve_todos)
query.set_field("todo", resolve_todo)

mutation = ObjectType("Mutation")
mutation.set_field("createTodo", resolve_create_todo)
mutation.set_field("markDone", resolve_mark_done)
mutation.set_field("deleteTodo", resolve_delete_todo)
mutation.set_field("updateDueDate", resolve_update_due_date)

type_defs: str = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs,
    query,
    mutation,
    snake_case_fallback_resolvers,  # type: ignore (pylance error)
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code
