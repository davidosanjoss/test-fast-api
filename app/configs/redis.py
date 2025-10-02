import redis.asyncio as aioredis

from .settings import settings

REDIS_URL = settings.REDIS_URL
conn_redis = aioredis.from_url(
    REDIS_URL,
    encoding="utf-8",
    decode_responses=True,
)


class RedisClass:
    conn = conn_redis

    @staticmethod
    async def get_cache(key: str):
        return await conn_redis.get(key)

    @staticmethod
    async def set_cache(key: str, value: str, expire: int = 60):
        await conn_redis.set(key, value, ex=expire)


redis = RedisClass()
