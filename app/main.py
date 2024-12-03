from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# Define another route
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}