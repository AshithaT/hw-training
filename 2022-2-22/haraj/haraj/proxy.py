import logging
import random
import json

logger = logging.getLogger(__name__)


def parse_proxy():

    # PROXY_LIST = requests.get('http://68.183.58.145/microleaves',
                              # headers={"x-api-key": "_/&IWn<rJ5hDTdq"}).json()
    PROXY_LIST = requests.get('http://68.183.58.145/stormproxies?',
                              headers={"x-api-key": "_/&IWn<rJ5hDTdq"}).json()
    PROXY = random.choice(PROXY_LIST)
    proxy_url = "http://%s" % PROXY
    proxies = {"http": "http://%s" % PROXY,
               "https": "http://%s" % PROXY}
    logger.debug("Proxy added")
    return {'proxies': proxies, 'proxy_url': proxy_url}