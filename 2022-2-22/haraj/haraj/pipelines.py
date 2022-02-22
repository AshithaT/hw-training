import pymongo
from pymongo import MongoClient
from scrapy.exceptions import DropItem
from haraj.items import *
from pymongo import MongoClient
from haraj.settings import *


class HarajPipeline:
    def __init__(self, settings):
        self.mongo_uri = settings.get('MONGO_URI')
        self.mongo_db = settings.get('MONGO_DB')
        self.mongo_collection = settings.get('MONGO_COLLECTION')
        self.mongo_collection_url = settings.get('MONGO_COLLECTION_URL')
        self.dup_key = settings.get('DUP_KEY')
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            settings=crawler.settings
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_uri)
        try:
            self.client.admin.command("enablesharding", self.mongo_db)
        except:
            pass
        try:
            self.client.admin.command(
                "shardcollection", self.mongo_db + '.' + self.mongo_collection, key={'profile_url': 1}, unique=True)
        except:
            pass

        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        if isinstance(item, harajItem):
            try:
                self.db[self.mongo_collection].insert_one(dict(item))
            except:
                raise DropItem("Dropping duplicate item")

        return item
       
       
