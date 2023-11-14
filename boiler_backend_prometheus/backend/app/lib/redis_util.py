import redis
from datetime import timedelta, datetime
from typing import Union

class RedisClient:
    def __init__(self, host='redis', port=6379,password='devpassword', db=0):
        self.redis_client = redis.Redis(host=host, port=port, db=db, password=password, decode_responses=True)

    def set(self, key, value):
        self.redis_client.set(key, value)

    def get(self, key):
        value = self.redis_client.get(key)
        if value is not None:
            return value
        return None

    def exists(self, key):
        return self.redis_client.exists(key)

    def delete(self, key):
        self.redis_client.delete(key)
    
    def setTime(self, key, value, timeout):
        self.redis_client.set(key, value, timedelta(milliseconds=timeout))
    
    def calculate_ttl(expire: Union[int, timedelta]) -> int:
        if isinstance(expire, timedelta):
            expire = int(expire.total_seconds())
        return min(expire)
