"""Beginners introduction to FastAPI"""

from typing import Union

from fastapi import FastAPI
from MockDB import items_db
from ModelName import ModelName

app = FastAPI()


@app.get("/")
async def root():
    """Simple set-up"""
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """Simply return the provided item_id

    Type hint provides automatic data type conversion.
    Error is raised if wrong data type is passed, like string.
    """
    return {"item_id": item_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """Get the name of the model based on the ModelName class"""

    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning model"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/mock_items/")
async def read_mock_item(skip: int = 0, limit: int = 10):
    """
    Any function parameters that are not part of the route are automatically
    considered as "query" parameters.
    The query is the set of key-value pairs that go after ? in a URL and are
    separated by & characters, e.g.
        http://127.0.0.1:8000/items/?skip=0&limit=10
    """

    return items_db[skip : skip + limit]


@app.get("/items_extended/{item_id}")
async def read_item_with_option(item_id: str, query: Union[str, None] = None):
    """
    Pass on additional optional query parameter
    Example: http://127.0.0.1:8000/items_extended/3?q=9
    """
    if query:
        return {"item_id": item_id, "additional": query}
    else:
        return {"item_id": item_id}
