import unittest
import mock
import json

from tsuru_docker_service import api
from tsuru_docker_service.adapters import adapters_mapping


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.client = api.app.test_client()

    @mock.patch('tsuru_docker_service.api.get_adapter')
    @mock.patch('tsuru_docker_service.api.ContainerModel')
    def test_add_instance(self, mockedContainerModel, mocked_get_adapter):
        response = self.client.post(
            '/resources', data={"plan": "redis", "name": "my-redis-server"})

        self.assertTrue(
            mockedContainerModel.return_value.create_from_adapter.called)
        self.assertTrue(
            mocked_get_adapter.return_value.create_container.called)

        self.assertEqual(response.status_code, 201)

    @mock.patch('tsuru_docker_service.api.get_adapter')
    @mock.patch('tsuru_docker_service.api.ContainerModel')
    def test_destroy_instance(self, mockedContainerModel, mocked_get_adapter):
        response = self.client.delete(
            '/resources/my-redis-server')

        must_be_called = [
            mockedContainerModel.return_value.get.called,
            mockedContainerModel.return_value.destroy.called,
            mocked_get_adapter.return_value.destroy_container.called,
        ]
        self.assertTrue(all(must_be_called))
        self.assertEqual(response.status_code, 200)

    def test_get_plans(self):
        response = self.client.get('/resources/plans')

        plans_description = json.loads(response.data.decode('utf-8'))

        self.assertEqual([plan["name"] for plan in plans_description],
                         list(adapters_mapping.keys()))
