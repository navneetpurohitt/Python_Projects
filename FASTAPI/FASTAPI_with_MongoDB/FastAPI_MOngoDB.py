from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection details
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "testdb")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "testcollection")

# Initialize FastAPI app
app = FastAPI()

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Helper function to convert MongoDB documents to JSON
def serialize_document(document):
    document["_id"] = str(document["_id"])
    return document

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with MongoDB"}

@app.get("/items")
def get_items():
    items = list(collection.find())
    return [serialize_document(item) for item in items]

@app.get("/items/{item_id}")
def get_item(item_id: str):
    item = collection.find_one({"_id": ObjectId(item_id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return serialize_document(item)

@app.post("/items")
def create_item(item: dict):
    result = collection.insert_one(item)
    return {"id": str(result.inserted_id)}

@app.put("/items/{item_id}")
def update_item(item_id: str, item: dict):
    result = collection.update_one({"_id": ObjectId(item_id)}, {"$set": item})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item updated successfully"}

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    result = collection.delete_one({"_id": ObjectId(item_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}