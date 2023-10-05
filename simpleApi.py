# Install FastAPI and Uvicorn
# Import FastAPI and create an instance of the FastAPI class
from fastapi import FastAPI
import os
app = FastAPI()

# Define a route that responds to the root URL ("/")
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# Define a route that accepts POST requests at "/items/"
@app.post("/items/")
async def create_item(item: dict):
    return {"item": item}
if __name__ == '__main__':
    from uvicorn import run
    hostval = '0.0.0.0'
    port1 = int(os.environ.get('PORT_APP1', 5000))
    run(app, host=hostval, port=port1)