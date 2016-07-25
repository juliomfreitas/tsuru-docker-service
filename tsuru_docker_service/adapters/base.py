import docker
from tsuru_docker_service import settings


class BaseAdapter:
    # Image name used to find the image of the docker containers
    name = None

    def client(self):
        return docker.Client(base_url=settings.DOCKER_ENDPOINT)

    def create_container(self):
        client = self.client()

        response = client.create_container(
            image=settings.DOCKER_IMAGES[self.name],
            host_config=client.create_host_config(publish_all_ports=True))

        self.container_id = response['Id']
        client.start(self.container_id)

    def destroy_container(self):
        client = self.client()
        client.stop(self.container_id)
        client.remove_container(self.container_id)

    def discover_published_port(self):
        client = self.client()
        result = client.inspect_container(self.container_id)

        return result['NetworkSettings']['Ports'].values()[0][0]['HostPort']
