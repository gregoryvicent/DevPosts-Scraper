# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonLinesItemExporter


class DevpostsStoreJsonPipeline:
    def process_item(self, item, spider):
        json_file = open("posts.json", "ab")
        exporter = JsonLinesItemExporter(json_file)
        exporter.start_exporting()
        exporter.export_item(item)
        # print("Start++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        # print(f"{item},")
        # print("End++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        exporter.finish_exporting()
        json_file.close()
        return item