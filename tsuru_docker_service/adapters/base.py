try:
    from urllib.parse import urlparse
except ImportError:
    # Python 2.x
    from urlparse import urlparse

import docker

from tsuru_docker_service import settings


class BaseAdapter:
    # Image name used to find the image of the docker containers
    name = None

    _client = None

    def __init__(self, container_id=None, instance_name=None):
        self.container_id = container_id
        self.instance_name = instance_name

    def client(self):
        if self._client:
            return self._client

        self._client = docker.Client(base_url=settings.DOCKER_ENDPOINT)
        return self._client

    def create_container(self, instance_name=None):
        client = self.client()

        response = client.create_container(
            image=settings.DOCKER_IMAGES[self.name],
            host_config=client.create_host_config(publish_all_ports=True))

        self.container_id = response['Id']
        self.instance_name = instance_name

        client.start(self.container_id)

    def destroy_container(self):
        client = self.client()
        client.stop(self.container_id)
        client.remove_container(self.container_id)

    def discover_published_port(self):
        client = self.client()
        result = client.inspect_container(self.container_id)

        return result['NetworkSettings']['Ports'].values()[0][0]['HostPort']

    def serialize(self):
        return {"adapter": self.name,
                "name": self.name,
                "instance_name": self.instance_name,
                "container_id": self.container_id,
                "port": self.discover_published_port()}

    def get_environment(self):
        raise NotImplementedError()

    def get_host(self):
        return urlparse(settings.DOCKER_ENDPOINT).netloc.split(':')[0]
