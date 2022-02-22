import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
import json
import datetime

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
    name = 'sakneen'
    allowed_domains = ['sakneen.com']

    def start_requests(self):
        with open('urls.json', 'r') as fp:
            datas = fp.read()
        datas = datas.split("\n")
        for data in datas:
            data = json.loads(data)
            url = data.get('url')
            yield Request(url, method='GET', meta={"url": url}, callback=self.parse, dont_filter=True)

    def parse(self, response):
        meta = response.meta
        TITLE = response.xpath('//h2/text()').extract_first()
        meta['title'] = TITLE
        slug = response.url
        slug = slug.split('/')[-1]
        url = 'https://app.sakneen.com/apis/marketplace/listings/slug/' + \
            str(slug)
        yield Request(url, method='GET', meta=meta, callback=self.parse_data, dont_filter=True)

    def parse_data(self, response):
        meta = response.meta
        nowdate = datetime.now().date()

        v = json.loads(response.text)
        data = v['listing']
        for v in data:
            if data:

                id_ = data.get('id', '')
                photos = data.get('photos', '')
                broker_display_name = ''
                broker = ''
                category = 'buy'
                category_url = ''

                property_type = data.get('unitType')
                depth = ''
                sub_category_1 = ''
                sub_category_2 = ''
                description = data.get('description', '')
                if description:
                    description = description.replace('\n', '').replace(
                        '\r', '').replace('\t', '').replace('\\', '')
                else:
                    description = ''
                location = ''
                price = data.get('totalPrice', '')
                currency = 'EGP'
                price_per = ''
                bedrooms = data.get('bedrooms', '')
                bathrooms = data.get('bathrooms', '')
                furnished = ''
                rera_permit_number = ''
                dtcm_licence = ''
                scraped_ts = nowdate.strftime("%Y_%m_%d")
                amenities = str(data.get('garden', ''))
                if data.get('land'):
                    land = str(data.get('land', '')) + "m2,"
                if data.get('bua'):
                    bua = str(data.get('bua', ''))+"m2"
                details = land+bua
                agent_name = ''
                reference_number = ''
                user_id = ''
                phone_number = data.get('phone', '')
                date = ''
                iteration_number = ''
                latitude = data.get('latitude', '')
                longitude = data.get('longitude', '')

            item = {}
            item = SakneenItem()
            item['id'] = id_
            item['number_of_photos'] = len(photos)
            item['broker_display_name'] = broker_display_name
            item['broker'] = broker
            item['category'] = category
            item['category_url'] = category_url
            item['title'] = meta['title']
            item['property_type'] = property_type
            item['depth'] = depth
            item['sub_category_1'] = sub_category_1
            item['sub_category_2'] = sub_category_2
            item['description'] = description
            item['location'] = location
            item['Price'] = price
            item['currency'] = currency
            item['price_per'] = price_per
            item['bedrooms'] = bedrooms
            item['bathrooms'] = bathrooms
            item['furnished'] = furnished
            item['rera_permit_number'] = rera_permit_number
            item['dtcm_licence'] = dtcm_licence
            item['scraped_ts'] = scraped_ts
            item['aminities'] = amenities
            item['details'] = details
            item['agent_name'] = agent_name

            item['reference_number'] = reference_number
            item['user_id'] = user_id
            item['phone_number'] = phone_number
            item['date'] = scraped_ts
            item['iteration_number'] = iteration_number
            item['latitude'] = latitude
            item['longitude'] = longitude
            # logging.warning(item)

            yield item
