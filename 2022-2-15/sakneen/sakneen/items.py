
import scrapy


class SakneenItem(scrapy.Item):
    # url = scrapy.Field()
    
    def __setitem__(self, key, value):
        self._values[key] = value
        self.fields[key] = {}