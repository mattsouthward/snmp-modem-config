#!/usr/local/bin/python3
"""Set up connection to mongodb. Provides a
function to store modem data in the collection.
"""

# import datetime
from pymongo import MongoClient
import settings

client = MongoClient('mongodb://localhost:27017/')
db = client.atmc
modems = db.modem_configs

def store_record(record):
    """Return id of inserted record."""
    return modems.insert_one(record).inserted_id
