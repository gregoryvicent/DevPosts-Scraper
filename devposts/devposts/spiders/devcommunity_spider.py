import scrapy
from devposts.itemLoaders.devCommunityPostsLoader import DevCommunityPostsLoader # ItemLoader para el analisis de los datos
from devposts.items import DevCommunityPostItem # Esquema para los datos de este Spider

# Spider que hace web scraping en 'https://dev.to/'
class DevCommunitySpider(scrapy.Spider):
    name = "devCommunity"
    start_urls = ["https://dev.to/"]

    def parse(self, response):
        # Extraemos  los links de la pagina principal sobre los que buscaremos la información
        links = response.css("main div.crayons-story a.crayons-story__hidden-navigation-link::attr(href)").getall()
        for link in links:
            if link is not None:
                yield response.follow(link, callback=self.get_post_info) # Entramos en cada post

    def get_post_info(self, response):
        # Aquí ya estamos dentro de cada uno de los posts
        main = response.css("main")
        post = DevCommunityPostsLoader(item=DevCommunityPostItem(), selector=main)
        post.add_css("title", "h1::text")
        post.add_css("date", "time::attr(datetime)")
        post.add_value("link", response.url)
        yield post.load_item()
        yield scrapy.Request(response.url, callback=self.parse) # Regresamos a la pagina principal de 'https://dev.to/'

