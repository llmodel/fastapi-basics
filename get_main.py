from enum import Enum
from typing import Union
from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"},{"item_name": "Oak"}, {"item_name": "Birch"}, {"item_name": "Cedar"}, {"item_name": "Elm"}, {"item_name": "Fir"}, {"item_name": "Hickory"}, {"item_name": "Ironwood"}, {"item_name": "Oak"}, {"item_name": "Pine"}, {"item_name": "Spruce"}]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

@app.get("/items/{item_id}")
# expecting parameters item_id and q. The default value for q is None, which means that q is optional.
# Example get: http://127.0.0.1:8000/items/foo?q=1
async def read_item(item_id: str, q: Union[int , None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

@app.get("/items/")
# expecting parameters skip and limit. The default values are 0 and 10
async def read_item(skip: int = 0, limit: int = 10):
    # return fake item number from item number skip to item number skip + limit
    return fake_items_db[skip : skip + limit]

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    # compare model_name to the enum members
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    # compare model_name to s string
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}