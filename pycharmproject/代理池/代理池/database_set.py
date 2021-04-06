MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

import redis
from random import choice

class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        """

        :param host:
        :param port:
        :param password:
        """
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)

    def add(self,proxy,score=INITIAL_SCORE):
        """
        添加代理，设置分数为最高
        :param port:
        :param score:
        :return:
        """
        if not self.db.zscore(REDIS_KEY,proxy):
            return self.db.zadd(REDIS_KEY,score,proxy)

    def random(self):
        """
        随机获取有效代理，首先尝试最高分数代理，如果最高分数不存在，按照排名获取，否则异常
        :return:
        """
        result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY,0,100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError



