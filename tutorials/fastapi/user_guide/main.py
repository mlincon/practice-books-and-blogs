from fastapi import FastAPI

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
        return {
            "model_name": model_name,
            "message": "Deep Learning model"
        }
    elif model_name.value == "lenet":
        return {
            "model_name": model_name,
            "message": "LeCNN all the images"
        }
    else:
        return {
            "model_name": model_name,
            "message": "Have some residuals"
        }

