import os


MONGDB_ENDPOINT = os.environ.get(
    "MONGDB_ENDPOINT", "mongodb://localhost:27017/")

REDIS_IMAGE = os.environ.get("REDIS_IMAGE", "redis:latest")
