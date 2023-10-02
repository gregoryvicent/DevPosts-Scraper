import scrapy

class DevCommunitySpider(scrapy.Spider):
    name = "devCommunity"
    start_urls = ["https://dev.to/"]

    def parse(self, response):
        links = response.css("main div.crayons-story a.crayons-story__hidden-navigation-link::attr(href)").getall()
        for link in links:
            if link is not None:
                yield response.follow(link, callback=self.get_post_info)

    def get_post_info(self, response):
        data_post = {
            "title": response.css("h1::text").get(),
            "date": response.css("time::attr(datetime)").get(),
            "link": response.url
        }
        print(data_post)
        yield scrapy.Request("https://dev.to/", callback=self.parse)

