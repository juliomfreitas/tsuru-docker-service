import re
import pymongo

from . import settings


MONGO_REGEX = r'^mongodb\:\/\/(?P<host>[@:_\.\w]+):(?P<port>\d+)/'\
              '(?P<database>[_\w]+)$'


class BaseModel:

    def _db(self):
        endpoint = settings.MONGODB_ENDPOINT
        client = pymongo.MongoClient(endpoint)

        config = re.compile(MONGO_REGEX).match(endpoint).groupdict()
        return client[config['database']].contaners


class ContainerModel(BaseModel):

    def create_from_adapter(self, adapter):
        self._db().insert_one(adapter.serialize())

    def destroy_from_adapter(self, adapter):
        self._db().delete_one({"container_id": adapter.container_id})

    def get(self, **filters):
        return self._db().find_one(filters)

    def destroy(self, **filters):
        return self._db().remove(filters)
