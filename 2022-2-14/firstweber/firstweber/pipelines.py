# -*- coding: utf-8 -*-
import pymongo
from scrapy.exceptions import DropItem
from firstweber.items import *
from pymongo import MongoClient
from datetime import datetime
from firstweber.settings import *
# from databasenotifier import automation_script


class FirstweberPipeline(object):

    def __init__(self, settings):
        self.mongo_uri = settings.get('MONGO_URI')
        self.mongo_db = settings.get('MONGO_DB')
        self.mongo_collection = settings.get('MONGO_COLLECTION')
        # self.mongo_collection_url = settings.get('MONGO_COLLECTION_URL')
        self.dup_key = settings.get('DUP_KEY')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            settings=crawler.settings
        )

    def open_spider(self, spider):
        # self.client = pymongo.MongoClient(self.mongo_uri)
        # self.db = self.client[self.mongo_db]
        # if self.dup_key:
        #     self.db[self.mongo_collection].create_index(
        #         self.dup_key, unique=True)
        self.client = MongoClient(self.mongo_uri)
        try:
            self.client.admin.command("enablesharding", self.mongo_db)
        except:
            pass
        # try:
        #     self.client.admin.command(
        #         "shardcollection", self.mongo_db + '.' + self.mongo_collection_url, key={'_id': 1})
        # except:
        #     pass

        try:
            self.client.admin.command(
                "shardcollection", self.mongo_db + '.' + self.mongo_collection, key={'profile_url': 1})
        except:
            pass

        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        if isinstance(item, FirstweberItem):
            try:
                self.db[self.mongo_collection].insert(dict(item))
            except:
                raise DropItem("Dropping duplicate item")
        if isinstance(item, FirstweberUrlItem):
            try:
                self.db[self.mongo_collection_url].insert(dict(item))
            except:
                raise DropItem("Dropping duplicate item")
        return item

    # def close_spider(self, spider):
    #     automation_script.Automation_Spider(
    #         self.mongo_db, self.mongo_collection)
    #     self.client.close()
