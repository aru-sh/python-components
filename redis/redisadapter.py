import redis

# r=redis.Redis(
#     host='0.0.0.0',
#     port=6379
# )

# example of using adapter
# r.set('foo', 'bar')
# value = r.get('foo')
# print(value)

# Helper class around redis


class RedisBaseAdapter:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.client = None
        self._initialize_client()

    def _initialize_client(self):
        self.client = redis.Redis(
            host='0.0.0.0',
            port=6379
        )

    def get(self, key):
        return self.client.get(key)

    def set(self, key, value):
        return self.client.set(key, value)
    

tu