import re
import pymongo

from . import settings


MONGO_REGEX = r'^mongodb\:\/\/(?P<host>[@:_\.\w]+):(?P<port>\d+)/'\
              '(?P<database>[_\w]+)$'


class BaseModel:

    def _db(self):
        endpoint = settings.MONGDB_ENDPOINT
        client = pymongo.MongoClient(endpoint)

        config = re.compile(MONGO_REGEX).match(endpoint).groupdict()
        return client[config['database']].contaners


class ContainerModel(BaseModel):

    def create_from_adapter(self, adapter):
        self._db().insert(adapter.serialize())

    def destroy_from_adapter(self, adapter):
        self._db().remove({"container_id": adapter.container_id})
