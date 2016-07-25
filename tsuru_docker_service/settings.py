import os

MONGDB_ENDPOINT = os.environ.get(
    "MONGDB_ENDPOINT", "mongodb://localhost:27017/")
