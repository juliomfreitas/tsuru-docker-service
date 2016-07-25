import pymongo
from pymongo.errors import ConfigurationError

import settings


class ContainerModel(object):

    @staticmethod
    def _db():
        client = pymongo.MongoClient(settings.MONGDB_ENDPOINT)
        try:
            database = client.get_default_database()
            database_name = database.name
        except ConfigurationError:
            pass

        return client[database_name]

    @staticmethod
    def create(container):
        ContainerModel._db().instances.insert(container.to_json())

    def delete(self, instance):
        ContainerModel._db().instances.remove({"name": instance.name})
