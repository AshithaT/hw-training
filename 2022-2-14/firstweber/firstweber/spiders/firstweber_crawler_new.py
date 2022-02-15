# # -*- coding: utf-8 -*-
# import scrapy
# import re
# import pika
# import json
# import logging

# from scrapy.spiders import Spider
# from scrapy.selector import Selector
# from scrapy.http import Request, FormRequest
# from firstweber.items import *
# from firstweber.settings import *
# # from databasenotifier import automation_script
# from firstweber.proxy import parse_proxy
# from scrapy import signals
# from slacker import Slacker
# from pymongo import MongoClient
# from datetime import datetime


# class FirstweberUrlSpider(Spider):
#     name = 'firstweber_crawler_new'
#     start_urls = [
#         'https://www.firstweber.com/find-wisconsin-real-estate-agent']
#     allowed_domains = []

#     def parse(self, response):

#         # GRAB XPATH
#         OFFICE_XPATH = '//select[@id="A_CD_OFFICE"]/option/@value'

#         # FETCHING XPATH
#         office_name = response.xpath(OFFICE_XPATH).extract()

#         # FORMDATA PASSING
#         for office in office_name:
#             if office != '':
#                 url = 'https://www.firstweber.com/vp/DisplayServlet?SITE=FIRSTWEBER&SCREENID=OFFICE_DETAIL&MS_CONTEXT=DC_OFFICE_DETAIL_VIEW&cd_Office=' + \
#                     str(office)
#                 headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#                            'accept-encoding': 'gzip, deflate',
#                            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#                            'upgrade-insecure-requests': '1',
#                            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
#                            }

#                 yield Request(url=url, headers=headers, callback=self.parse_urls)

#     def parse_urls(self, response):
#         Profile_link = response.xpath(
#             '//div[@class="agents_list"]//div[@class="portrait"]/a/@href').extract()
#         for link in Profile_link:
#             agent_url = response.urljoin(link)
#             # meta = {'url': agent_url}
#             # db.firstweber_urls.insert(dict(meta))
#             item = FirstweberUrlItem()
#             item['url'] = agent_url
#             yield item
