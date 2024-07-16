# main.py

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pymongo import MongoClient

load_dotenv()

app = FastAPI()

# MongoDB connection string from environment variable
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI)

# Replace "mydatabase" with your database name
db = client.mydatabase
collection = db.mycollection

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

# Example of a CRUD operation
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    return {"item_id": item_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
