import pymongo
import pandas as pd
import numpy as np
import json
import os, sys
from dataclasses import dataclass

#client = pymongo.MongoClient("mongodb+srv://vaishnavi:mongodbpassword@cluster0.7ruwl8u.mongodb.net/?retryWrites=true&w=majority")
@dataclass
class EnvironmentVariable:
    mongo_db_url = os.getenv("MONGO_DB_URL")


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = 'expenses'
print(env_var.mongo_db_url)

