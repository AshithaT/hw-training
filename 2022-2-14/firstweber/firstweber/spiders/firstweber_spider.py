# -*- coding: utf-8 -*-
import scrapy
import re
import pika
import json
import logging
# from dateutil import parser
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request, FormRequest
from firstweber.items import *
from firstweber.settings import *
from firstweber.proxy import parse_proxy
from pymongo import MongoClient
from datetime import datetime

handler = logging.FileHandler('spider_error.log')
handler.setLevel('ERROR')
logging.root.addHandler(handler)
logger = logging.getLogger('pika')
logger.propagate = False

headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'accept-encoding': 'gzip, deflate',
           'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
           }


class FirstweberSpider(Spider):
    name = 'firstweber'
    start_urls = [
        'https://www.firstweber.com/find-wisconsin-real-estate-agent']

    def parse(self, response):
        OFFICE_XPATH = '//select[@id="A_CD_OFFICE"]/option/@value'
        office_name = response.xpath(OFFICE_XPATH).extract()
        for office in office_name:
            if office != '':
                url = 'https://www.firstweber.com/vp/DisplayServlet?SITE=FIRSTWEBER&SCREENID=OFFICE_DETAIL&MS_CONTEXT=DC_OFFICE_DETAIL_VIEW&cd_Office=' + \
                    str(office)
                headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                           'accept-encoding': 'gzip, deflate',
                           'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                           'upgrade-insecure-requests': '1',
                           'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
                           }

                yield Request(url=url, headers=headers, callback=self.parse_urls)

    def parse_urls(self, response):
        office_phone_num = []
        office_phn = response.xpath('//div[@class="phone"]/p/text()').extract()
        for number in office_phn:
            if 'Phone:' in number:
                office_phone_num = number.replace(
                    'Phone:', '').replace('Work Fax:', '').replace('eFax', '').strip()
        office_phone_num = [office_phone_num] if office_phone_num else []
        meta = {'office_phone_numbers': office_phone_num}

        Profile_link = response.xpath(
            '//div[@class="agents_list"]//div[@class="portrait"]/a/@href').extract()
        for link in Profile_link:
            agent_url = response.urljoin(link)
            logging.warning(meta)
            yield Request(url=agent_url, callback=self.parse_data, headers=headers, meta=meta)

    def parse_data(self, response):
        # GRAB XPATH
        NAME_XPATH = '//h2/text()'
        TITLE_XPATH = '//h4[@class="credentials"]/text()'
        DESCRIPTION_XPATH = '//div[@class="agent_bio"]/ul//li/text()|//div[@class="agent_bio"]//p//text() | //div[@class="agent_bio"]/div/text()'
        FACEBOOK_XPATH = '//ul[@class="social"]/li[@class="fcbk"]/a[contains(@href,"facebook.com")]/@href'
        TWITTER_XPATH = '//ul[@class="social"]/li[@class="twtr"]/a[contains(@href,"twitter.com")]/@href'
        LINKEDIN_XPATH = '//ul[@class="social"]/li[@class="lkin"]/a[contains(@href,"linkedin.com")]/@href'
        PINTEREST_XPATH = '//ul[@class="social"]/li[@class="ptrt"]/a[contains(@href,"pinterest.com")]/@href'
        GOOGLEPLUS_XPATH = '//ul[@class="social"]/li[@class="gpls"]/a[contains(@href,"plus.google.com")]/@href'
        INSTAGRAM_XPATH = '//ul[@class="social"]/li[@class="istg"]/a[contains(@href,"instagram.com")]/@href'
        BLOG_XPATH = '//ul[@class="social"]/li[@class="blog"]/a[contains(@href,"blog.firstweber.com")]/@href'
        HOME_PHONE_XPATH = '//div[@class="phone"]/span[starts-with(text(), "Home")]/text()'
        MOBILE_PHONE_XPATH = '//div[@class="phone"]/span[starts-with(text(), "Mobile")]/text()'
        WORK_PHONE_XPATH = '//div[@class="phone"]/span[starts-with(text(), "Work")]/text()'
        DIRECT_PHONE_XPATH = '//div[@class="phone"]/span[starts-with(text(), "Direct")]/text()'

        # FETCHING XPATH
        name = response.xpath(NAME_XPATH).extract_first('')
        title = response.xpath(TITLE_XPATH).extract_first('')
        description = response.xpath(DESCRIPTION_XPATH).extract()
        facebook_url = response.xpath(FACEBOOK_XPATH).extract_first('')
        twitter_url = response.xpath(TWITTER_XPATH).extract_first('')
        linkedin_url = response.xpath(LINKEDIN_XPATH).extract_first('')
        pinterest_url = response.xpath(PINTEREST_XPATH).extract_first('')
        googleplus_url = response.xpath(GOOGLEPLUS_XPATH).extract_first('')
        instagram_url = response.xpath(INSTAGRAM_XPATH).extract_first('')
        blog_url = response.xpath(BLOG_XPATH).extract_first('')
        home_phone = response.xpath(HOME_PHONE_XPATH).extract_first('')
        mobile_phone = response.xpath(MOBILE_PHONE_XPATH).extract_first('')
        work_phone = response.xpath(WORK_PHONE_XPATH).extract_first('')
        direct_phone = response.xpath(DIRECT_PHONE_XPATH).extract_first('')

        # CLEANING XPATH
        agent_name = name.replace('-', ' ').split()
        first_name = ''
        middle_name = ''
        last_name = ''
        if '&' in agent_name:
            first_name = name
        else:
            if len(agent_name) == 1:
                first_name = agent_name[0]
                middle_name = ''
                last_name = ''
            if len(agent_name) == 2:
                first_name = agent_name[0]
                middle_name = ''
                last_name = agent_name[1]
            if len(agent_name) == 3:
                first_name = agent_name[0]
                middle_name = agent_name[1]
                last_name = agent_name[2]
            if len(agent_name) >= 4:
                first_name = name
                middle_name = ''
                last_name = ''

        description = ' '.join(''.join(description).split())
        address = ''
        zipcode = ''
        city = ''
        state = ''
        office_name = ''
        agent_phone_numbers = []
        office_phone_numbers = []

        award = response.xpath(
            '//div[@class="agent_data"]/h4/text()').extract_first('').strip().replace('\r\n', ' ')
        res_body = re.sub(
            b",\n\s*\"description\":\s\"(?:.|\n)*?\"", b"", response.body)
        sel_ = Selector(text=res_body)
        JSON_XPATH = '//script[contains(text(),"@context")]/text()'
        json_ = sel_.xpath(JSON_XPATH).extract()
        if json_:
            json_ = ' '.join(' '.join(json_).split()).strip(
            ).replace(name, "").replace(award, "") if json_ else ''
            try:
                json_data = json.loads(json_)
            except:
                pass
            office_name = json_data.get('location', {}).get('name', '')
            office_name = office_name + ' ' + 'office'
            email = json_data.get('email', '')
            image_url = json_data.get('image', '')
            websites = json_data.get('url', '')
            if websites == 'https://':
                websites = ''
            elif websites == 'http://':
                websites = ''

            agent_address = json_data.get('address', {})
            address = agent_address.get('streetAddress', '')
            zipcode = agent_address.get('postalCode', '')
            city = agent_address.get('addressLocality', '')
            state = agent_address.get('addressRegion', '')

        if 'www.facebook.com' in facebook_url:
            facebook_url = facebook_url.strip()
        else:
            facebook_url = ''
        if 'twitter.com' in twitter_url:
            twitter_url = twitter_url.strip()
        else:
            twitter_url = ''
        if 'www.linkedin.com' in linkedin_url:
            linkedin_url = linkedin_url.strip()
        else:
            linkedin_url = ''
        if 'www.pinterest.com' in pinterest_url:
            pinterest_url = pinterest_url.strip()
        else:
            pinterest_url = ''
        if 'google.com' in googleplus_url:
            googleplus_url = googleplus_url.strip()
        else:
            googleplus_url = ''
        if '/blog/' in blog_url:
            blog_url = blog_url.strip()
        else:
            blog_url = ''
        if 'instagram.com' in instagram_url:
            instagram_url = instagram_url.strip()
        else:
            googleplus_url = ''

        other_urls_ = []

        if pinterest_url:
            other_urls_.append(pinterest_url)
        if googleplus_url:
            other_urls_.append(googleplus_url)
        if blog_url:
            other_urls_.append(blog_url)
        if instagram_url:
            other_urls_.append(instagram_url)

        other_urls = []
        for url in other_urls_:
            if url:
                other_urls.append(url)
            else:
                other_urls = []

        if facebook_url or twitter_url or linkedin_url or other_urls:
            social = {'facebook_url': facebook_url,
                      'twitter_url': twitter_url,
                      'linkedin_url': linkedin_url,
                      'other_urls': other_urls,
                      }
        else:
            social = {}
        if mobile_phone:
            agent_phone_number = mobile_phone.replace('Mobile:', '').replace(
                '(call/text)', '').replace('\xa0', '').strip()
            agent_phone_numbers.append(agent_phone_number)
        if work_phone:
            office_phone_number = work_phone.replace('Work:', '').replace(
                'Phone:', '').replace('Work Fax:', '').replace('eFax', '').strip()
            office_phone_numbers.append(office_phone_number)
        if direct_phone:
            direct_phone_number = direct_phone.replace('Direct:', '')
            agent_phone_numbers.append(direct_phone_number)

        # agent_phone_numbers = home_phone + mobile_phone + direct_phone
        # office_phone_numbers = work_phone
        if not office_phone_numbers:
            if response.meta.get('office_phone_numbers'):
                office_phone_numbers = response.meta.get(
                    'office_phone_numbers')
        if description:
            cleanr = re.compile('<.*?>')
            description = re.sub(cleanr, '', description)
            description = re.sub(r'[^\x00-\x7f]', r'', description)
            description = description.replace('\n', '').replace(
                '\r', '').replace('\t', '').replace('\\', '')
        else:
            description = ''

        # YIELDING ITEM
        if first_name:
            item = FirstweberItem(
                title=title,
                office_name=office_name,
                address=address,
                city=city,
                state=state,
                zipcode=zipcode,
                profile_url=response.request.url,
                languages=[],
                description=description,
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                website=websites,
                email=email,
                image_url=image_url,
                agent_phone_numbers=agent_phone_numbers,
                office_phone_numbers=office_phone_numbers,
                social=social,
                country='United States',
            )
            yield item
#
