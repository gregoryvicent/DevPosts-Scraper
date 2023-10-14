import scrapy

from devposts.itemLoaders.freecodecampPostsLoader import FreeCodeCampPostsLoader 
from devposts.items import PostItem

class FreeCodeCampSpider(scrapy.Spider):
    name = "freecodecamp"
    start_urls = ["https://www.freecodecamp.org/espanol/news/"]

    def parse(self, response):
        main = response.css("div.inner")

        for article in main.css("article.post-card"):
            post = FreeCodeCampPostsLoader(item=PostItem(), selector=article)
            post.add_css("title", "h2 a::text")
            post.add_css("link", "h2 a::attr(href)")
            post.add_css("date", "time::attr(datetime)")
            post.add_css("image", "img::attr(src)")
            yield post.load_item()