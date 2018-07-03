#!/usr/local/bin/python3
"""Set up connection to mongodb. Provides a
function to store modem data in the collection.
"""

# import datetime
from pymongo import MongoClient

CLIENT = MongoClient('mongodb://localhost:27017/')
DB = CLIENT.atmc
MODEMS = DB.modem_configs
