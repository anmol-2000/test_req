from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

#Importing the pydantic schema and the Item model class
from item_api.item_schema import Item, Login
from item_api.item_model import ItemModel
from auth import current_user

router = APIRouter(prefix="/item")

item_model = ItemModel()

@router.post("/auth")
async def auth(login: Login):
    resp = await item_model.auth(login)
    if "error" in resp:
        return JSONResponse(resp, status_code=400)
    return JSONResponse(resp)

@router.post("")
async def create_item(item: Item, userid: str = Depends(current_user)):
    resp = await item_model.create_item(item,userid)
    if "error" in resp:
        return JSONResponse(resp, status_code=400)
    return JSONResponse(resp)

@router.get("")
async def get_item(userid: str = Depends(current_user)):
    resp = await item_model.get_item(userid)
    if "error" in resp:
        return JSONResponse(resp, status_code=400)
    return JSONResponse(resp)

@router.get('/summary')
async def get_summary(userid: str = Depends(current_user)):
    resp = await item_model.get_summray(userid)
    if "error" in resp:
        return JSONResponse(resp, status_code=400)
    return JSONResponse(resp)