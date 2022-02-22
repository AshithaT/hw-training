import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
import json

from sakneen.items import *
from sakneen.settings import *
# from sakneen.proxy import parse_proxy
from pymongo import MongoClient

headers = {'accept': '*/*',
 'accept-encoding': 'gzip, deflate, br',
 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
 'app-request-origin': 'sakneen-platform',
 'content-type': 'application/json',
 'origin': 'https://www.sakneen.com',
 'referer': 'https://www.sakneen.com/',
 'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
 'sec-ch-ua-mobile': '?0',
 'sec-fetch-dest': 'empty',
 'sec-fetch-mode': 'cors',
 'sec-fetch-site': 'same-site',
 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

class sakneen_Spider(scrapy.Spider):
    # db = MongoClient('mongodb://localhost:27017')[dbname]
    name = 'sakneen_crawler'
    allowed_domains = ['sakneen.com']

    def start_requests(self):
        meta={"page":1}
        payload = {}  
        url = 'https://app.sakneen.com/apis/marketplace/filters/v2?limit=30&page=1'
        yield FormRequest(url=url,method="POST",callback=self.parse_search, meta=meta,body=json.dumps(payload),headers=headers)                                           


    def parse_search(self,response):
        base_url='https://www.sakneen.com/en/house/'
        meta=response.meta
        v=json.loads(response.text)
        
        # print(response.text)
        v=v['data'] 
        if v:
            for data in v:
                url=base_url+str(data['slugEnglish'])
                # print(base_url+str(data['slugEnglish']))
                item=SakneenItem(url=url)
                yield item

        payload = {}  
        url = 'https://app.sakneen.com/apis/marketplace/filters/v2?limit=30&page='+str(meta['page']+1)
        
        meta={"page":meta['page']+1}
        if meta['page']<= 34:
            yield FormRequest(url=url,method="POST",callback=self.parse_search, meta=meta,body=json.dumps(payload),headers=headers)
    
    
        