
# title
# response.xpath('//h1/text()').extract_first()

# MRP
#  response.xpath('//span[text()="MRP:"]/following-sibling::span/text()').extract_first() 



# # reviews

# # response.xpath('//div[@itemprop="aggregateRating"]/following::div[4]/text()').extract_first() 

# # rating

# # response.xpath('//div[@itemprop="aggregateRating"]/following::div[2]/text()').extract_first()   





# reviews
# a=response.xpath('//div[@itemprop="aggregateRating"]/preceding::div/text()').extract_first()                                        

#  a=float(a)/5  

# ratingValue b=response.xpath('//div[@itemprop="aggregateRating"]/following::div[2]/text()').extract_first()                                     

#  b=float(b)  

#  
#  mrp=response.xpath('//span[text()="MRP:"]/following-sibling::span/text()').extract_first().strip("₹")                               

#   mrp=float(mrp)                                                                                                                                 
#  