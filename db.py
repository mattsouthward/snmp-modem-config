#!/usr/local/bin/python3
"""Set up connection to mongodb. Provides a
function to store modem data in the collection.
"""

# import datetime
from pymongo import MongoClient

CLIENT = MongoClient('mongodb://localhost:27017/')
DB = CLIENT.atmc
MODEMS = DB.modem_configs

# def store_doc(doc):
#     """Return id of inserted record."""
#     return MODEMS.insert_one(doc).inserted_id

# def find_doc(mac_addr):
#     """Return True if document was found else False."""
#     return MODEMS.find({"MAC Address": mac_addr}).count()
