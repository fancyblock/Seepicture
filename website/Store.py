# for operate the mongodb database
from pymongo import MongoClient


class Store(object):

    def __init__(self, address, port, database_name):
        self._client = MongoClient(address, port)
        self._db = self._client[database_name]
        #TODO