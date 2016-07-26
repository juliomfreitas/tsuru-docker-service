import unittest
import mock

from tsuru_docker_service import api


class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.client = api.app.test_client()

    @mock.patch('tsuru_docker_service.api.get_adapter')
    @mock.patch('tsuru_docker_service.api.ContainerModel')
    def test_add_instance(self, mockedContainerModel, mocked_get_adapter):
        response = self.client.post('/resources', data={"plan": "redis"})

        self.assertTrue(
            mockedContainerModel.return_value.create_from_adapter.called)
        self.assertTrue(
            mocked_get_adapter.return_value.create_container.called)

        self.assertEqual(response.status_code, 201)
