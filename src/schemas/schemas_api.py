from pydantic import BaseModel

class Response (BaseModel):
    '''Json schema for response'''
    num: int
    response: str


class Request (BaseModel):
    '''Json schema for request'''
    num: int
    list: str

