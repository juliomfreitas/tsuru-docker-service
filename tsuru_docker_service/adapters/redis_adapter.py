from .base import BaseAdapter


class RedisAdapter(BaseAdapter):

    """Adapter used to create redis container"""

    name = "redis"