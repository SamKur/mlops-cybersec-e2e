from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os, sys
from dotenv import load_dotenv
load_dotenv()
mongodb_uri = os.getenv("MONGODB_URI")

import certifi
ca = certifi.where()    # Get path to CA cert file

import numpy as np
import pandas as pd
import json

# Importing necessary custom modules
from networksecurity.utils.exception import NetworkSecurityException
from networksecurity.utils.logger import logging

# Create a new client and connect to the server
# Use a trusted certificate authority list to verify MongoDB’s TLS (https connection) certificate to prevent MITM attacks


# Send a ping to confirm a successful connection

class NetworkDataExtract:
    def __init__(self):
        try:
            self.client = MongoClient(mongodb_uri, server_api=ServerApi('1'), tlsCAFile=ca)
            logging.info("MongoDB client initialized.")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.to_json(orient="records")))
            logging.info(f"Converted {len(records)} records from CSV to JSON.")
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection): # collection is like table in SQL
        try:
            db = self.client[database]
            coll = db[collection]
            result = coll.insert_many(records)
            logging.info(f"Inserted {len(result.inserted_ids)} records to MongoDB.")
            return len(result.inserted_ids)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':              # Execution of my ETL pipeline
    FILE_PATH = "data/phisingData.csv"  # Use forward slash for cross-platform
    DATABASE = "NetworkSecurityDataBase"
    COLLECTION = "NetworkData"

    try:
        extractor = NetworkDataExtract()
        records = extractor.csv_to_json_convertor(FILE_PATH)
        print(f"Sample record:\n{records[0]}")
        count = extractor.insert_data_mongodb(records, DATABASE, COLLECTION)
        print(f"✅ Total records inserted: {count}")
    except Exception as e:
        print("❌ Insertion failed:", str(e))