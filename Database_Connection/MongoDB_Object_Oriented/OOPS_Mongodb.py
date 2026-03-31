from pymongo import MongoClient

class MongoDBHandler:
    def __init__(self, uri, database_name, collection_name):
        self.client = MongoClient(uri)
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def create_document(self, document):
        result = self.collection.insert_one(document)
        return result.inserted_id

    def read_documents(self, query=None):
        if query is None:
            query = {}
        return list(self.collection.find(query))

    def update_document(self, query, update_values):
        result = self.collection.update_one(query, {'$set': update_values})
        return result.modified_count

    def delete_document(self, query):
        result = self.collection.delete_one(query)
        return result.deleted_count

# Example usage:
if __name__ == "__main__":
    uri = "mongodb://localhost:27017/"
    database_name = "test_db"
    collection_name = "test_collection"

    db_handler = MongoDBHandler(uri, database_name, collection_name)

    # Create a document
    document = {"name": "John Doe", "age": 30, "city": "New York"}
    print("Inserted ID:", db_handler.create_document(document))

    # Read documents
    print("Documents:", db_handler.read_documents())

    # Update a document
    query = {"name": "John Doe"}
    update_values = {"age": 31}
    print("Modified Count:", db_handler.update_document(query, update_values))

    # Delete a document
    print("Deleted Count:", db_handler.delete_document(query))