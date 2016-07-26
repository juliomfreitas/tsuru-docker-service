import unittest
import mongomock

from tsuru_docker_service import model, adapters


class ContainerModelTestCase(unittest.TestCase):

    def test_create_from_adapter(self):
        adapter = adapters.RedisAdapter()
        adapter.container_id = 'dummy'
        adapter.instance_name = 'my dummy instance'
        adapter.discover_published_port = lambda: 6379

        containers = mongomock.MongoClient().db.containers
        container = model.ContainerModel()
        container._db = lambda: containers

        self.assertEqual(containers.count(), 0)
        container.create_from_adapter(adapter)
        self.assertEqual(containers.count(), 1)

        created = containers.find_one()
        self.assertEqual(created['port'], 6379)
        self.assertEqual(created['adapter'], "redis")
        self.assertEqual(created['container_id'], "dummy")

    def test_destroy_from_adapter(self):
        adapter = adapters.RedisAdapter()
        adapter.container_id = 'dummy'
        adapter.instance_name = 'my dummy instance'
        adapter.discover_published_port = lambda: 6379

        containers = mongomock.MongoClient().db.containers
        container = model.ContainerModel()
        container._db = lambda: containers

        container.create_from_adapter(adapter)
        self.assertEqual(containers.count(), 1)
        container.destroy_from_adapter(adapter)
        self.assertEqual(containers.count(), 0)
