from fastapi import APIRouter, HTTPException
import logging
from pydantic import BaseModel

class SearchRequest(BaseModel):
    '''Request body for binary search'''
    list: list[int]
    num: int

class BinarySearch:
    '''Binary search class that contains the router and the binary search function''' 
    router: APIRouter = APIRouter()
    logger: logging.Logger

    def __init__(self):
        '''Initializes the logger and adds the binary search route to the router'''
        self.logger = logging.getLogger('default')
        self.router.prefix="/binary"
        self.router.add_api_route("/submit",self.binary_search, methods=["POST"])

    def serialize_json(self, input: SearchRequest, response: str):
        body = {"num": input.num, "response": response}
        return body
    
    async def binary_search(self, request: SearchRequest): 
        self.logger.debug("Binary search request received")
        try: 
            left, right= 0, len(request.list) -1 
            while left <= right:
                middle = (left + right) // 2
                if request.list[middle] < request.num:
                    left = middle + 1
                elif request.list[middle] > request.num:
                    right = middle - 1
                else:
                    return self.serialize_json(request, "Search was successful")
            return self.serialize_json(request, "Search was unsuccessful")
        
        except Exception as e:
            self.logger.error(e)
            raise HTTPException()


        


