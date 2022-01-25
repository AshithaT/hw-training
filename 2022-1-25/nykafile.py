
import datetime
import json

item={}

# mrp=response.xpath('//span[text()="MRP:"]/following-sibling::span/text()').extract_first()
# reviews=response.xpath('//div[@itemprop="aggregateRating"]/following::div[4]/text()').extract_first() 
# rating=response.xpath('//div[@itemprop="aggregateRating"]/following::div[2]/text()').extract_first() 

product_name=response.xpath('//h1/text()').extract_first()
reviews=response.xpath('//div[@itemprop="aggregateRating"]/preceding::div/text()').extract_first()                                        
reviews=float(reviews)/5  
rating=response.xpath('//div[@itemprop="aggregateRating"]/following::div[2]/text()').extract_first()                             
rating=float(rating)  
mrp=response.xpath('//span[text()="MRP:"]/following-sibling::span/text()').extract_first().strip("₹")                               
mrp=float(mrp)

expiry_date=response.xpath("//script[contains(text(),'expiry')]/text()").extract_first()                                            
expiry_date=expiry_date.split(",")
expiry_date= ["{"+s+"}" for s in expiry_date  if "expiry" in s]
expiry_date = json.loads(str(expiry_date[-1]))
expiry_date=datetime.datetime.strptime(expiry_date['expiry'], '%d %B %Y').strftime('%Y/%m/%d')

country_of_origin=response.xpath("//script[contains(text(),'originOfCountryName')]/text()").extract_first()
country_of_origin=country_of_origin.split(",")
country_of_origin= ["{"+s+"}" for s in country_of_origin  if "originOfCountryName" in s]
country_of_origin = json.loads(str(country_of_origin[-1]))
item["country_of_origin"]=country_of_origin['originOfCountryName']

item['product_name']=product_name
item['reviews']=reviews
item['rating']=rating
item['mrp']=mrp
item['expiry_date']=expiry_date
item['country_of_origin']=country_of_origin




