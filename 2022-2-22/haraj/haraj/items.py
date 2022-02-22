import scrapy


class harajItem(scrapy.Item):
    def __setitem__(self, key, value):
        self._values[key] = value
        self.fields[key] = {}
