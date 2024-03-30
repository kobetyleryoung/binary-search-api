from fastapi import FastAPI
from router.router import BinarySearch

app = FastAPI()

binary_search = BinarySearch()
app.include_router(binary_search.router)