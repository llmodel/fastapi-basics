# from typing import Union # not needed for python 3.10 of later

from fastapi import FastAPI
from pydantic import BaseModel


# item class is inherited from BaseModel
class Item(BaseModel):
    name: str
    # description: Union[str, None] = None
    description: str | None = None
    price: float
    # tax: Union[float, None] = None
    tax: float | None = None


app = FastAPI()

##### REQUEST BODY #####
##### POST METHOD #####
#####
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    # if tax is present, add it to the price and store it in price_with_tax key:value pair
    # and return the updated dictionary as response
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


##### REQUEST BODY + PATH PARAMETER #######
##### PUT METHOD #####
# #####
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

##### REQUEST BODY + PATH PARAMETER + QUERY PARAM #######
##### PUT METHOD #####
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result

# python >= 3.10
@app.put("/items/{item_id}")
## item_id is a path parameter
## item is a request body
## q (optional) is a query parameter in the url path
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result