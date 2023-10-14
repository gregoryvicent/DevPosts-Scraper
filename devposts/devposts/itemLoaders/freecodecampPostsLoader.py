from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


class FreeCodeCampPostsLoader(ItemLoader):
    default_output_processor = TakeFirst()
    title_in = MapCompose(lambda x: x[29:-25])
    link_in = MapCompose(lambda x: f"https://freecodecamp.org{x}")