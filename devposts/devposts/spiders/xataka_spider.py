import scrapy

from devposts.items import PostItem

# Extrae la información de los posts de https://www.xataka.com
class XatakaSpider(scrapy.Spider):
    name = "xataka"
    start_urls = ["https://www.xataka.com/tag/programacion"]

    # Hacemos la busqueda y extracción de la información de los posts
    def parse(self, response):
        main = response.css("div.section-recent-list") # Elemento HTML principal donde estan los posts
        post = PostItem() # Estructura de los datos

        # Recorremos cada posts y extraemos sus datos - Solo de la primera pagina
        for article in main.css("article.recent-abstract"):
            post["title"] = article.css("h2 a::text").get()
            post["link"] = article.css("h2 a::attr(href)").get()
            post["date"] = article.css("time::attr(datetime)").get()
            post["image"] = article.css("img::attr(src)").get()
            yield post