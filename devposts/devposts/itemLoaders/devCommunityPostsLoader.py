from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader

class DevCommunityPostsLoader(ItemLoader):
    default_output_processor = TakeFirst()
    title_in = MapCompose(lambda x: x[15:-13]) # Limpiamos el titulo de cada post
    # link_in = MapCompose()
    # date_in = MapCompose()

