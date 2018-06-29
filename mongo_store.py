#!/usr/local/bin/python3
"""Set up connection to mongodb. Provides a
function to store modem data in the collection.
"""

# import datetime
from pymongo import MongoClient

CLIENT = MongoClient('mongodb://localhost:27017/')
DB = CLIENT.atmc
MODEMS = DB.modem_configs

def store_record(record):
    """Return id of inserted record."""
    return MODEMS.insert_one(record).inserted_id
