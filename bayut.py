header={"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
"cache-control": "max-age=0",
"cookie": "device_id=kyjyvsw0n9d9x3pbd; os_name=N%2FA; os_version=N%2FA; browser_name=N%2FA; browser_version=N%2FA; settings=%7B%22area%22%3Anull%2C%22currency%22%3A%22AED%22%2C%22installBanner%22%3Atrue%2C%22searchHitsLayout%22%3A%22LIST%22%7D; abTests=%7B%22MobileChatButton%22%3A%22bubble_button%22%2C%22EmailAlertsBanners%22%3A%22original%22%2C%22SearchPageListingCard%22%3A%22original%22%2C%22CompactNavBar%22%3A%22original%22%7D; banners=%7B%7D; userLocation=%7B%22countryCode%22%3Anull%2C%22countryName%22%3Anull%2C%22cityName%22%3Anull%7D; userGeoLocation=%7B%22coordinates%22%3Anull%2C%22closestLocation%22%3Anull%2C%22loading%22%3Afalse%2C%22error%22%3Anull%7D; _gcl_au=1.1.697229358.1642501332; _fbp=fb.1.1642501332237.23341741; TRUCHECK_ACKNOWLEDGED=true; FPID=FPID2.2.9r9PR0nPgF0M5uyP06BZl64aTVCqqMa4MQ8pFzs3oRw%3D.1642501332; __gads=ID=c92b130eb7dcfda1:T=1642501332:S=ALNI_MZnRrlkA-FNwqkS5ZyS2ehtlkB-Tw; _gid=GA1.2.2064655876.1642661186; anonymous_session_id=943ac28b-ce7f-416c-ace2-d6802b75ea60; PHPSESSID=pc4iol3bqkfachhvl9fvivfv41; moe_uuid=f2b0e59e-ccd2-4820-b18e-533e720ed026; FPLC=wQ%2BAb0m%2FzcMlOK0kjEdaqh7pHFaBWFwRkiPBJNaUs99pYqc4Qpzayx9XyfkDf9ta88rlOm8zYfIX64egtoj09%2FCc6UJeMrTp1iqGv%2BHO8qIqQ1MKBrvmwY7Eil%2FkBg%3D%3D; AMP_TOKEN=%24NOT_FOUND; _gat_UA-201547-17=1; _gat_UA-201547-38=1; _dc_gtm_UA-201547-17=1; _ga_YTDB8TQ5Q9=GS1.1.1642755262.9.1.1642755365.40; _ga_JMZ5C490RT=GS1.1.1642755262.8.1.1642755365.0; AWSALB=/eqeLhsuQzP6OIRE4nd8Vhh4ItcGM2tsF31RI5kXGY5SXqVDsoHMhIvKULzbUrCd9hbDsGwey+a9W0D2tP27NRWamB2LQ42KekVLW42S40wCWyOnGNda4L1l4x/1; AWSALBCORS=/eqeLhsuQzP6OIRE4nd8Vhh4ItcGM2tsF31RI5kXGY5SXqVDsoHMhIvKULzbUrCd9hbDsGwey+a9W0D2tP27NRWamB2LQ42KekVLW42S40wCWyOnGNda4L1l4x/1; XSRF-TOKEN=eyJpdiI6InU3d0FCNVZvazhRQUI2cmNYU2xHc1E9PSIsInZhbHVlIjoidU83VExqYXVaTlRudWtCV29ibUhtRDhXZU81NllLaVEwajZ2QThvaVZjb1ZndFFabVBmVnJBWXFQRkZyQm9sZENQUjdwY2FxU0FGYjIxNTZNdllITnc9PSIsIm1hYyI6ImM5MGQ4ZGY2ZTNmZWU1MjgzMzQ3YjM1NmU1NGRhMzVjMmE1OWI5M2ExOGRjY2NhNzdmNzhjNmE2N2VlY2U3OWMifQ%3D%3D; byt_session=eyJpdiI6ImhuVlltZkhQUnBpR3RPcm1uZitNY2c9PSIsInZhbHVlIjoiR0xrYkRQUUFpaDRtbmNoeU9VRFpjVXRrNU51V2ROWW1qQ0pvSlJuNWdNTEZhUDV3NHVGd1dMSTRcL0owVmJkMU94ZkpraFFBWHBFU3M5OTBpaEpcL3ZqZz09IiwibWFjIjoiNWYxMzQ1NTA2OWQ4MzIyNGYyNDcwOGQzZmRiZjlkYTA2ZWFiMWQyODQ5Y2QxMjBhYjdjYTI3ZGM5M2JiMzhhNSJ9; landing_url=%2Fto-rent%2Fproperty%2Fdubai%2F; _ga=GA1.2.18016187.1642501332",
"sec-ch-ua": '"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Linux",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
}


from lxml import html
import requests
import json
import pymongo
from pymongo import MongoClient
import pprint
client = MongoClient()
db=client.bayut

ref_id='//span[@aria-label="Reference"]/text()'
purpose='//li/span[@aria-label="Purpose"]/text()'
types='//span[@aria-label="Type"]/text()'
added_on='//li/span[@aria-label="Reactivated date"]/text()'
furnishing='//li/span[@aria-label="Furnishing"]/text()'
price='//div/span[@aria-label="Price"]//text()'
currency='//div/span[@aria-label="Currency"]/text()'
location='//div[@aria-label="Property header"]/text()'
bed='//span[@aria-label="Beds"]//text()'
bath='//span[@aria-label="Baths"]//text()'
size='//span[@aria-label="Area"]//text()'
p_no='//div/span[@class="ff863316"]/text()'
agent_name='//div/span[@aria-label="Agent name"]/text()'
img='//img[@title="1 "]/@src'
breadcrumbs='//span[@aria-label="Link name"]//text()'
aminities='//div[@class="ef5bd664"]//text()'
description='//div[@aria-label="Property description"]//text()'

base_url='https://www.bayut.com'
url='https://www.bayut.com/to-rent/property/dubai/'

def data(urls):
	page = requests.get(url=urls,headers=header)
	tree = html.fromstring(page.content)
	r="".join(tree.xpath(ref_id))
	p="".join(tree.xpath(purpose))
	t="".join(tree.xpath(types))
	a="".join(tree.xpath(added_on))
	f="".join(tree.xpath(furnishing))
	pr="".join(tree.xpath(price))
	cr="".join(tree.xpath(currency))
	lo="".join(tree.xpath(location))
	bd="".join(tree.xpath(bed))
	bt="".join(tree.xpath(bath))
	sz="".join(tree.xpath(size))
	pn="".join(tree.xpath(p_no))
	an="".join(tree.xpath(agent_name))
	im="".join(tree.xpath(img))
	bc="".join(tree.xpath(breadcrumbs))
	am="".join(tree.xpath(aminities))
	des="".join(tree.xpath(description))

	item={}
	item["property_id"]=r
	item["purpose"]=p
	item["types"]=t
	item["added_on"]=a
	item["furnishing"]=f
	item["price"]={"currency":cr,
	                "amount":pr}
	item["location"]=lo	
	item["bed_bath_size"]={"bedroom":bd,
	                        "bath":bt,
	                        "size":sz}
	item["permit_no"]=pn
	item["Agent_name"]=an
	item["img_url"]=im
	item["Breadcrumbs"]=bc
	item["Aminities"]=am
	item["description"]=des	
	post=db.login.insert_one(item)								
	# details=json.dumps(item)
	# with open("outs.json","a") as f:
	#   f.write(json.dumps(json.loads(details),indent=4))

def links(pages):
	try:
		page = requests.get(url = pages, headers = header)
		response = html.fromstring(page.content)
		links = response.xpath('//a[@aria-label="Listing link"]/@href')
		for link in links:
			print(link)
			data(base_url+link)
	except:
		# print("value error")	
		pass
try:
	while True:
		page = requests.get(url = url, headers = header)
		response = html.fromstring(page.content)
		linkss="".join(response.xpath('//a[@title="Next"]/@href'))
		links(base_url+linkss)
		print(base_url+linkss)
		url=base_url+linkss
except:
	print("END")





