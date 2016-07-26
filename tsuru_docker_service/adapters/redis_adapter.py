from .base import BaseAdapter


class RedisAdapter(BaseAdapter):

    """Adapter used to create redis container"""

    name = "redis"

    def get_environment(self):
        return {"REDIS_HOST": self.get_host(),
                "REDIS_PORT": self.discover_published_port()}
