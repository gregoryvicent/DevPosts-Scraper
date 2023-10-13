import scrapy

from devposts.items import PostItem

# Spider que extrae información de los posts del dia de https://genbeta.com
class GenbetaSpider(scrapy.Spider):
    name = "genbeta"
    start_urls = ["https://genbeta.com"]

    def parse(self, response):
        main = response.css("main") # Extraemos la etiqueta main del HTML
        post = PostItem() # Estructura de nuestros datos

        # Se recorren cada uno de los articulos y se extraen los datos requeridos
        for article in main.css("article"):
            post["title"] = article.css("h2 a::text").get()
            post["link"] = article.css("h2 a::attr(href)").get()
            post["image"] = article.css("img::attr(src)").get()
            post["date"] = article.css("time::attr(datetime)").get()
            yield post 

