import scrapy

from devposts.items import PostItem

# Spider que extrae información de los posts del sitio web https://linuxadictos.com
class LinuxAdictosSpider(scrapy.Spider):
    name = "linuxAdictos"
    start_urls = ["https://www.linuxadictos.com/"]

    def parse(self, response):
        main = response.css("div.content") # Elemento HTML contenedor de los posts
        post = PostItem() # Estructura de los datos a extraer

        # Recorremos cada uno de los articulos de posts y extraemos sus datos
        for article in main.css("article.post"):
            post["title"] = article.css("h2 a::text").get()
            post["link"] = article.css("h2 a::attr(href)").get()
            post["date"] = article.css("time::attr(datetime)").get()
            post["image"] = article.css("img::attr(src)")[1].get()
            yield post

        link = response.css("footer.page-footer a::attr(href)").get() # Obtenemos el link a la siguiente pagina de posts
        number_page = int(link[-1]) # Se obtinen el numero de la pagina actual

        if link is not None and number_page <= 5: # Verificamos que exista el link y que solo busquemos dentro de las primeras 5 paginas
            yield scrapy.Request(link, callback=self.parse) # Ejecutamos nuevamente el codigo que esta en el metodo 'parse' en la nueva url