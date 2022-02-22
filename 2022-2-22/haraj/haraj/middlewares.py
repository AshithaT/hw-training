from scrapy import signals
import logging
# from sakneen.proxy import parse_proxy


logger = logging.getLogger(__name__)
class HarajSpiderMiddleware:
    
    def process_request(self, request, spider):
            proxy = parse_proxy()
            request.meta['proxy'] = proxy['proxy_url']


class HarajDownloaderMiddleware:
    def process_request(self, request, spider):
        try:
            ua = UserAgent()
            ua = ua.random
        except:
            ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
        if ua:
            request.headers.setdefault('User-Agent', ua)
        logger.debug("USER AGENT IS: " + ua)