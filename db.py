#!/usr/local/bin/python3
"""Set up connection to mongodb. Provides a
function to store modem data in the collection.
"""

# import datetime
from pymongo import MongoClient

CLIENT = MongoClient('mongodb://localhost:27017/')
DB = CLIENT.atmc
MODEMS = DB.modem_configs

def check_index(key):
    """Return truth of the existance of an index named key."""
    indexes = MODEMS.list_indexes()
    return key in indexes

def create_index(key):
    """Create an index named key."""
    return MODEMS.create_index(key, unique=True, background=True)