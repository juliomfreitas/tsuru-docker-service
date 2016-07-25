import unittest
import mock

from tsuru_docker_service import adapters


class GetAdapterTestCase(unittest.TestCase):

    def test_invalid_adapter(self):
        with self.assertRaises(adapters.AdapterNotFound):
            adapters.get_adapter("foo")

    def test_redis_adapter(self):
        adapter = adapters.get_adapter("redis")
        self.assertTrue(isinstance(adapter, adapters.RedisAdapter))


class CreateContainerTestCase(unittest.TestCase):

    @mock.patch('tsuru_docker_service.adapters.base.docker')
    def test_create_container(self, mock_docker):
        mock_docker.Client = mock.Mock()
        mock_docker.Client.return_value.create_container.return_value = {
            "Id": "id"}

        adapter = adapters.RedisAdapter()
        adapter.create_container()

        self.assertTrue(
            mock_docker.Client.return_value.create_container.called)
        self.assertTrue(
            mock_docker.Client.return_value.start.called)

    @mock.patch('tsuru_docker_service.adapters.base.docker')
    def test_destroy_container(self, mock_docker):
        adapter = adapters.RedisAdapter()
        adapter.container_id = 'id'

        adapter.destroy_container()

        self.assertTrue(
            mock_docker.Client.return_value.remove_container.called)
        self.assertTrue(
            mock_docker.Client.return_value.stop.called)
