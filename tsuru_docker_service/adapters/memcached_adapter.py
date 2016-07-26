from .base import BaseAdapter


class MemcachedAdapter(BaseAdapter):

    """Adapter used to create memcached container"""

    name = "memcached"

    def get_environment(self):
        return {"MEMCACHED_HOST": self.get_host(),
                "MEMCACHED_PORT": self.discover_published_port()}
