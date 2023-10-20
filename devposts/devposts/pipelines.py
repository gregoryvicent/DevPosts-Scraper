# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter
from scrapy.exporters import JsonLinesItemExporter


class DevpostsStoreJsonPipeline:
    posts_list = []

    def process_item(self, item, spider):
        try:
            adapter = ItemAdapter(item)
            post = {}
            if adapter["title"] is None or adapter["link"] is None or adapter["date"] is None or adapter["image"] is None:
                return item
            post["title"] = adapter["title"]
            post["link"] = adapter["link"]
            post["date"] = adapter["date"]
            post["image"] = adapter["image"]
            self.posts_list.append(post)
            return item
        except KeyError:
            print("Image not found")

    def close_spider(self, spider):
        data = json.dumps(self.posts_list, ensure_ascii=True)
        with open("posts.json", "w", encoding="utf-8") as file:
            file.write(data)