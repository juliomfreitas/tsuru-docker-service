import os


MONGDB_ENDPOINT = os.environ.get(
    "MONGDB_ENDPOINT", "mongodb://localhost:27017/docker_service")

DOCKER_IMAGES = {'redis': "redis:latest"}

DOCKER_ENDPOINT = os.environ.get("DOCKER_ENDPOINT")
