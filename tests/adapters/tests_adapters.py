import unittest
from tsuru_docker_service import adapters


class GetAdapterTestCase(unittest.TestCase):

    def test_invalid_adapter(self):
        with self.assertRaises(adapters.AdapterNotFound):
            adapters.get_adapter("foo")

    def test_redis_adapter(self):
        adapter = adapters.get_adapter("redis")
        self.assertTrue(isinstance(adapter, adapters.RedisAdapter))
