"""Defining the Request Model of the Payload"""
from pydantic import BaseModel


class Item(BaseModel):
    item_name: str
    item_price: float

class Login(BaseModel):
    userid: str
    password: str