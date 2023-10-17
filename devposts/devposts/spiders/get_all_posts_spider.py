import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from devposts.spiders.xataka_spider import XatakaSpider
from devposts.spiders.devcommunity_spider import DevCommunitySpider
from devposts.spiders.freecodecamp_es_spider import FreeCodeCampSpider
from devposts.spiders.genbeta_spider import GenbetaSpider
from devposts.spiders.linux_adictos_spider import LinuxAdictosSpider 

class GetAllPostsSpider(scrapy.Spider):
    name = "getallposts"


process = CrawlerProcess(get_project_settings())

process.crawl(DevCommunitySpider)
process.crawl(XatakaSpider)
process.crawl(FreeCodeCampSpider)
process.crawl(GenbetaSpider)
process.crawl(LinuxAdictosSpider)
process.start()