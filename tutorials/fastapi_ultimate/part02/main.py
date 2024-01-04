from typing import Union

from fastapi import APIRouter, FastAPI, status
from recipes import RECIPES

# instantiate FastAPI app
app = FastAPI()

# allows to group API endpoints, specify versions and other configs
api_router = APIRouter()


# route definition. If everything goes well, the specified status_code is used
# in the response. Default is 200. Depending on context, other status code like
# 201 or 204, etc. can be used.
@api_router.get("/", status_code=status.HTTP_200_OK)
def root() -> dict:
    """Root GET"""
    return {"msg": "Hello World"}


# curly braces indicate the parameter value
@api_router.get("/recipe/{recipe_id}", status_code=status.HTTP_200_OK)
def fetch_recipe(recipe_id: int) -> Union[dict, None]:
    """Fetch a single recipe by ID"""
    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if result:
        return result[0]


# register the router
app.include_router(api_router)

# run the app
if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
