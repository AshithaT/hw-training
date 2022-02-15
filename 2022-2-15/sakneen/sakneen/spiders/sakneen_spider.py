import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
# from sakneen.items import *
# from sakneen.settings import *
# from sakneen.proxy import parse_proxy
from pymongo import MongoClient

headers = {'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
'content-length': '112',
'content-type': 'text/plain; charset=UTF-8',
'origin': 'https://www.sakneen.com',
'referer': 'https://www.sakneen.com/',
'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'cross-site',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

class sakneen_Spider(scrapy.Spider):
    name = 'sakneen'
    start_urls = ['https://www.sakneen.com/en']
    def start_requests(self):
    	yield scrapy.Request(
         url=self.start_url,
         callback=self.parse_product_url,
         headers=self.headers,
         dont_filter=True,
         meta={"villa-for-sale-greater-cairo-giza-sheikh-zayed-city-al-rabwa-647bdf4115d74201b12ebcdd945ac496": 1}
        )
    