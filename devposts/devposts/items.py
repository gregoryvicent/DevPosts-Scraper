# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DevCommunityPostItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()


class PostItem(scrapy.Item):
    title = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()

