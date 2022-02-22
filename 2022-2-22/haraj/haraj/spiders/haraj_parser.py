import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
import json

from haraj.items import *
from haraj.settings import *
# from sakneen.proxy import parse_proxy
from pymongo import MongoClient

headers = {'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
'content-length': '287',
'content-type': 'text/plain; charset=utf-8',
'origin: https':'//haraj.com.sa',
'referer': 'https://haraj.com.sa/',
'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'trackid': 'eyJ0YWciOiLYrdix2KfYrCDYp9mE2LnZgtin2LEifQ==',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

class HarajSpider(scrapy.Spider):
	# db = MongoClient('mongodb://localhost:27017')[dbname]
	name = 'haraj'
	allowed_domains = ['haraj.com.sa']

	def start_requests(self):
		meta={}
		url='https://haraj.com.sa/1189493263/ارض_علان_18_بالحناكيه_المدينه'
		id=url.split('/')[-2]
		id=id[2:]
		meta['id']=id

		query={"query":"query postLikeInfo_postContact($id: Int!, $token: String,$postId: Int!) {\n\t\t\n\t\tpostLikeInfo(id: $id, token: $token)\n\t\t{ \n                    isLike\n                    total\n                    isFollowing\n                     }\n\t\n\r\n\t\tpostContact(postId: $postId)\n\t\t{ \n                    contactText\n                    contactMobile\n                     }\n\t\n\t}","variables":{"id":int(id),"token":"","postId":int(id)}}
		url='https://graphql.haraj.com.sa/?queryName=postLikeInfo,postContact'
		yield Request(url, callback=self.parse_data, method="POST",meta=meta, body=json.dumps(query),dont_filter=True)


	def parse_data(self,response):
		meta=response.meta
		# print(meta)
		v=json.loads(response.text)
		phone_no=v.get('data',{}).get('postContact',{}).get('contactMobile')
		meta['phone_no']=phone_no
		# print(phone_no)
		







