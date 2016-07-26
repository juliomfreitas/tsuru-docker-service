import os


MONGODB_ENDPOINT = os.environ["MONGODB_ENDPOINT"]

DOCKER_IMAGES = {'redis': 'redis:latest',
                 'memcached': 'memcached:latest'}

DOCKER_ENDPOINT = os.environ["DOCKER_ENDPOINT"]
