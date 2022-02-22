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
		meta={'page':1}
		query = {"query":"query($tag:String,$page:Int) { posts( tag:$tag, page:$page) {\n\t\titems {\n\t\t\tid status authorUsername title city postDate updateDate hasImage thumbURL authorId bodyTEXT city tags imagesList commentStatus commentCount upRank downRank geoHash geoCity geoNeighborhood\n\t\t}\n\t\tpageInfo {\n\t\t\thasNextPage\n\t\t}\n\t\t} }","variables":{"tag":"حراج العقار","page":1}}
		url='https://graphql.haraj.com.sa/?queryName=detailsPosts_tag_page1'
		yield Request(url, callback=self.parse_search, method="POST",meta=meta, body=json.dumps(query),dont_filter=True)

	def parse_search(self,response):
		meta=response.meta
		base_url="https://haraj.com.sa/"
		v=(json.loads(response.text)).get('data',{})
		items=v.get('posts',{}).get('items',[])
		for item in items:
			id=item.get('id','')
			title=item.get('title','').replace(' ','_')
			url=base_url+'11'+str(id)+'/'+str(title)
			item=harajItem()
			item['url']=url
			yield item

		meta['page']=meta['page']+1
		query = {"query":"query($tag:String,$page:Int) { posts( tag:$tag, page:$page) {\n\t\titems {\n\t\t\tid status authorUsername title city postDate updateDate hasImage thumbURL authorId bodyTEXT city tags imagesList commentStatus commentCount upRank downRank geoHash geoCity geoNeighborhood\n\t\t}\n\t\tpageInfo {\n\t\t\thasNextPage\n\t\t}\n\t\t} }","variables":{"tag":"حراج العقار","page":meta['page']}}
		url='https://graphql.haraj.com.sa/?queryName=detailsPosts_tag_page'+str(meta['page'])
		yield Request(url, callback=self.parse_search, method="POST",meta=meta, body=json.dumps(query),dont_filter=True)




