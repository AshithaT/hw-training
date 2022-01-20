# from requests_html import HTMLSession
# session = HTMLSession()
# r = session.get('https://www.bayut.com/to-rent/property/dubai/')
# r.html.links
# print(r)

from lxml import html
import requests
headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"} 
page = requests.get('https://www.bayut.com/to-rent/property/dubai/',headers=headers)
tree = html.fromstring(page.content)
print(page.text)
hotel_name = tree.xpath('//div[@class="e676c252"]/text()')

print(hotel_name)
