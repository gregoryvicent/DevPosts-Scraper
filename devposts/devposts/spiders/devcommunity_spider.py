import scrapy
from devposts.items import DevCommunityPostItem

class DevCommunitySpider(scrapy.Spider):
    name = "devCommunity"
    start_urls = ["https://dev.to/"]
    DevCommunityPost = DevCommunityPostItem()

    def parse(self, response):
        links = response.css("main div.crayons-story a.crayons-story__hidden-navigation-link::attr(href)").getall()
        for link in links:
            if link is not None:
                yield response.follow(link, callback=self.get_post_info)

    def get_post_info(self, response):
        self.DevCommunityPost["title"] = response.css("h1::text").get()
        self.DevCommunityPost["date"] = response.css("time::attr(datetime)").get()
        self.DevCommunityPost["link"] = response.url
        yield self.DevCommunityPost
        yield scrapy.Request("https://dev.to/", callback=self.parse)

