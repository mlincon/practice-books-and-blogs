from todo.api import app, db
from todo.api import models

from ariadne import load_schema_from_path
from ariadne import make_executable_schema
from ariadne import graphql_sync
from ariadne import snake_case_fallback_resolvers
from ariadne import ObjectType
from ariadne.constants import PLAYGROUND_HTML

from flask import request
from flask import jsonify

from todo.api.queries import resolve_todos


query = ObjectType("Query")

query.set_field("todos", resolve_todos)

type_defs: str = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers # type: ignore (pylance error)
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code