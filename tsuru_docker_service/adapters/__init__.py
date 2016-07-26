from .redis_adapter import RedisAdapter


adapters_mapping = {'redis': RedisAdapter}


class AdapterNotFound(BaseException):
    pass


def get_adapter(name, **kwargs):
    adapter_class = adapters_mapping.get(name)
    if not adapter_class:
        raise AdapterNotFound("Adapter `{}` does not exists".format(name))

    return adapter_class(**kwargs)
