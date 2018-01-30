# for operate the mongodb database
from pymongo import MongoClient


class Store(object):

    # 初始化数据库连接
    def __init__(self, address, port, database_name):
        self._client = MongoClient(address, port)
        self._db = self._client[database_name]
        self._thread_info = self._db["thread_info"]     # 数据库Collection名字
        self._pic_info = self._db["pic_data"]

    # 按关键字查找帖子，返回帖子信息列表
    def get_threads_by_keyword(self, keyword):
        cursor = self._thread_info.find({"name": {"$regex": ".*" + keyword + ".*"}})
        result = []

        for item in cursor:
            result.append(item)

        return result
