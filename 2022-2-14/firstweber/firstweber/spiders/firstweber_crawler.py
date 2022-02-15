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
#     name = 'firstweber_crawler'
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
#                 url = 'https://www.firstweber.com/vp/AgentServlet'
#                 headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#                            'accept-encoding': 'gzip, deflate',
#                            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#                            'upgrade-insecure-requests': '1',
#                            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
#                            }

#                 formdata = {'fg_SummaryCntl': 'TRUE',
#                             'SITE': 'FIRSTWEBER',
#                             'ScreenID_Cur': 'SEARCH_AGENTS_P',
#                             'ScreenID': 'AgentsSummary_Public',
#                             'ScreenID_Alt': 'AGENT_DETAIL_P',
#                             'fg_PublicWebPage': 'Y',
#                             'Search': 'Search',
#                             'A_FG_ACTIVE': 'Y',
#                             'A_FG_PUBLICWEBPAGE': 'Y',
#                             'A_CD_COMPANY': 'FIRSTWEBER',
#                             'A_CD_AGENT': '',
#                             'context': 'SEARCH_AGENTS_P_SEARCH',
#                             'AGENT_NAME': '',
#                             'A_CD_OFFICE': office,
#                             'A_DS_LANGUAGES': '',
#                             'A_DS_CREDITS': '',
#                             'submit': 'View+agents'}

#                 yield FormRequest(url=url, headers=headers, formdata=formdata, callback=self.parse_urls)

#     def parse_urls(self, response):
#         Profile_link = response.xpath('//h3/a/@href').extract()
#         for link in Profile_link:
#             agent_url = response.urljoin(link)
#             # meta = {'url': agent_url}
#             # db.firstweber_urls.insert(dict(meta))
#             item = FirstweberUrlItem()
#             item['url'] = agent_url
#             yield item
#         # automation_script.Automation_Spider(MONGO_DB, MONGO_COLLECTION_URL)
