import logging
from firstweber.proxy import parse_proxy
# from fake_useragent import UserAgent

logger = logging.getLogger(__name__)


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        proxy = parse_proxy()
        request.meta['proxy'] = proxy['proxy_url']


class RandomUserAgentMiddleware(object):

    def process_request(self, request, spider):
        try:
            ua = UserAgent()
            ua = ua.random
        except:
            ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        if ua:
            request.headers.setdefault('User-Agent', ua)
        logger.debug("USER AGENT IS: " + ua)
