from pymongo import MongoClient


def clase10():
    print("--- CLASE 10: Base Mongo -----------------------------------------------")
    print("--- 01-04-24 -----------------------------------------------------------")

    try:
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)

        # Access database
        db = client['test_database']

        # Access collection
        collection = db['mongo']

        # Insert one document
        collection.insert_one({"name": "Charlie", "age": 40})
        print("Element added successfully!")

        # Add new elements to the collection
        new_elements = [
            {"name": "John", "age": 30},
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 35}
        ]

        # Insert multiple documents
        collection.insert_many(new_elements)
        print("Elements added successfully!")

        # Update one document
        collection.update_one({"name": "Charlie"}, {"$set": {"age": 62}})
        print("Element updated successfully!")

        # Query the collection
        print("Data in the collection: ------------")
        for element in collection.find():
            print(element)
            print("-------------------------")

        # Close the connection
        client.close()
        print("Disconnected from MongoDB")
    except Exception as e:
        print("Error:", e)
        print("Make sure that MongoDB is running on localhost and port 27017")
        print("No se puede ejecutar clase 10 - Iniciar docker con MongoDB")
