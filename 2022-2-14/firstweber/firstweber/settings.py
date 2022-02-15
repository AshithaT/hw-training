# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
now = datetime.now()
day = int(now.strftime("%d"))
if day > 20:
    db_month = now + relativedelta(months=+1)
else:
    db_month = now
new_format = "%Y_%m"
db_date = db_month.strftime(new_format)
dbname = 'kw_monthly_' + db_date

# dbname='automation_test_kw'
FEED_EXPORT_ENCODING = 'utf-8'
BOT_NAME = 'firstweber'

SPIDER_MODULES = ['firstweber.spiders']
NEWSPIDER_MODULE = 'firstweber.spiders'

AUTHOR_EMAIL = ''
# Crawl responsibly by identifying yourself (and your website) on the
# user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

# Duplicate filtering field in item for both mongo and DC
DUP_KEY = ''

# Configure QUEUE
# QUEUE_NAME = 'firstweber'
# QUEUE_IP = '174.138.80.75'
# QUEUE_USER = 'datahut'
# QUEUE_PASS = 'betaqueue123'

# Configure MONGODB
# MONGO_URI = 'mongodb://localhost:27017'  # local
MONGO_URI = 'mongodb://datahut:cGFzc21lMTIz@104.131.41.31:27017/?authSource=admin&retryWrites=false'  # shard
MONGO_DB = dbname
MONGO_COLLECTION = 'firstweber_data'
# MONGO_COLLECTION_URL = 'firstweber_urls'

# Enable or disable downloader middlewares
DOWNLOADER_MIDDLEWARES = {
    'firstweber.middlewares.RandomUserAgentMiddleware': 100,
    'firstweber.middlewares.ProxyMiddleware': 110,
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 130,
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,

}

# Enable or disable extensions
EXTENSIONS = {
    # 'general_validator.GeneralValidator': 100,
    # 'sc_mongo.ScrapyMongoExtension': 400,
}

# Configure DC
# SC_MONGO_EXT_ENABLED = True

# Configure item pipelines
ITEM_PIPELINES = {
    'firstweber.pipelines.FirstweberPipeline': 300,
}


# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Enable and configure the AutoThrottle extension (disabled by default)
#AUTOTHROTTLE_ENABLED = True
