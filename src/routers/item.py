from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from src.models.item import Item
from src.config.index import mongo_config

router = APIRouter()

item_collection = mongo_config.db.get_collection("items")

def item_helper(item) -> dict:
    return {
        "name": item["name"],
        "description": item.get("description"),
        "price": item["price"],
        "available": item["available"]
    }

@router.post("/", response_description="Add new item")
async def create_item(item: Item = Body(...)):
    item = jsonable_encoder(item)
    new_item = item_collection.insert_one(item)
    created_item = item_collection.find_one({"_id": new_item.inserted_id})
    return item_helper(created_item)

@router.get("/", response_description="List all items")
async def get_items():
    items = []
    async for item in item_collection.find():
        items.append(item_helper(item))
    return items

@router.get("/{id}", response_description="Get a single item")
async def get_item(id: str):
    item = item_collection.find_one({"_id": ObjectId(id)})
    if item:
        return item_helper(item)
    raise HTTPException(status_code=404, detail=f"Item {id} not found")

@router.put("/{id}", response_description="Update an item")
async def update_item(id: str, item: Item = Body(...)):
    item = {k: v for k, v in item.dict().items() if v is not None}
    if len(item) < 1:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    item_found = item_collection.find_one({"_id": ObjectId(id)})
    if item_found:
        updated_item = item_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": item}
        )
        if updated_item.modified_count == 1:
            return item_collection.find_one({"_id": ObjectId(id)})
    raise HTTPException(status_code=404, detail=f"Item {id} not found")

@router.delete("/{id}", response_description="Delete an item")
async def delete_item(id: str):
    item = item_collection.find_one({"_id": ObjectId(id)})
    if item:
        item_collection.delete_one({"_id": ObjectId(id)})
        return {"message": f"Item {id} is successfully deleted"}
    raise HTTPException(status_code=404, detail=f"Item {id} not found")
