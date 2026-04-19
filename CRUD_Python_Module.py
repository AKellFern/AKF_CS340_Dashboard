# Example Python Code to Insert a Document

from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d/?authSource=admin' % (username, password, HOST, PORT)
        )
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            try:
                self.collection.insert_one(data)  # data should be dictionary
                return True
            except Exception as e:
                print(f"Error occurred while inserting document: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Read method to implement the R in CRUD
    def read(self, query):
        if query is not None:
            try:
                result = self.collection.find(query)  # query should be dictionary
                return list(result)  # convert cursor to list
            except Exception as e:
                print(f"Error occurred while reading documents: {e}")
                return []
        else:
            raise Exception("Nothing to read, because query parameter is empty")

    # Update method to implement the U in CRUD
    def update(self, query, newData):
        if query is not None and newData is not None:
            try:
                result = self.collection.update_many(query, newData)
                return result.modified_count
            except Exception as e:
                print(f"Error occurred while updating documents: {e}")
                return 0
        else:
            raise Exception("Query or newData parameter is empty")

    # Delete method to implement the D in CRUD
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"Error occurred while deleting documents: {e}")
                return 0
        else:
            raise Exception("Nothing to delete, because query parameter is empty")