from fastapi import APIRouter, HTTPException
import logging
import json


from src.schemas.schemas_api import Response, Request 


class BinarySearch: 
    router: APIRouter = APIRouter()
    logger: logging.Logger

    def __init__(self):
        self.logger = logging.getLogger('debug')
        self.router.prefix="/binary"
        self.router.add_api_route("/submit",self.binary_search, methods=["POST"])

    def serialize_json(input: Request, response):
                body = Response
                body.num = input.num
                body.response = response   
    try: 
        async def binary_search(request: Request) -> int:
       
            left, right= 0, len(request.list)
            while right > left:
                middle = (left + right) // 2
                if request.list[middle] > request.num:
                    right = middle
                elif request.list[middle] <= request.num:
                    left = middle + 1
                else:
                    serialize_json(request, "Search was successful")
                    return request
            return None

        if binary_search is not None:
            def serialize_json(input: Request):
                body = Response
                body.num = input.num
                body.response = "The search was successful"
        else: 
            def serialize_json(input:Request): 
                body = Response
                body.num = None
                body.response = "The search was unsuccessful"

    except Exception as e:
        self.logger.error(e)
        raise HTTPException()


        


