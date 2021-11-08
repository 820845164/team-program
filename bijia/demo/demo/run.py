from scrapy import cmdline
cmdline.execute("scrapy crawl myspiders -s LOG_ENABLED=True".split())