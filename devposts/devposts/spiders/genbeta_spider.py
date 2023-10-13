import scrapy

from devposts.items import PostItem

class GenbetaSpider(scrapy.Spider):
    name = "genbeta"
    start_urls = ["https://genbeta.com"]

    def parse(self, response):
        pass
