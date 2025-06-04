from pymongo import MongoClient

# MongoDB connection setup
def connect_to_mongo(uri, db_name, collection_name):
    client = MongoClient(uri)
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Create operation
def create_document(collection, document):
    result = collection.insert_one(document)
    print(f"Document inserted with ID: {result.inserted_id}")

# Read operation
def read_documents(collection, query=None):
    query = query or {}
    documents = collection.find(query)
    for doc in documents:
        print(doc)

# Update operation
def update_document(collection, query, update_values):
    result = collection.update_one(query, {"$set": update_values})
    print(f"Matched {result.matched_count} document(s), Modified {result.modified_count} document(s)")

# Delete operation
def delete_document(collection, query):
    result = collection.delete_one(query)
    print(f"Deleted {result.deleted_count} document(s)")

if __name__ == "__main__":
    # MongoDB connection details
    uri = "mongodb://localhost:27017/"
    db_name = "test_db"
    collection_name = "test_collection"

    # Connect to MongoDB
    collection = connect_to_mongo(uri, db_name, collection_name)

    # Example CRUD operations
    # Create
    create_document(collection, {"name": "Alice", "age": 25, "city": "New York"})

    # Read
    print("Documents in collection:")
    read_documents(collection)

    # Update
    update_document(collection, {"name": "Alice"}, {"age": 26})

    # Delete
    delete_document(collection, {"name": "Alice"})